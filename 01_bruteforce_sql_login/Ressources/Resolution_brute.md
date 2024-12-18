# Finding 01 - login credentials - bruteforce


## Exploitability
???


## Risk level/type
OWASP top 10 :
- A02:2021 – Cryptographic Failures
	=>" Are deprecated hash functions such as MD5 or SHA1 in use [...] ?"
- A07:2021 – Identification and Authentication Failures
	=> "Permits brute force or other automated attacks."
???


Common Weakness Enumeration :

CWE-327: Use of a Broken or Risky Cryptographic Algorithm
https://cwe.mitre.org/data/definitions/327.html

CWE-307: Improper Restriction of Excessive Authentication Attempts
https://cwe.mitre.org/data/definitions/307.html

## Detailed description of the exploit
?????


## Remediation
The md5 hashing algorithm is now deprecated in favor of sha2 algorithms (sha256, sha512) as well as sha3 algorithms.

?????????????????


## Additional resources
md5 deprecation notice :
https://www.security-database.com/detail.php?alert=VU836068

????????????????????