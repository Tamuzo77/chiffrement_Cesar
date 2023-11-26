## Exercice du chiffrement de César par [MENGA Tamuzo Jonathan]()

Le programme se lance dans le fichier [app.py]().

Les fonctions de chiffrement et de déchiffrement sont écrits dans le fichier [cesarchiff.py]()

Au lancement du programme vous avez la possibilité d'entrer la commande "help"

```agsl
> help

crypt [message] - to crypt a meaage
decrypt [message] - to decrypt a message
help            - help
quit            - to end the process
        
> 

```

> Pour chiffrer un message vous pouvez utiliser la commande "crypt" suivi du message à crypter

Exemple: 
```agsl
> crypt Le lendemain aura ses propres inquietudes

Entrer le nombre de decalage: 3
Message Chiffre: Oh ohqghpdlq dxud vhv sursuhv lqtxlhwxghv

> 
```

ou 

```agsl
> crypt
Entrer le message: Le lendemain aura ses propres inquietudes

Entrer le nombre de decalage: 10
Message Chiffre: Vo voxnowksx kebk coc zbyzboc sxaesodenoc

> 
```

> Pour déchiffrer un message vous pouvez utiliser la commande "decrypt" suivi du message à décrypter

Exemple:

```agsl
> decrypt Vo voxnowksx kebk coc zbyzboc sxaesodenoc

Entrer le nombre de decalage: 10
Message Dechiffre: Le lendemain aura ses propres inquietudes

> 
```
ou

```agsl
> decrypt

Entrer le message: Vo voxnowksx kebk coc zbyzboc sxaesodenoc
Entrer le nombre de decalage: 10

Message Dechiffre: Le lendemain aura ses propres inquietudes

> 
```
