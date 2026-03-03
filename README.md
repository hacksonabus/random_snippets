# random_snippets
Ransom snippets of code.

### public_ip_intel.go
Quick check of your current public ip and recon of available services using Censys and Shodan.<br>
__Usage__
```
export SHODAN_API_KEY="YourShodanAPIKey"    # https://account.shodan.io/register
export CENSYS_API_TOKEN="YourCensysAPIKey"  # https://platform.censys.io/ 
go run public_ip_intel.go
```
