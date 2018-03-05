# -*- coding: utf-8 -*-
import random

def main():
	number_found = False
	random_number = random.randint(0,20)

	while not number_found:
		number_try = int(raw_input('cual crees que es el numero?'))

		if number_try==random_number:
			print('felicidades, encontró el numero')
			number_found=True
		elif number_try<random_number:
			print('el número que se inventó la máquina es mayor')
		else:
			print('el número que se inventó la máquina es menor')


if __name__ == '__main__':
	main()