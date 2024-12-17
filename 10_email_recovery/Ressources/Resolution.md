# Finding 10 - email recovery

## Exploitability
Very easy. Just need to inspect the page and change a value

## Risk level/type
OWASP top 10
- A04:2021 – Insecure Design
- A05:2021 – Security Misconfiguration

## Detailed description of the exploit
On the login page, we see a link saying "I forgot my password".
It brings us to a page that only shows a "submit" button... but this only give "Sorry wrong answer" response.
If we inspect the "submit" button, we can see immediately above it a hidden input, that contains an email value. Let's change the email to something else, then click submit.
We get to a page saying:
"The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0"

## Remediation
????

## Additional resources
????????