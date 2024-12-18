# Finding 11 - redirection

## Exploitability
Easy. Only need to inspect page and add modification.

## Risk level/type
OWASP top 10 :
- A03:2021 – Injection
	=> "User-supplied data is not validated, filtered, or sanitized by the application."

Common Weakness Enumeration:
https://cwe.mitre.org/data/definitions/601.html

## Detailed description of the exploit
Inspect any of the redirection icons.
Change its value (facebook/twitter/instagram) to something else (does not have to exist)
Without reloading, just click on the icon.
We get to a page that shows:
"Good Job Here is the flag : b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3"

## Remediation
The remedy is quite simple : any redirection should be validated on the server side, using an allowlist rather than a denylist.
It may also be helpful for users to display a page before redirection, in order to notify them that they will be redirected and where they will be redirected.

## Additional resources
https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html


https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html

