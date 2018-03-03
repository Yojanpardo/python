# -*- coding: utf-8 -*-

def main():
	number = int(raw_input('escribe un numero y determinaremos si éste es primo o no'))
	result = is_prime(number)

	if result:
		print('Tu número es primo')
	else:
		print('tu número no es primo')

def is_prime(number):
	if number <= 1:
		return False
	elif number == 2:
		return True
	elif number > 2 and number%2 == 0:
		return False
	else:
		for i in range(3,number):
			if number % i == 0:
				return False
	return True


if __name__ == '__main__':
	main()