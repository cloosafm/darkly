# Finding 10 - email recovery


## Exploitability
Easy. Just need to inspect the page and change a value


## Risk level/type
OWASP top 10 :
- A01:2021 – Broken Access Control
	=> Bypassing access control checks by modifying the URL (parameter tampering or force browsing), internal application state, or the HTML page, or by using an attack tool modifying API requests."
- A07:2021 – Identification and Authentication Failures
	=> "Uses weak or ineffective credential recovery and forgot-password processes, such as "knowledge-based answers," which cannot be made safe."


Common Weakness Enumeration :

CWE-200: Exposure of Sensitive Information to an Unauthorized Actor
https://cwe.mitre.org/data/definitions/200.html

CWE-284: Improper Access Control
https://cwe.mitre.org/data/definitions/284.html

CWE-287: Improper Authentication
https://cwe.mitre.org/data/definitions/287.html


## Detailed description of the exploit
On the login page, we see a link saying "I forgot my password".
It brings us to a page that only shows a "submit" button... but this only give "Sorry wrong answer" response.
If we inspect the "submit" button, we can see immediately above it a hidden input, that contains an email value. Let's change the email to something else, then click submit.
We get to a page saying:
"The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0"


## Remediation
When using input fields on html page, make sure any value attribute is set to something generic. Although you can set the "hidden" attribute to ensure the user does not see the element, a simple inspection tool will reveal the element.


## Additional resources
https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html

https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden
