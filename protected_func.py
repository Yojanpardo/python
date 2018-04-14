# -*- coding: utf-8 -*-

def protected(func):

	def wrapper(password):

		if password == 'cuca':
			return func()
		else:
			print('La contraseña es incorrecta: =C')

	return wrapper

@protected
def protected_func():
	print('contraseña correcta =D')

if __name__ == '__main__':
	password = str(input('ingresa la contraseña:\n'))

	protected_func(password)
