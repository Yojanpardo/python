# -*- coding: utf-8 -*-

import turtle

def main():
	window = turtle.Screen()
	crush = turtle.Turtle()

	make_scuare(crush)

	turtle.mainloop()

def make_scuare(crush):
	length = int(raw_input('De qué tamaño quieres que sea el lado del cuadrado? '))
	for x in range(4):
		make_line_and_turn(crush, length)

def make_line_and_turn(crush, length):
	crush.forward(length)
	crush.left(90)

if __name__ == '__main__': #define la funcion principal y el orden en el cual se deben ejecutar las cosas
	main()
