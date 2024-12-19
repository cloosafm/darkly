got to survey page
inspect any grade
change any value
Get to flag page :

 The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa


 issue is : insecure input validation

 # Finding 06 - survey page : insecure input validation

## Exploitability
 Easy. The vulnerability is due to the lack of server-side validation, which allows an attacker to modify the input values directly in the browser.


## Risk level/type

OWASP top 10 :
- A01:2021 - Broken Access Control

CWE-602: Client-Side Enforcement of Server-Side Security
=> Relying on client-side validation alone to enforce security policies leads to exploitation.
https://cwe.mitre.org/data/definitions/602.html

CWE-20: Improper Input Validation
=> Failure to validate data before processing it allows attackers to submit unexpected or malicious values.
https://cwe.mitre.org/data/definitions/20.html

## Detailed description of the exploit
- **Analyze the page:**
    - The Survey page allowed users to vote on items, with an input field for setting the vote's weight. The visible range was between 1 and 10.
- **Modify the input field:**
    - By inspecting the element using browser developer tools, we changed the input field’s value to a much larger number (e.g., 99999999).
- **Submit the form:**
    - When the form was submitted, the backend did not validate the value. The extremely high weight was accepted, skewing the vote tally and revealing the flag.

## Impact
- **Data manipulation:**
    - Attackers can bypass client-side constraints to submit any value, including values outside the intended range (negative, zero, or extremely large).
    - This leads to data corruption, inaccurate results, or unfair outcomes (e.g., in surveys, polls, or leaderboard systems).

## Remediation
1. **Server-side validation:**
    - All input from the client must be validated and sanitized on the server before processing
2. **Implement data integrity checks:**
    - On the server, enforce limits on critical fields (e.g., max weight for votes).
    - Log unusual input values for monitoring and investigation.

## Additional resources

Preventing Input Tampering:
https://owasp.org/www-community/attacks/Input_Manipulation