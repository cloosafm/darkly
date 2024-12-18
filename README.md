# darkly

This is a security assessment report on the project "darkly", structured as suggested by the OWASP testing guide. See the foollowing :
https://owasp.org/www-project-web-security-testing-guide/v42/5-Reporting/README

## Table of content

The Team
Scope
Limitations
Timeline
Disclaimer
Executive summary
Findings
Appendices


## The team
ablevin & acloos

## Scope
The scope of the project is limited to the use of the provided iso, which will launch a website on a given IP. There are 14 security breaches to be found, in a CTF format.

## Limitations

## Timeline
This project is supposed to be completed within 98h.

## Disclaimer

## Executive summary
Objective : as students, get hands-on experience of web security applied specifically to websites.
As a consequence, be able to understand how to secure these breaches proactively, and apply safety patches if/when possible.

## Findings

### Findings summary
The exact content of each finding will be in the Resolution.md of their directory

ID	Title
01	login credentials (bruteforce and SQL injection)
20	SQL injection on image searching input field
03	
04	
05	
06	
07	SQL injection on member searching input field
08	robots.txt - admin page
09	cookie
10	email recovery
11	redirection
12	robots.txt - .hidden/
13	local file inclusion & path traversal
14	

For each finding, wegive the following information:

- reference ID

- vulnerability title

- likelihood/exploitability of the issue, with a difficulty assessment and quick description of the difficulty.
	We decided on 4 levels : Easy, Moderately easy, Moderately difficult, Difficult

- risk level/type : we reference where the vulnerability stands in the owasp top 10 and in CWE

- description of vulnerability and how to exploit it

- how to remediate the vulnerability, possible improvements, what security practices are missing

- additional resources to help understand the vulnerability


## Appendices

### Resources

### Methodology

### Severity and risk rating explanations

### Tools and relevant outputs

### Checklist of all conducted tests