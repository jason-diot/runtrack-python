import hashlib
import json

def check_password(password):
    """Vérifie si le mot de passe respecte les exigences de sécurité."""
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in '!@#$%^&*' for c in password):
        return False
    return True

def hash_password(password):
    """Retourne le hachage SHA-256 du mot de passe."""
    return hashlib.sha256(password.encode()).hexdigest()

def add_password(passwords):
    """Demande à l'utilisateur de saisir un nouveau mot de passe et l'ajoute au dictionnaire."""
    password = input("Entrez votre nouveau mot de passe: ")
    if check_password(password):
        hashed_password = hash_password(password)
        if hashed_password in passwords:
            print("Le mot de passe existe déjà")
        else:
            passwords[hashed_password] = ""
            print("Mot de passe ajouté avec succès!")
    else:
        print("Le mot de passe ne respecte pas les exigences de sécurité.")

def list_passwords(passwords):
    """Affiche la liste des mots de passe enregistrés dans le dictionnaire."""
    print("Liste des mots de passe enregistrés:")
    for hashed_password, password in passwords.items():
        print(hashed_password)

def save_passwords(passwords, filename):
    """Enregistre le dictionnaire des mots de passe dans un fichier JSON."""
    with open(filename, 'w') as f:
        json.dump(passwords, f, indent=2)

def load_passwords(filename):
    """Charge le dictionnaire des mots de passe à partir d'un fichier JSON."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def main():
    """Fonction principale du programme."""
    passwords = load_passwords("passwords.json")

    while True:
        print("Que souhaitez-vous faire?")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher tous les mots de passe")
        print("3. Quitter")

        choice = input("Entrez le numéro de votre choix: ")
        if choice == '1':
            add_password(passwords)
            save_passwords(passwords, 'passwords.json')
        elif choice == '2':
            list_passwords(passwords)
        elif choice == '3':
            break
        else:
            print("Choix invalide.")

if __name__ == '__main__':
    main()

