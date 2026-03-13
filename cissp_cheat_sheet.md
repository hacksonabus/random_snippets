# CISSP Cheat Sheet (20‑Page Condensed Study Guide)

## How to Use This Cheat Sheet

This document condenses the core knowledge areas from the CISSP Common
Body of Knowledge (CBK). It is intended for rapid review before practice
exams or certification testing.

Domains Covered: 1. Security and Risk Management 2. Asset Security 3.
Security Architecture and Engineering 4. Communication and Network
Security 5. Identity and Access Management 6. Security Assessment and
Testing 7. Security Operations 8. Software Development Security

------------------------------------------------------------------------

# Domain 1 --- Security and Risk Management

## CIA Triad

-   **Confidentiality** -- Prevent unauthorized disclosure
-   **Integrity** -- Prevent unauthorized modification
-   **Availability** -- Ensure reliable access to systems and data

## Governance Components

-   Policies
-   Standards
-   Procedures
-   Guidelines
-   Baselines

## Risk Terminology

  Term            Definition
  --------------- --------------------------------
  Asset           Something of value
  Threat          Potential cause of harm
  Vulnerability   Weakness that can be exploited
  Risk            Likelihood × Impact

### Risk Formula

Risk = Threat × Vulnerability × Impact

## Risk Treatment Options

-   Avoid
-   Transfer
-   Mitigate
-   Accept

## Security Frameworks

-   NIST Cybersecurity Framework
-   ISO 27001
-   COBIT
-   SABSA

## Compliance and Legal

-   Due Care
-   Due Diligence
-   Privacy Laws
-   Intellectual Property

------------------------------------------------------------------------

# Domain 2 --- Asset Security

## Data Classification

Typical enterprise classification:

Public → Internal → Confidential → Restricted

## Data Lifecycle

1.  Create
2.  Store
3.  Use
4.  Share
5.  Archive
6.  Destroy

## Data Protection Methods

-   Encryption
-   Tokenization
-   Masking
-   Data Loss Prevention (DLP)

## Media Sanitization

  Method        Description
  ------------- ----------------------
  Clearing      Overwriting
  Purging       Degaussing
  Destruction   Physical destruction

## Data Ownership Roles

-   Data Owner
-   Data Custodian
-   Data Steward
-   Data User

------------------------------------------------------------------------

# Domain 3 --- Security Architecture & Engineering

## Security Design Principles

-   Least Privilege
-   Fail Secure
-   Defense in Depth
-   Separation of Duties
-   Economy of Mechanism

## Security Models

### Bell-LaPadula (Confidentiality)

-   No Read Up
-   No Write Down

### Biba (Integrity)

-   No Read Down
-   No Write Up

### Clark-Wilson

Integrity through transactions and separation of duties

## Trusted Computing Base (TCB)

Components responsible for enforcing security.

## Common Criteria

Evaluation Assurance Levels (EAL1--EAL7)

## Cryptography Overview

### Symmetric Encryption

-   AES
-   ChaCha20

### Asymmetric Encryption

-   RSA
-   ECC

### Hash Functions

-   SHA‑256
-   SHA‑3

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

-   Router
-   Switch
-   Firewall
-   IDS/IPS
-   Proxy

## Network Segmentation

-   VLANs
-   DMZ
-   Microsegmentation

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

-   Something you know
-   Something you have
-   Something you are
-   Somewhere you are
-   Something you do

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

-   SSO
-   Federation
-   Kerberos
-   LDAP
-   OAuth / OpenID Connect

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

-   Red Team -- attacker simulation
-   Blue Team -- defense monitoring

## Continuous Monitoring

-   SIEM
-   Log analysis
-   Threat intelligence feeds

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

-   Centralized logging
-   Time synchronization
-   Log retention policies

## Digital Forensics

Key Principles: - Chain of custody - Evidence preservation - Repeatable
analysis

## Business Continuity

### RTO

Recovery Time Objective

### RPO

Recovery Point Objective

### Disaster Recovery Sites

-   Cold site
-   Warm site
-   Hot site

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

-   Automate security checks
-   Integrate into CI/CD
-   Continuous monitoring

------------------------------------------------------------------------

# Cryptography Quick Reference

## Encryption Types

  Type           Example
  -------------- ----------------
  Symmetric      AES
  Asymmetric     RSA
  Hash           SHA‑256
  Key Exchange   Diffie‑Hellman

## PKI Components

-   Certificate Authority
-   Registration Authority
-   Certificates
-   Revocation Lists

------------------------------------------------------------------------

# Networking Ports to Remember

  Port   Protocol
  ------ ----------
  21     FTP
  22     SSH
  23     Telnet
  25     SMTP
  53     DNS
  80     HTTP
  110    POP3
  143    IMAP
  443    HTTPS
  3389   RDP

------------------------------------------------------------------------

# Security Operations Quick Reference

## Backup Types

  Type           Description
  -------------- ---------------------------
  Full           Complete backup
  Incremental    Changes since last backup
  Differential   Changes since last full

------------------------------------------------------------------------

# Threat Categories

  Threat Type          Example
  -------------------- -----------------
  Malware              Ransomware
  Social Engineering   Phishing
  Network Attacks      MITM
  Insider Threat       Privilege abuse

------------------------------------------------------------------------

# Security Principles Summary

-   Least Privilege
-   Need to Know
-   Separation of Duties
-   Defense in Depth
-   Zero Trust

------------------------------------------------------------------------

# Quick Exam Tips

-   CISSP tests **management thinking**, not just technical knowledge.
-   Choose the **best risk management answer**, not the most technical
    one.
-   Look for answers involving:
    -   Policy
    -   Process
    -   Risk reduction
    -   Governance

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

*End of Cheat Sheet*
