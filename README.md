# Random snippets of code.
This repo is a few random snippets of code. Generally built to proof out some idea before integrating the code into a larger project.

---

### public_ip_intel.go
Quick check of your current public ip and recon of available services using Censys and Shodan.<br>
__Usage__
```
export SHODAN_API_KEY="YourShodanAPIKey"    # https://account.shodan.io/register
export CENSYS_API_TOKEN="YourCensysAPIKey"  # https://platform.censys.io/ 
go run public_ip_intel.go
```

---

### osfingerprint.go
Minimal Port Scanner...working toward an OS Fingerprinting tool.

__Usage__
```
go run osfingerprint.go
```
