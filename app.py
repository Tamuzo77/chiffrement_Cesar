import functions
import pyfiglet

command = ''
welcome =  pyfiglet.print_figlet(text="B y  T a m u z o", colors="GREEN")
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

        key = functions.generateKey(message)
        message_chiffre = functions.chiffrement_vigenere(message, key)
        print(f'\nMessage Chiffre: {message_chiffre}')
        print(f'Clé de chiffrement: {key}')

    elif command == 'decrypt':
        if not message:
            message = input("Entrer le message: ")
        else:
            message = message[0]

        key = input("Entrer la clé: ")
        message_chiffre = functions.dechiffrement_vigenere(message, key)
        print(f'\nMessage Dechiffre: {message_chiffre}')
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
