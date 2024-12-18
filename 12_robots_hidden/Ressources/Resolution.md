# Finding 12 - robots.txt - .hidden/


## Exploitability
Difficult. Need to know (and check) for a specific page, and have some scripting skills.


## Risk level/type
OWASP top 10 :
- A01:2021 – Broken Access Control
	=> "Violation of the principle of least privilege or deny by default, where access should only be granted for particular capabilities, roles, or users, but is available to anyone."


Common Weakness Enumeration :

CWE-552: Files or Directories Accessible to External Parties
https://cwe.mitre.org/data/definitions/552.html

CWE-548: Exposure of Information Through Directory Listing
https://cwe.mitre.org/data/definitions/548.html


## Detailed description of the exploit
Previously, we found the robots.txt file:
192.168.56.101/robots.txt

This showed 2 directories:
- /whatever/
- /.hidden/

If we go to:
192.168.56.101/.hidden/
We can see 26 top-level directories and one README. Each directory seems to have 26 sub-level subdirs... let's not waste any more time.
We write a scraping script that will go through all these directories recursively, in order to find the flag.

The 1st part is to go through all directories, and store the URLs of the files in a set.
Then we go through all the files and check the content - a lot of it is similar.
We want to compare each file content to what was previously found, and print only what is new.

After a while - and some more-or-less funny messages - we find:
```Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
```

## Remediation

The file robots.txt should/must not contain any sensitive data. Its purpose is to tell any web robot which section of the site it may visit.
Although the file may contain the ```Disallow``` directive, this is not binding for scraper/crawlers which may chose to disregard the directive. Keep in mind that the robots.txt file is a public file !
Also, authorization and access control must be put in place ti ensure the identity of whomever tries to access any files.


## Additional resources
https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
