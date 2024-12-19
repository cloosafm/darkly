# Finding 01 - login credentials - bruteforce

## Exploitability

Easy. Only 2 steps required: run a brute force script using a commonly available password list, then use the discovered credentials to log in.

## Risk level/type

OWASP top 10 :
- A07:2021 - Identification and Authentification Failures
    => "Permits brute force or other automated attacks."


Common Weakness Enumeration :

CWE-521: Weak Password Requirements
https://cwe.mitre.org/data/definitions/521.html

CWE-307: Improper Restriction of Excessive Authentication Attempts
https://cwe.mitre.org/data/definitions/307.html

## Detailed description of the exploit

Steps followed:
1. **Running a brute force script**
We wrote a simple Python script, ```bruteForce.py```, that takes a dictionary file containing over 12,000+ commonly used passwords.
2. **Result of the brute force:**
After running the script, the password "shadow" was successfully guessed for the user "admin"
3. **Logging in with discovered credentials:**
We used the discovered credentials to login wich reveal the flag9

## Impact
Complete access to another user account and/or admin account.

## Remediation

1. **Rate limiting and account lockout mechanisms:**
    - Enforce a rate limit on login attempts (e.g., allow only 3-5 attempts per minute).
    - Implement account lockout mechanisms after multiple failed login attempts.

2. **Enforce strong password policies:**
    - Mandate the use of strong, unique passwords for all accounts. For example:
        - Minimum 12 characters
        - Inclusion of uppercase, lowercase, numbers and/or special characters
    - Check passwords against a list of commonly used or breached passwords.

3. **Use multi-factor authentication (MFA):**
    - Require a second factor, such as a one-time password (OTP) or hardware token, to log in.

## Additional resources

Rate Limiting:
https://owasp.org/www-community/controls/Blocking_Brute_Force_Attacks
