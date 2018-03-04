# -*- coding: utf-8 -*-

def main():
	option = int(raw_input("ingresa la opcción que deseas ejecutar.\n1. deletrear una palabra.\n2. decir mierda x cantidad de veces.\n3.Ver como se cancela una funcion con break\n"))
	if option == 1:
		word = raw_input("ingresa la palabra que quieres deletrear\n")
		print_letter_by_letter(word)
	elif option == 2:
		quantity=int(raw_input('cuantas veces quieres decir mierda?\n'))
		print_mierda(quantity)
	elif option==3:
		iterations = int(raw_input('cuantas iteraciones quieres?\n'))
		cancel = int(raw_input('con que numero quieres que se cancele la operacion(limite {})?\n'.format(iterations)))
		cancel_operation(iterations,cancel)

def print_letter_by_letter(word):
	for letter in word:
		print(letter)

	length=len(word)
	print('la palabra {} tiene una longitud de {} letras'.format(word,length))

def print_mierda(quantity):	
	for i in range(quantity):
		print('mierda')

def cancel_operation(iterations, cancel):
	for i in range(iterations):
		print(i)
		if i == cancel-1:
			print('operacion cancelada por el usuario con el numero {}'.format(cancel))
			break

if __name__ == '__main__':
	main()