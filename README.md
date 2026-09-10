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

---

### snow_catcher.py
Simple game. Spawned from a random Discord conversation.<br>
Inspired by Kaboom! - https://en.wikipedia.org/wiki/Kaboom!_(video_game)<br>

Requires PyGame

__Usage__
```
python3 snow_catcher.py
```

---

### pve-governor.sh<br>
Minimal script to set the CPU Governor of a Proxmox server.

nano /usr/local/sbin/pve-governor.sh<br>
chmod +x /usr/local/sbin/pve-governor.sh

__Usage__
```
pve-governor.sh
```

---


### cpu_freq.sh<br>
Display the current running CPU/Core frequencies.

nano /usr/local/sbin/cpu_freq.sh<br>
chmod +x /usr/local/sbin/cpu_freq.sh

__Usage__
```
cpu_freq.sh
```
