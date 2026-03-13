# CISSP Cheat Sheet

## How to Use This Cheat Sheet

This document condenses the core knowledge areas from the CISSP Common
Body of Knowledge (CBK). It is intended for rapid review before practice
exams or certification testing.

Domains Covered: 
<ol>
  <li>Security and Risk Management</li>
  <li>Asset Security</li>
  <li>Security Architecture and Engineering</li>
  <li>Communication and Network Security</li>
  <li>Identity and Access Management</li>
  <li>Security Assessment and Testing</li>
  <li>Security Operations</li>
  <li>Software Development Security</li>
</ol>

------------------------------------------------------------------------

# Domain 1 - Security and Risk Management

## CIA Triad
<ul>
  <li>Confidentiality - Prevent unauthorized disclosure</li>
  <li>Integrity - Prevent unauthorized modification</li>
  <li>Availability - Ensure reliable access to systems and data</li>
</ul>

## Governance Components
<ul>
  <li>Policies</li>
  <li>Standards</li>
  <li>Procedures</li>
  <li>Guidelines</li>
  <li>Baselines</li>
</ul>

## Risk Terminology

| Term | Definition |
|-----|-----|
| Asset | Something of value |
| Threat | Potential cause of harm |
| Vulnerability | Weakness that can be exploited |
| Risk | Likelihood × Impact |

### Risk Formula

Risk = Threat × Vulnerability × Impact

## Risk Treatment Options
<ul>
  <li>Avoid</li>
  <li>Transfer</li>
  <li>Mitigate</li>
  <li>Accept</li>
</ul>

## Security Frameworks
<ul>
  <li>NIST Cybersecurity Framework</li>
  <li>ISO 27001</li>
  <li>COBIT</li>
  <li>SABSA</li>
</ul>

## Compliance and Legal
<ul>
  <li>Due Care</li>
  <li>Due Diligence</li>
  <li>Privacy Laws</li>
  <li>Intellectual Property</li>
</ul>

------------------------------------------------------------------------

# Domain 2 - Asset Security

## Data Classification

Typical enterprise classification:

Public -> Internal -> Confidential -> Restricted

## Data Lifecycle
<ol>
  <li>Create</li>
  <li>Store</li>
  <li>Use</li>
  <li>Share</li>
  <li>Archive</li>
  <li>Destroy</li>
</ol>

## Data Protection Methods
<ul>
  <li>Encryption</li>
  <li>Tokenization</li>
  <li>Masking</li>
  <li>Data Loss Prevention (DLP)</li>
</ul>

## Media Sanitization

| Method | Description |
|-----|-----|
| Clearing | Overwriting |
| Purging | Degaussing |
| Destruction | Physical destruction |

## Data Ownership Roles
<ul>
  <li>Data Owner</li>
  <li>Data Custodian</li>
  <li>Data Steward</li>
  <li>Data User</li>
</ul>

------------------------------------------------------------------------

# Domain 3 - Security Architecture & Engineering

## Security Design Principles
<ul>
  <li>Least Privilege</li>
  <li>Fail Secure</li>
  <li>Defense in Depth</li>
  <li>Separation of Duties</li>
  <li>Economy of Mechanism</li>
</ul>

## Security Models

### Bell-LaPadula (Confidentiality)
<ul>
  <li>No Read Up</li>
  <li>No Write Down</li>
</ul>

### Biba (Integrity)
<ul>
  <li>No Read Down</li>
  <li>No Write Up</li>
</ul>

### Clark-Wilson

Integrity through transactions and separation of duties

## Trusted Computing Base (TCB)

Components responsible for enforcing security.

## Common Criteria

Evaluation Assurance Levels (EAL1--EAL7)

## Cryptography Overview

### Symmetric Encryption
<ul>
  <li>AES</li>
  <li>ChaCha20</li>
</ul>

### Asymmetric Encryption
<ul>
  <li>RSA</li>
  <li>ECC</li>
</ul>

### Hash Functions
<ul>
  <li>SHA‑256</li>
  <li>SHA‑3</li>
</ul>

### Digital Signatures

Provide authenticity and non‑repudiation.

------------------------------------------------------------------------

# Domain 4 --- Communication & Network Security

## OSI Model

  Layer   Function
  ------- --------------
  7       Application
  6       Presentation
  5       Session
  4       Transport
  3       Network
  2       Data Link
  1       Physical

## Network Devices
<ul>
  <li>Router</li>
  <li>Switch</li>
  <li>Firewall</li>
  <li>IDS/IPS</li>
  <li>Proxy</li>
</ul>

## Network Segmentation
<ul>
  <li>VLANs</li>
  <li>DMZ</li>
  <li>Microsegmentation</li>
</ul>

## Secure Protocols

  Protocol   Use
  ---------- ----------------------
  TLS        Secure web
  SSH        Secure remote access
  IPSec      VPN tunnels
  SFTP       Secure file transfer

------------------------------------------------------------------------

# Domain 5 --- Identity and Access Management

## Authentication Factors
<ul>
  <li>Something you know</li>
  <li>Something you have</li>
  <li>Something you are</li>
  <li>Somewhere you are</li>
  <li>Something you do</li>
</ul>

## Access Control Models

  Model   Description
  ------- ------------------
  DAC     Owner controlled
  MAC     Label based
  RBAC    Role based
  ABAC    Attribute based

## Identity Lifecycle

1.  Provisioning
2.  Access assignment
3.  Monitoring
4.  De‑provisioning

## IAM Technologies
<ul>
  <li>SSO</li>
  <li>Federation</li>
  <li>Kerberos</li>
  <li>LDAP</li>
  <li>OAuth / OpenID Connect</li>
</ul>

------------------------------------------------------------------------

# Domain 6 --- Security Assessment & Testing

## Security Testing Types

### Vulnerability Scanning

Automated detection of weaknesses.

### Penetration Testing

Simulated attack.

### Security Audits

Compliance verification.

### Red vs Blue Teams
<ul>
  <li>Red Team - attacker simulation</li>
  <li>Blue Team - defense monitoring</li>
</ul>

## Continuous Monitoring
<ul>
  <li>SIEM</li>
  <li>Log analysis</li>
  <li>Threat intelligence feeds</li>
</ul>

------------------------------------------------------------------------

# Domain 7 --- Security Operations

## Incident Response Lifecycle

1.  Preparation
2.  Detection
3.  Containment
4.  Eradication
5.  Recovery
6.  Lessons Learned

## Logging Best Practices
<ul>
  <li>Centralized logging</li>
  <li>Time synchronization</li>
  <li>Log retention policies</li>
</ul>

## Digital Forensics

Key Principles: - Chain of custody - Evidence preservation - Repeatable
analysis

## Business Continuity

### RTO

Recovery Time Objective

### RPO

Recovery Point Objective

### Disaster Recovery Sites
<ul>
  <li>Cold site</li>
  <li>Warm site</li>
  <li>Hot site</li>
</ul>

------------------------------------------------------------------------

# Domain 8 --- Software Development Security

## Secure SDLC

1.  Requirements
2.  Design
3.  Development
4.  Testing
5.  Deployment
6.  Maintenance

## Security Testing in Development

  Method   Description
  -------- ----------------------
  SAST     Static code analysis
  DAST     Dynamic analysis
  IAST     Interactive testing
  SCA      Dependency analysis

## OWASP Top Vulnerabilities

Common risks: - Injection - Broken authentication - Sensitive data
exposure - Security misconfiguration - Cross‑site scripting

## DevSecOps Principles
<ul>
  <li>Automate security checks</li>
  <li>Integrate into CI/CD</li>
  <li>Continuous monitoring</li>
</ul>

------------------------------------------------------------------------

# Cryptography Quick Reference

## Encryption Types

| Type | Example |
|-----|-----|
| Symmetric | AES |
| Asymmetric | RSA |
| Hash | SHA‑256 |
| Key Exchange | Diffie‑Hellman |

## PKI Components
<ul>
  <li>Certificate Authority</li>
  <li>Registration Authority</li>
  <li>Certificates</li>
  <li>Revocation Lists</li>
</ul>

------------------------------------------------------------------------

# Networking Ports to Remember

| Port | Protocol |
|-----|-----|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3389 | RDP |

------------------------------------------------------------------------

# Security Operations Quick Reference

## Backup Types

| Type | Description |
|-----|-----|
| Full | Complete backup |
| Incremental | Changes since last backup |
| Differential | Changes since last full |

------------------------------------------------------------------------

# Threat Categories

| Threat Type | Example |
|-----|-----|
| Malware | Ransomware |
| Social Engineering | Phishing |
| Network Attacks | MITM |
| Insider Threat | Privilege abuse |

------------------------------------------------------------------------

# Security Principles Summary
<ul>
  <li>Least Privilege</li>
  <li>Need to Know</li>
  <li>Separation of Duties</li>
  <li>Defense in Depth</li>
  <li>Zero Trust</li>
</ul>

------------------------------------------------------------------------

# Quick Exam Tips
<ul>
  <li>CISSP tests **management thinking**, not just technical knowledge.</li>
  <li>Choose the **best risk management answer**, not the most technical one.</li>
  <li>Look for answers involving:
    <ul>
      <li>Policy</li>
      <li>Process</li>
      <li>Risk reduction</li>
      <li>Governance</li>
    </ul>
  </li>
</ul>

------------------------------------------------------------------------

# Last‑Minute Review Checklist

Security Governance\
Risk Management\
Access Control Models\
OSI Layers\
Incident Response\
Cryptography Basics\
Secure SDLC\
Network Security Architecture

------------------------------------------------------------------------
