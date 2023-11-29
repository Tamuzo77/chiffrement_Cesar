def generate_key(message, mot_cle):
    mot_cle = mot_cle.upper()
    cle_etendue = ""

    j = 0
    for i in range(len(message)):
        if message[i].isalpha():
            cle_etendue += mot_cle[j % len(mot_cle)]
            j += 1
        else:
            cle_etendue += message[i]

    return cle_etendue

def chiffrement_vigenere(message, key):
    message_chiff = []

    for i in range(len(message)):
        if message[i].isalpha():
            letter = message[i]
            lettre_chiffre = ((ord(message[i].upper()) + ord(key[i])) % 26) + ord('A')
            message_chiff.append(chr(lettre_chiffre) if letter.isupper() else chr(lettre_chiffre).lower())
        else:
            message_chiff.append(message[i])

    return "".join(message_chiff)

def dechiffrement_vigenere(message, key):
    original_text = []
    for i in range(len(message)):
        if message[i].isalpha():
            letter = message[i]
            lettre_chiffre = ((ord(message[i].upper()) - ord(key[i])) % 26) + ord('A')
            original_text.append(chr(lettre_chiffre) if letter.isupper() else chr(lettre_chiffre).lower())
        else:
            original_text.append(message[i])

    return "".join(original_text)


