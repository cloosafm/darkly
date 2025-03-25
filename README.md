# darkly

This is a security assessment report on the project "darkly", structured as suggested by the OWASP testing guide. See the foollowing :
https://owasp.org/www-project-web-security-testing-guide/v42/5-Reporting/README

## Table of content

### The Team
### Scope
### Limitations
### Timeline
### Disclaimer
### Executive summary
### Findings
### Appendices


## The team
ablevin & acloos

## Scope
The scope of the project is limited to the use of the provided iso, which will launch a website on a given IP. There are 14 security breaches/vulnerabilities to be found, in a CTF format.

## Disclaimer
The project states that we are to find 14 security breaches/vulnerabilities. In this contexte, we did not attempt to find additional issues.

## Executive summary
Objective : as students, get hands-on experience of web security applied specifically to websites.
As a consequence, be able to understand how to secure these breaches proactively, and apply safety patches if/when possible.

## Findings

### Findings summary
The exact content of each Finding will be in the Resolution.md of their directory

ID	Title
01	login credentials (2 methods : bruteforce and SQL injection)
20	SQL injection on image searching input field
03	XSS on media URL
04	XSS on feedback page
05	spoofing
06	survey hack
07	SQL injection on member searching input field
08	robots.txt - admin page
09	cookie
10	email recovery
11	redirection
12	robots.txt - .hidden/
13	local file inclusion & path traversal
14	file upload

For each finding, wegive the following information:
- reference ID
- vulnerability title
- likelihood/exploitability of the issue, with a difficulty assessment and quick description of the difficulty.
- risk level/type : we reference where the vulnerability stands in the owasp top 10 and in CWE
- description of vulnerability and how to exploit it
- how to remediate the vulnerability, possible improvements, what security practices are missing
- additional resources to help understand the vulnerability


## Appendices

### Resources
Specific resources can be found in each Finding's Reslution.md file.
Below can be found some more general resources:

https://owasp.org/www-project-web-security-testing-guide/stable/
https://www.indusface.com/blog/notorious-hacks-history/

#### XSS (Cross-Site Scripting)
https://www.clovinsec.com/post/understanding-xss-vulnerability-types-impact-and-countermeasures
https://portswigger.net/web-security/cross-site-scripting
https://www.softwaretestinghelp.com/cross-site-scripting-xss-attack-test/
https://en.wikipedia.org/wiki/Samy_%28computer_worm%29
https://web.archive.org/web/20160305044015/http://samy.pl/popular/tech.html

#### SQL injections
https://www.clovinsec.com/post/uncovering-the-threat-of-sql-injection-understanding-the-different-types-exploits-and-effective-d
https://portswigger.net/web-security/sql-injection#what-is-sql-injection-sqli
https://www.sqlinjection.net/table-names/
https://en.wikipedia.org/wiki/SQL_injection
https://en.wikipedia.org/wiki/2015_TalkTalk_data_breach
https://www.vps.net/blog/historic-hacks-albert-gonzalez/

#### redirection / open redirect vulnerabilities
https://bugbase.ai/blog/A-Guide-to-Open-Redirection
https://tcm-sec.com/understanding-and-finding-open-redirects/
https://en.wikipedia.org/wiki/Phishing
https://brightsec.com/blog/open-redirect-vulnerabilities/

#### bruteforce
https://www.malwarebytes.com/cybersecurity/basics/brute-force-attack
https://en.wikipedia.org/wiki/Brute-force_attack

#### robots.txt
https://en.wikipedia.org/wiki/Robots.txt
https://www.baeldung.com/cs/robots-txt-risk-threat
https://portswigger.net/kb/issues/00600600_robots-txt-file


### Severity and risk rating explanations
In terms of easiness of exploit, we decided on 4 levels : Easy, Moderately easy, Moderately difficult, Difficult
These ratings are only to be evaluated in relation to the project itself. This means that exploits rated as "Difficult" are not necessarily extremely difficult to find and exploit, but they are the most difficult in this project.

### Tools and relevant outputs
Each Finding's Resolution.md lists relevant outputs as well as the tools that were used.

## 42 score
This project was fully completed at 125% (bonus : in-depth understanding of specific risks, such as SQL injection, XSS...)
