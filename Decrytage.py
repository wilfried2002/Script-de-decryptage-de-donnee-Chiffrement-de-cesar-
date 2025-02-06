import string

def cesar_encrypt(text, shift):
    """
    Chiffre un texte en utilisant le chiffrement de César.
    
    :param text: Le texte à chiffrer (str).
    :param shift: Le décalage (int).
    :return: Le texte chiffré (str).
    """
    result = []

    for char in text:
        if char.isalpha():  # Traiter uniquement les lettres
            # Déterminer si la lettre est minuscule ou majuscule
            base = ord('a') if char.islower() else ord('A')
            # Appliquer le décalage et boucler sur l'alphabet
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(encrypted_char)
        else:
            # Conserver les caractères non alphabétiques inchangés
            result.append(char)

    return ''.join(result)


def encrypt_file(input_file, shift):
    """
    Chiffre le contenu d'un fichier texte en utilisant le chiffrement de César.
    
    :param input_file: Chemin vers le fichier d'entrée (str).
    :param shift: Le décalage pour le chiffrement (int).
    """
    try:
        # Lire le contenu du fichier d'entrée
        with open(input_file, 'r', encoding='utf-8') as file:
            plaintext = file.read()

        # Chiffrer le texte
        ciphertext = cesar_encrypt(plaintext, shift)

        # Déterminer le chemin du fichier de sortie
        output_file = input_file.replace('.txt', '_encrypted.txt')

        # Écrire le texte chiffré dans le fichier de sortie
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(ciphertext)

        print(f"Le fichier '{input_file}' a été chiffré avec succès et sauvegardé dans '{output_file}'.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{input_file}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


def cesar_decrypt(text, shift):
    """
    Déchiffre un texte en utilisant le chiffrement de César.
    
    :param text: Le texte à déchiffrer (str).
    :param shift: Le décalage (int).
    :return: Le texte déchiffré (str).
    """
    return cesar_encrypt(text, -shift)  # Utiliser la fonction d'encryptage avec un décalage négatif


def decrypt_file(input_file, shift):
    """
    Déchiffre le contenu d'un fichier texte en utilisant le chiffrement de César.
    
    :param input_file: Chemin vers le fichier d'entrée (str).
    :param shift: Le décalage pour le déchiffrement (int).
    """
    try:
        # Lire le contenu du fichier d'entrée
        with open(input_file, 'r', encoding='utf-8') as file:
            ciphertext = file.read()

        # Déchiffrer le texte
        plaintext = cesar_decrypt(ciphertext, shift)

        # Déterminer le chemin du fichier de sortie
        output_file = input_file.replace('_encrypted.txt', '_decrypted.txt')

        # Écrire le texte déchiffré dans le fichier de sortie
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(plaintext)

        print(f"Le fichier '{input_file}' a été déchiffré avec succès et sauvegardé dans '{output_file}'.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{input_file}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


# Exemple d'utilisation
if __name__ == "__main__":
    # Demander à l'utilisateur de saisir le chemin du fichier
    input_filename = input("Veuillez entrer le chemin du fichier à chiffrer : ")
    
    if input_filename:  # Vérifier si un fichier a été spécifié
        shift_value = 3  # Valeur de décalage pour le chiffrement de César
        encrypt_file(input_filename, shift_value)
    else:
        print("Aucun fichier spécifié.")

# Exemple d'utilisation pour le décryptage
if __name__ == "__main__":
    # Demander à l'utilisateur de saisir le chemin du fichier
    input_filename = input("Veuillez entrer le chemin du fichier à déchiffrer : ")
    
    if input_filename:  # Vérifier si un fichier a été spécifié
        shift_value = 3  # Valeur de décalage pour le déchiffrement de César
        decrypt_file(input_filename, shift_value)
    else:
        print("Aucun fichier spécifié.")