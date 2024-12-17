# Finding 08 - robots.txt - admin page

## Exploitability
Moderately difficult. Need to know (and check) for specific pages.

## Risk level/type
OWASP top 10
- A02:2021 – Cryptographic Failures		using md5 encryption
- A05:2021 – Security Misconfiguration
- A07:2021 – Identification and Authentication Failures icon

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

Also, md5 is now deprecated in favor of sha2 algorithms (sha256, sha512) as well as sha3 algorithms.

## Additional resources
https://en.wikipedia.org/wiki/Robots.txt

md5 deprecation notice :
https://www.security-database.com/detail.php?alert=VU836068