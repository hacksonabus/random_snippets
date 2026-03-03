// public_ip_intel.go
//
// Compile with:
//     go build -o public_ip_intel public_ip_intel.go
//
// Cross-compile for Windows:
//     GOOS=windows GOARCH=amd64 go build -o public_ip_intel.exe public_ip_intel.go
//
// Description:
//     - Detects your current public IP
//     - Queries Censys v3 Asset API for IP information
//     - Queries Shodan host API for IP information
//     - Outputs JSON with aggregated results and any errors
//
// Requirements:
//     - Environment variables:
//         CENSYS_API_TOKEN : Your Censys personal access token
//         SHODAN_API_KEY   : Your Shodan API key (optional, Shodan errors handled gracefully)
//
// Notes:
//     - Censys uses "result.resource" as the correct JSON key
//     - Shodan returns 404 if IP not scanned; handled in output
//     - Both lookups timeout after 15 seconds
//

package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net"
	"net/http"
	"os"
	"strings"
	"time"
)

//
// -------------------- Public IP Discovery --------------------
//

func getPublicIP() (string, error) {
	services := []string{
		"https://api.ipify.org",
		"https://icanhazip.com",
		"https://ifconfig.me/ip",
		"https://checkip.amazonaws.com",
	}

	client := &http.Client{Timeout: 5 * time.Second}

	for _, url := range services {
		resp, err := client.Get(url)
		if err != nil {
			continue
		}

		body, err := io.ReadAll(resp.Body)
		resp.Body.Close()
		if err != nil {
			continue
		}

		ip := strings.TrimSpace(string(body))
		if net.ParseIP(ip) != nil {
			return ip, nil
		}
	}

	return "", fmt.Errorf("unable to determine public IP")
}

//
// -------------------- Censys v3 Asset API Models --------------------
//

type CensysResponse struct {
	Result struct {
		Resource CensysHostResource `json:"resource"`
	} `json:"result"`
}

type CensysHostResource struct {
	IP string `json:"ip,omitempty"`

	Location *struct {
		Continent   string `json:"continent,omitempty"`
		Country     string `json:"country,omitempty"`
		CountryCode string `json:"country_code,omitempty"`
		City        string `json:"city,omitempty"`
		Province    string `json:"province,omitempty"`
		PostalCode  string `json:"postal_code,omitempty"`
		Timezone    string `json:"timezone,omitempty"`
	} `json:"location,omitempty"`

	AutonomousSystem *struct {
		ASN         int    `json:"asn,omitempty"`
		Name        string `json:"name,omitempty"`
		Description string `json:"description,omitempty"`
		BGPPrefix   string `json:"bgp_prefix,omitempty"`
		CountryCode string `json:"country_code,omitempty"`
	} `json:"autonomous_system,omitempty"`

	Services []struct {
		Port     int    `json:"port,omitempty"`
		Protocol string `json:"protocol,omitempty"`
	} `json:"services,omitempty"`

	ServiceCount int `json:"service_count,omitempty"`
}

//
// -------------------- Shodan API Models --------------------
//

type ShodanHost struct {
	IP        string `json:"ip_str,omitempty"`
	ASN       string `json:"asn,omitempty"`
	Org       string `json:"org,omitempty"`
	OS        string `json:"os,omitempty"`
	Country   string `json:"country_name,omitempty"`
	City      string `json:"city,omitempty"`
	ISP       string `json:"isp,omitempty"`
	Ports     []int  `json:"ports,omitempty"`
	Hostnames []string `json:"hostnames,omitempty"`
	Data      []struct {
		Port      int    `json:"port,omitempty"`
		Transport string `json:"transport,omitempty"`
		Product   string `json:"product,omitempty"`
		Version   string `json:"version,omitempty"`
		Banner    string `json:"data,omitempty"`
	} `json:"data,omitempty"`
}

//
// -------------------- Censys Query --------------------
//

func queryCensys(ip string) (*CensysHostResource, error) {
	token := os.Getenv("CENSYS_API_TOKEN")
	if token == "" {
		return nil, fmt.Errorf("CENSYS_API_TOKEN not set")
	}

	url := fmt.Sprintf("https://api.platform.censys.io/v3/global/asset/host/%s", ip)
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return nil, err
	}

	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("Accept", "application/json")

	client := &http.Client{Timeout: 15 * time.Second}
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(resp.Body)
		return nil, fmt.Errorf("censys HTTP %d: %s", resp.StatusCode, string(body))
	}

	var parsed CensysResponse
	if err := json.NewDecoder(resp.Body).Decode(&parsed); err != nil {
		return nil, err
	}

	return &parsed.Result.Resource, nil
}

//
// -------------------- Shodan Query --------------------
//

func queryShodan(ip string) (*ShodanHost, error) {
	key := os.Getenv("SHODAN_API_KEY")
	if key == "" {
		return nil, fmt.Errorf("SHODAN_API_KEY not set")
	}

	url := fmt.Sprintf("https://api.shodan.io/shodan/host/%s?key=%s", ip, key)
	client := &http.Client{Timeout: 15 * time.Second}
	resp, err := client.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		body, _ := io.ReadAll(resp.Body)
		return nil, fmt.Errorf("shodan HTTP %d: %s", resp.StatusCode, string(body))
	}

	var host ShodanHost
	if err := json.NewDecoder(resp.Body).Decode(&host); err != nil {
		return nil, err
	}

	return &host, nil
}

//
// -------------------- Output Model --------------------
//

type Output struct {
	IP        string              `json:"ip"`
	Timestamp time.Time           `json:"timestamp"`
	Censys    *CensysHostResource `json:"censys,omitempty"`
	Shodan    *ShodanHost         `json:"shodan,omitempty"`
	Errors    map[string]string   `json:"errors,omitempty"`
}

//
// -------------------- Main --------------------
//

func main() {
	ip, err := getPublicIP()
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	out := Output{
		IP:        ip,
		Timestamp: time.Now().UTC(),
		Errors:    make(map[string]string),
	}

	if c, err := queryCensys(ip); err != nil {
		out.Errors["censys"] = err.Error()
	} else {
		out.Censys = c
	}

	if s, err := queryShodan(ip); err != nil {
		out.Errors["shodan"] = err.Error()
	} else {
		out.Shodan = s
	}

	if len(out.Errors) == 0 {
		out.Errors = nil
	}

	enc := json.NewEncoder(os.Stdout)
	enc.SetIndent("", "  ")
	enc.Encode(out)
}
