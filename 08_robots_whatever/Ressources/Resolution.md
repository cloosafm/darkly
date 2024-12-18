# Finding 08 - robots.txt - admin page


## Exploitability
Moderately difficult. Need to know (and check) for specific pages.


## Risk level/type
OWASP top 10 :
- A01:2021 – Broken Access Control
	=> Bypassing access control checks by modifying the URL (parameter tampering or force browsing), internal application state, or the HTML page, or by using an attack tool modifying API requests."
- A02:2021 – Cryptographic Failures
	=>" Are deprecated hash functions such as MD5 or SHA1 in use [...] ?"
- A07:2021 – Identification and Authentication Failures
	=> "Uses plain text, encrypted, or weakly hashed passwords data stores."

Common Weakness Enumeration :

CWE-327: Use of a Broken or Risky Cryptographic Algorithm
https://cwe.mitre.org/data/definitions/327.html

CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
https://cwe.mitre.org/data/definitions/200.html

CWE-287: Improper Authentication
https://cwe.mitre.org/data/definitions/287.html


## Detailed description of the exploit
Let's see if there is an admin page:
192.168.56.101/admin

Yes, there is one. Just in case, let's try the password discovered on Finding #01, but it won't work.

Let's check the robots.txt file:
192.168.56.101/robots.txt

This shows 2 directories:
- /whatever/
- /.hidden/

If we go to:
192.168.56.101/whatever
we can see there is a file called ```htpasswd```
Let's download the file and open it, it contains:
```root:437394baff5aa33daa618be47b75cb49```
Now the value for th key "root" would not be md5 encrypted, now, would it?
Let's use our web tool again:
https://www.md5online.org/md5-decrypt.html
It gives us:
qwerty123@

So now we can try logging into the admin page, and get the following:
The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff


## Remediation
The file robots.txt should/must not contain any sensitive data. Its purpose is to tell any web robot which section of the site it may visit.
Although the file may contain the ```Disallow``` directive, this is not binding for scraper/crawlers which may chose to disregard the directive. Keep in mind that the robots.txt file is a public file !
Data that should not be accessed remotely just should not be accessible via internet - or you want to implement strict access rules for that data.
Obviously, authorization and access control must be put in place to ensure the identity of whomever tries to access any files.

Also, md5 is now deprecated in favor of sha2 algorithms (sha256, sha512) as well as sha3 algorithms.


## Additional resources
https://en.wikipedia.org/wiki/Robots.txt
https://www.baeldung.com/cs/robots-txt-risk-threat
https://portswigger.net/kb/issues/00600600_robots-txt-file

md5 deprecation notice :
https://www.security-database.com/detail.php?alert=VU836068