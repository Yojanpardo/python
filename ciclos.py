def main():
    ciclos(0,0)

def ciclos(numero_while,numero_for):
    #para un ciclo while lo que hacemos es lo siguiente
    while numero_while < 10:
        print(numero_while)
        numero_while += 1
    #para un ciclo for:
    for numero_for in 10:
        print(numero_for)

if __name__=='__main__':
    main()
