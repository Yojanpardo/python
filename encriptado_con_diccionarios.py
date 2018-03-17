# -*- coding: utf-8 -*-

from time import time
import os, getpass

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    ' ': '&',
}

def clear(): #Funcion para limpiar las diferentes pantallas
    if os.name == "nt": # Windows
        os.system("cls")
    elif os.name == "posix": # Linux / Mac
        os.system("clear")

def main():
	while True:
			
		option=int(input('''
			C Y P H E R   P R O G R A M  

Puedes escoger una de las siguientes opciones:

1. Cifrar un mensaje
2. Decifrar un mensaje
3. Salir

'''))
		if option==1:
			message=str(getpass.getpass('Ingresa el mensaje que quieres cifrar:\n'))
			cypher_message=cypher(message)
			print('''

Tu mensaje cifrado es:

{}'''.format(cypher_message))
			input('Presiona enter para continuar.')
		elif option==2:
			cypher_message=str(input('Ingresa el mensaje que quieres decifrar:\n'))
			message=decipher(cypher_message)
			print('''

Tu mensaje decifrado es:

{}
'''.format(message))
			input('Presiona enter para continuar.')
		elif option==3:
			print('Hasta la próxima!')
			input('Presiona enter para continuar.')
			exit()
		else:
			print('\nElige una opción de las que están disponibles, Cabrón!\n')
			input('Presiona enter para continuar.')
			return main()

def cypher(message):
	words = message.split(' ')
	cypher_message=[]

	for word in words:
		cypher_word=''
		for letter in word:
			cypher_word += KEYS[letter]

		cypher_message.append(cypher_word)

	clear()

	return ' '.join(cypher_message)

def decipher(cypher_message):
	words = cypher_message.split(' ')
	message = []

	for word in words:
		decipher_word = ''
		for letter in word:
			for key, value in KEYS.items():
				if value == letter:
					decipher_word += key

		message.append(decipher_word)
	
	clear()

	return ' '.join(message)

if __name__ == '__main__':
	main()