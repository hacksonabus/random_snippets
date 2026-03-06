// osfingerprint.go
package main

import (
  "fmt"
  "net"
  "os"
  "time"
)

type Fingerprint struct {
  IP        string
  TTL       int
  OpenPorts []int
  Banner    string
}

func scanPort(ip string, port int) bool {
  timeout := time.Millisecond * 800
  conn, err := net.DialTimeout("tcp", fmt.Sprintf("%s:%d", ip, port), timeout)
  if err != nil {
    return false
  }
  conn.Close()
  return true
}

func scanHost(ip string) Fingerprint {
  commonPorts := []int{22, 80, 135, 139, 443, 445, 3389}
  openPorts := []int{}
  for _, port := range commonPorts {
    if scanPort(ip, port) {
      openPorts = append(openPorts, port)
    }
  }
  fp := Fingerprint{
    IP:        ip,
    TTL:       0,
    OpenPorts: openPorts,
  }
  return fp
}

func main() {
  if len(os.Args) < 2 {
    fmt.Println("usage: osfingerprint <subnet>")
    return
  }
  subnet := os.Args[1]
  for i := 1; i < 255; i++ {
    ip := fmt.Sprintf("%s.%d", subnet, i)
    fp := scanHost(ip)
    if len(fp.OpenPorts) > 0 {
      fmt.Printf("Host: %s OpenPorts: %v\n", fp.IP, fp.OpenPorts)
    }
  }
}
