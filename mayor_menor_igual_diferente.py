def main():
    primero = int(input('ingresa el primer numero: '))
    segundo = int(input('ingresa el segundo numero: '))
    print('Los numeros numeros ingresados son iguales? %s' % los_numeros_son_iguales(primero,segundo))
    print('Los numeros son diferentes? %s' % los_numeros_son_diferentes(primero,segundo))
    print('El primer numero es mayor que el segundo? %s' % primero_mayor_que_segundo(primero,segundo))
    print('El segundo es mayor que el primero? %s' % segundo_mayor_que_primero(primero,segundo))

def los_numeros_son_iguales(a,b):
    iguales = a==b
    return iguales

def los_numeros_son_diferentes(a,b):
    diferentes = a!=b
    return diferentes

def primero_mayor_que_segundo(a,b):
    mayor = a>b
    return mayor

def segundo_mayor_que_primero(a,b):
    menor = a<b
    return menor

if __name__=='__main__':
    main()
