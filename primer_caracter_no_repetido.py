 # -*- coding: utf-8 -*-

def first_not_repeating_char(sequence):
    seen_letters = {}

    for idx, letter in enumerate(sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter]=(seen_letters[letter][0],seen_letters[letter][1]+1)

        final_letters = []
        for key, value in seen_letters.items():
            if value[1] == 1:
                final_letters.append( (key, value[0]) )

        not_repeated_letters = sorted(final_letters,key=lambda value: value[1]) #esto es lo mismo que definir una funcion en una linea

        if not_repeated_letters:
            return not_repeated_letters
        else:
            return '_'


if __name__ == '__main__':
    sequence = str(input('Ingresa una cadena de caracteres:\n'))
    result = first_not_repeating_char(sequence)
    if result=='_':
        print('Todos los caracteres se repiten')
    elif len(result)>1:
        print('Los caracteres que no se repiten son: {}'.format(result))
    else:
        print('El caracter que no se repite es: {}'.format(result))
