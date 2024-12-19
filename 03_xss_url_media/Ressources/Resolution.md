# Finding 03 - XSS via URL Parameter


## Exploitability
Moderate/Hard. The vulnerability allows injecting arbitrary code through a URL parameter, which is then rendered as part of the page without validation or sanitization.


## Risk level/type
OWASP top 10 :
- A03:2021 - Injection
    => "Hostile data is directly used or concatenated. The SQL or command contains the structure and malicious data in dynamic queries, commands, or stored procedures." 

Common Weakness Enumeration:

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
https://cwe.mitre.org/data/definitions/79.html

CWE-116: Improper Encoding or Escaping of Output
https://cwe.mitre.org/data/definitions/116.html

CWE-20: Improper Input Validation
https://cwe.mitre.org/data/definitions/20.html


## Detailed description of the exploit
1. **Identify the vulnerable parameter:**
While scrolling the homepage, we notice that one image is clickable, so let's try that.
The target page dynamically generates an ```<object>``` element, using a URL parameter as the ```src``` attribute.
2. **Inject a malicious payload:**
By crafting a payload in Base64 format, we were able to inject and execute arbitrary JavaScript. The payload used was: ```src=data:text/html;base64,PHNjcmlwdD5hbGVydCg0Mik8L3NjcmlwdD4=```. Decoded payload: ```<script>alert(42)</script>```


## Impact ##
- **Persistent XSS:** The payload remains stored on the server, meaning any user who accesses the feedback page will trigger the malicious script.
- **Scope of attack:**
    - **Stealing session cookies:** Attackers could use document.cookie to steal user sessions.
    - **Redirects to malicious sites:** Users could be redirected to phishing sites.
    - **Manipulating the DOM:** Malicious scripts could modify the page’s content or behavior.
- **Escalation potential:** If an administrator views the feedback page while logged in, attackers may gain higher-privilege access.


## Remediation
- **Input validation:**
    Validate and sanitize all user inputs, including URL parameters. For example:
    - Allow only whitelisted schemes (https://, http://, etc.).
    - Reject data: URLs unless explicitly required.
- **Output encoding:**
    - Escape all dynamic values used within HTML attributes, ensuring that special characters like < and > are encoded
- **Content Security Policy (CSP):**
    - Implement a strong CSP to limit the execution of untrusted scripts. For example: ```Content-Security-Policy: script-src 'self'; object-src 'none';```
- **Disable dangerous elements:**
    - If <object> elements are not required, remove or disable them. Use safer alternatives like <iframe> with restricted attributes (e.g., sandbox).


## Additional resources
Encoding and Escaping Data:
https://cheatsheetseries.owasp.org/cheatsheets/Output_Encoding_Cheat_Sheet.html

Content Security Policy Guide:
https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP