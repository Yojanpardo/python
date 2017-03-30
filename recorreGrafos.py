
def recorre_grafo(nodo_final,arista,valor,intersecciones):

    while nodo_final != 15:
        print "ingresa el valor de la arista que escogiste"
        arista = input()
        valor = valor + arista
        valor = valor - 3
        print("ingresa la cantidad de intersecciones que realiza la arista")
        intersecciones = input()
        valor = valor - (intersecciones*2)
        print "ingresa el valor del nodo donde quedaste parado"
        nodo_final = input()
        print "el peso acumulado actual es de: %i" % valor

recorre_grafo(0,0,0,0)
