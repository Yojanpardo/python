# -*- coding: utf-8 -*-

def binary_search(lista,number_to_find,low,high):
	if low>high:
		return False
	
	mid = int((low+high)/2)

	if lista[mid]==number_to_find:
		return True
	elif number_to_find < lista[mid]:
		return binary_search(lista,number_to_find,low,mid -1)
	else:
		return binary_search(lista,number_to_find,mid+1,high)

if __name__ == '__main__':
	lista=[1,2,3,5,8,9,11,15,18,25,30,35,36,37,39,40,48,50,51,52,56,58,59,60]
	
	number_to_find = int(input('ingresa un numero:\n'))
	
	result= binary_search(lista, number_to_find,0,len(lista)-1)

	if result:
		print('el número sí se encuentra en la lista')
	else:
		print('el número no se encuentra en la lista')