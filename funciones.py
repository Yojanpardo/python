#esta es una funcion que toma como parametro dos variables
def suma(a,b):
	return a + b
	
'''aquí imprime la suma y le mando por parametros esas mierdas'''
d=suma(23,12)

print d

#combinación de cadenas de texto en una función.
def saludo(nombre):
	return "hola %s" % nombre

print saludo("Yojan")