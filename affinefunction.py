def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def est_valide(a, m):
    return pgcd(a, m) == 1

def chiffrement_affine(texte, a, b):
    texte_chiffre = ""
    for char in texte:
        if char.isalpha():
            if char.isupper():
                texte_chiffre += chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
            elif char.islower():
                texte_chiffre += chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
        else:
            texte_chiffre += char
    return texte_chiffre

def dechiffrement_affine(texte_chiffre, a, b):
    a_inv = mod_inverse(a, 26)
    texte_dechiffre = ""
    for char in texte_chiffre:
        if char.isalpha():
            if char.isupper():
                texte_dechiffre += chr((a_inv * (ord(char) - ord('A') - b)) % 26 + ord('A'))
            elif char.islower():
                texte_dechiffre += chr((a_inv * (ord(char) - ord('a') - b)) % 26 + ord('a'))
        else:
            texte_dechiffre += char
    return texte_dechiffre

