# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
	mex_to_col_rate = 145.97
	return mex_to_col_rate*ammount

def calculate():
	print('C A L C U L A D O R A   D E   D I V I S A S ')
	print('convierte pesos mexicanos a pesos colombianos con solo un para de clicks')
	print('')
	
	ammount=float(raw_input('cuantos pesos mexicanos quieres convertir? '))

	col = foreign_exchange_calculator(ammount)

	print('${} pesos mexicanos son ${} pesos colombianos!'.format(ammount,col))
	print('')
if __name__ == '__main__':
	calculate()