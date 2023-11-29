import affinefunction

command = ''
print("Taper 'help' pour voir les commandes à utiliser")
while True:
    user_input = input('> ')
    command, *message = user_input.split(' ',1);
    command = command.lower()
    if command == 'crypt':

        if not message:
            message = input("Entrer le message: ")
        else:
            message = message[0]

        a_valide = False
        while not a_valide:
            a = int(input("Entrez la valeur du coefficient A (doit être premier avec 26) : "))
            a_valide = affinefunction.est_valide(a, 26)

        b = int(input("Entrez la valeur de b : "))

        message_chiffre = affinefunction.chiffrement_affine(message, a,b)
        #loader.simulate_download_loader(3)
        print(f'\nMessage Chiffre: {message_chiffre}')

    elif command == 'decrypt':
        if not message:
            message = input("Entrer le message: ")
        else:
            message = message[0]

        a_valide = False
        while not a_valide:
            a = int(input("Entrez la valeur du coefficient A (doit être premier avec 26) : "))
            a_valide = affinefunction.est_valide(a, 26)

        b = int(input("Entrez la valeur de b : "))

        message_dechiffre = affinefunction.dechiffrement_affine(message, a,b)
        #loader.simulate_download_loader(3)
        print(f'\nMessage Chiffre: {message_dechiffre}')
    elif command == 'help':
        print('''
crypt [message] - Crypter un message
decrypt [message] - Decrypter un message
help            - aide
quit            - Quitter l'application 
        ''')
    elif command == 'quit':
        break
    else:
        print(f'No command {command} found')
