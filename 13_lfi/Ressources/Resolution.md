# Finding 13 - local file inclusion & path traversal

## Exploitability
Moderately easy. Need specific knowledge about the vulnerability.

## Risk level/type
OWASP top 10 :
A03:2021 – Injection
	=> "User-supplied data is not validated, filtered, or sanitized by the application."

Common Weakness Enumeration :

CWE-98: Improper Control of Filename for Include/Require Statement in PHP Program ('PHP Remote File Inclusion')
https://cwe.mitre.org/data/definitions/98.html

CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
https://cwe.mitre.org/data/definitions/22.html

CWE-23: Relative Path Traversal
https://cwe.mitre.org/data/definitions/23.html

CWE-36: Absolute Path Traversal
https://cwe.mitre.org/data/definitions/36.html

## Detailed description of the exploit
The local file inclusion consists of injecting code on the URL, to obtain a remote location from which one can retrieve info or code to execute.

Specifically, path traversal is about trying to access known possible credential paths that are alike in the OS and the site structure.

One such known vulnerability is to add ```/?page=../../../../../../../../etc/passwd``` after the domain name (here, IP address).
So, let's try that:
http://192.168.56.101/?page=../../../../../../../../etc/passwd

We get to a page that says:
"Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0"

Note: in our case, we need to use at least 7 "../" to get the flag.

## Remediation
You want to validate user input on the serverside with an allowlist. Ideally, use chrooted jail and strict access policies in order to restrict where files can be obtained.

## Additional resources
https://medium.com/@Aptive/local-file-inclusion-lfi-web-application-penetration-testing-cc9dc8dd3601
