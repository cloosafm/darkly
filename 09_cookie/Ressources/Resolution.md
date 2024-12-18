# Finding 09 - cookie

## Exploitability
Moderately easy. Inspect cookie and note its name, see that the value is hashed, figure out the hash algo then replace value.

## Risk level/type
OWASP top 10 :
- A01:2021 – Broken Access Control
	=> "Metadata manipulation, such as replaying or tampering with [...] a cookie [...] to elevate privileges or abusing JWT invalidation."
- A02:2021 – Cryptographic Failures
	=>" Are deprecated hash functions such as MD5 or SHA1 in use [...] ?"


Common Weakness Enumeration 

CWE-327: Use of a Broken or Risky Cryptographic Algorithm
https://cwe.mitre.org/data/definitions/327.html

CWE-922: Insecure Storage of Sensitive Information
https://cwe.mitre.org/data/definitions/922.html


## Detailed description of the exploit
Let's inspect the cookie. It has quite a remarkable name : "I_am_admin"
The value seems to be hashed, it is:
68934a3e9455fa72420237eb05902327
As we have encountered md5 before, let's try it out with our usual web tool and see if we're lucky :
 
https://www.md5online.org/md5-decrypt.html
It gives us:
false

We can try setting it to "true", but won't get any result.
Let's try encrypting in md5, using
https://www.md5online.org/md5-encrypt.html
It yields:
b326b5062b2f0e69046810717534cb09

Let's replace the cookie value with it, then reload.
We get the pop-up message:
"Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3"

## Remediation

At the bare minimum, obfuscate anything that may give out sensitive info. Also, you want to check the user identity with credentials and not store a state (such as being the admin) in a cookie.
Cookies can also have the ```Secure``` attribute, to order the web browsers to use only https connection.

Also, md5 is now deprecated in favor of sha2 algorithms (sha256, sha512) as well as sha3 algorithms.

## Additional resources
https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html

md5 deprecation notice :
https://www.security-database.com/detail.php?alert=VU836068