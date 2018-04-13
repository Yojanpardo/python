# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'perú': 31
}

while True:
    country = str(input('Escribe el pais del cual quieres conocer su cantidad de habitantes: ')).lower()
    try:
        print('La población de {} es de {} Millones de habitantes'.format(country, countries[country]))
    except KeyError:
        print('No tenemos el dato de la población de {}'.format(country))
