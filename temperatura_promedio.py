# coding: utf-8 -*-

def promedio(temperaturas):
	suma_de_temperaturas=0

	for temperatura in temperaturas:
		suma_de_temperaturas += float(temperatura)

	promedio = suma_de_temperaturas/len(temperaturas)

	return promedio

if __name__ == '__main__':
	temperaturas =[18,20,16,21,19,21]
	promedio=promedio(temperaturas)
	print('Las temperaturas son: {}'.format(temperaturas))
	print('La temperatura promedio es de: {0:.3f}'.format(promedio))