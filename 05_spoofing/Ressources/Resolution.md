spoof id by using the nsa as referer (https://www.nsa.org/) and ft_bornToSec as User-agent

# Finding 05 - Spoofing

## Exploitability
Moderate. Requires inspection of the source code and some knowledge of HTTP headers (specifically the User-Agent header). However, tools like browser devtools or extensions make it relatively straightforward to exploit.

## Risk level/type
OWASP top 10 :
- A04:2021 - Insecure Design
- A01:2021 - Broken Access Control
    => "CORS misconfiguration allows API access from unauthorized/untrusted origins."

## Detailed description of the exploit
1. **Inspect the source code of copyright page:**
    - On the copyright page, we opened the developer tools and inspected the page’s HTML.
    - Instructions about spoofing are found.
2. **Understand the requirement:**
    - Based on the comment, access to a restricted area was granted only when the request met these two conditions:
        - **Referer** header to be set to https://www.nsa.org/.
        - **User-Agent** header was set to ft_bornToSec.
3. **Craft the request:**
    - Using tools such as curl or a browser extension (like ModHeader) we modified the necessary headers.

## Impact
- **Information disclosure:**
    - Hidden comments: Comments in the source code provided sensitive information about how to bypass access restrictions. If such comments are leaked in production, attackers can exploit them to gain unauthorized access.
- **Misconfigured access controls:**
    - The reliance on easily spoofed headers (like User-Agent and Referer) for authentication is inherently insecure.9
    - Attackers can craft requests that simulate any browser or referer, rendering these checks ineffective.

## Remediation
1. **Remove sensitive comments:**
    - Avoid including any sensitive or environment-specific information (e.g., API keys, credentials, or internal instructions) in HTML comments.
    - Use logging systems to track internal messages rather than exposing them in production.
2. **Strengthen access controls:**
    - Avoid header-based authentication: Do not rely on Referer or User-Agent headers for authentication or access control. These headers can be easily spoofed.
    - Use proper authentication mechanisms such as tokens, session management, or IP whitelisting for sensitive areas.

## Additional resources

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent


CWE-290: Authentication Bypass by Spoofing
https://cwe.mitre.org/data/definitions/290.html

