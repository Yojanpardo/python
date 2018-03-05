# -*- coding: utf-8 -*-

def palindromo(word):
	reversed_letters = []

	for letter in word:
		reversed_letters.insert(0, letter)

	reversed_word=''.join(reversed_letters)

	if reversed_word==word:
		return True
	else:
		return False

def palindromo2(word):
	if word==word[::-1]:
		return True
	else:
		return False

if __name__ == '__main__':
	print('--------------P A L I N D R O M O--------------')
	print('descubre si una palabra es un palindromo o no')
	
	word=str(raw_input('escribe una palabra\n'))
	
	if palindromo2(word):
		print('nu ma! si es un palindromo')
	else:
		print('no es un palindromo')
