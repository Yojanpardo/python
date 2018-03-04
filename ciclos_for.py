# -*- coding: utf-8 -*-

def main():
	option = int(raw_input("ingresa la opcción que deseas ejecutar.\n1. deletrear una palabra.\n2. decir mierda x cantidad de veces\n"))
	if option == 1:
		word = raw_input("ingresa la palabra que quieres deletrear\n")
		print_letter_by_letter(word)
	elif option == 2:
		quantity=int(raw_input('cuantas veces quieres decir mierda?\n'))
		print_mierda(quantity)

def print_letter_by_letter(word):
	for letter in word:
		print(letter)

	length=len(word)
	print('la palabra {} tiene una longitud de {} letras'.format(word,length))

def print_mierda(quantity):	
	for i in range(quantity):
		print('mierda')


if __name__ == '__main__':
	main()