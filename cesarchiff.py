def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    for char in message:
        if char.isalpha():
            lettre_chiffree = chr((ord(char) - ord('a' if char.islower() else 'A') + decalage) % 26 + ord('a' if char.islower() else 'A'))
            message_chiffre += lettre_chiffree
        else:
            message_chiffre += char
    return message_chiffre

def dechiffrement_cesar(message, decalage):
    message_chiffre = ""
    for char in message:
        if char.isalpha():
            lettre_chiffree = chr((ord(char) - ord('a' if char.islower() else 'A') - decalage) % 26 + ord('a' if char.islower() else 'A'))
            message_chiffre += lettre_chiffree
        else:
            message_chiffre += char
    return message_chiffre