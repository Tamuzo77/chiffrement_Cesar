import cesarchiff

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

        decalage = int(input('Entrer le nombre de decalage: '))
        message_chiffre = cesarchiff.chiffrement_cesar(message,decalage)
        print(f'Message Chiffre: {message_chiffre}')

    elif command == 'decrypt':
        if not message:
            message = input("Entrer le message: ")
        else:
            message = message[0]

        decalage = int(input('Entrer le nombre de decalage: '))
        message_chiffre = cesarchiff.dechiffrement_cesar(message,decalage)
        print(f'Message Dechiffre: {message_chiffre}')
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
