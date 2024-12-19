# Finding 04 - Persistent XSS in Feedback Form


## Exploitability
Easy to find, moderate to understand. Input a malicious script in the feedback form and submit. The script is executed and remains on the page, affecting all users who access the page.


## Risk level/type
OWASP top 10 :
- A03:2021 - Injection
    => "User-supplied data is not validated, filtered, or sanitized by the application."
    => "Dynamic queries or non-parameterized calls without context-aware escaping are used directly in the interpreter."

Common Weakness Enumeration :

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
https://cwe.mitre.org/data/definitions/79.html

CWE-116: Improper Encoding or Escaping of Output
https://cwe.mitre.org/data/definitions/116.html


## Detailed description of the exploit
Steps followed:
1. **Locate the vulnerable input field:**
On the feedback page, there is a text input field where users can leave comments or feedback.
2. **Inject malicious script:**
To test this, you can just try writing ```<script>``` in the freee form.


## Impact ##
(Same as the other XSS injection)
- **Persistent XSS:** The payload remains stored on the server, meaning any user who accesses the feedback page will trigger the malicious script.
- **Scope of attack:**
    - **Stealing session cookies:** Attackers could use document.cookie to steal user sessions.
    - **Redirects to malicious sites:** Users could be redirected to phishing sites.
    - **Manipulating the DOM:** Malicious scripts could modify the page’s content or behavior.
- **Escalation potential:** If an administrator views the feedback page while logged in, attackers may gain higher-privilege access.


## Remediation
1. **Input sanitization:**
    - Sanitize and escape all user input, especially in contexts where HTML, JavaScript, or other potentially dangerous elements may be interpreted.
2. **Output encoding:**
    - Use context-appropriate escaping:
        - HTML escaping for content inside tags.
        - JavaScript escaping for dynamically-injected JavaScript.
        - URL encoding for query parameters.
3. **Content Security Policy (CSP):**
    - Implement a strong CSP to limit the execution of untrusted scripts. For example: ```Content-Security-Policy: script-src 'self'; object-src 'none';```


## Additional resources
https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html

https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

Testing for XSS Vulnerabilities:
https://owasp.org/www-community/attacks/xss/