# Vernam Cipher Tool

### [By Tamuzo]() 


Bienvenue dans l'outil de chiffrement de Vernam développé par Tamuzo. Cet outil simple et puissant vous permet de crypter et décrypter des messages en utilisant le chiffrement de Vernam, également connu sous le nom de chiffrement à clé unique ou à masque jetable.
## Présentation

Le chiffrement de Vernam garantit un niveau de sécurité élevé en utilisant une clé unique de la même longueur que le message. Chaque caractère du message est combiné avec son homologue dans la clé à l'aide d'une opération XOR, assurant ainsi une confidentialité robuste.
Utilisation

    Assurez-vous d'avoir Python installé sur votre système.
    Clonez ce dépôt ou téléchargez le fichier app.py et functions.py.
    Exécutez le script avec la commande suivante :

```bash
python app.py
```
    Suivez les instructions interactives pour crypter, décrypter, obtenir de l'aide ou quitter l'application.

Commandes Disponibles

    crypt [message] - Crypte le message en utilisant une clé générée automatiquement.
    decrypt [message] - Décrypte le message chiffré en utilisant la clé fournie.
    help - Affiche les commandes disponibles.
    quit - Quitte l'application.

Fonctionnalités

    Génération automatique d'une clé sécurisée pour chaque cryptage.
    Affichage de la clé de chiffrement pour référence lors du déchiffrement.

Exemple d'Utilisation

```agsl
> crypt La Fin Justifie Les Moyens

Message Chiffre: Vg Pkl Lfploecp Qdx Izijbx
Cle de chiffrement: KG KCY CLXSGZUL FZF WLKFOF
>
```
ou

```agsl
> decrypt Vg Pkl Lfploecp Qdx Izijbx
Entrer la cle: KG KCY CLXSGZUL FZF WLKFOF

Message Dechiffre: La Fin Justifie Les Moyens
> 
```

Avertissement

    Sécurité Importante : Assurez-vous de conserver la clé de chiffrement générée lors du cryptage pour déchiffrer ultérieurement.
    Explorez différentes combinaisons de clés et de messages pour mieux comprendre le chiffrement de Vernam.

Merci d'utiliser l'outil de chiffrement de Vernam by Tamuzo. Sécurisez vos messages avec style! 🌐🔐