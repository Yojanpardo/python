

def factorial(numero):
	if numero == 0:
		return 1

	return numero * factorial(numero-1)


if __name__ == '__main__':
	numero = int(raw_input("escribe un numero para encontrar su factorial"))
	
	result = factorial(numero)

	print('{} es el reultado'.format(result))