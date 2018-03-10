# -*- coding: utf-8 -*-
# las constantes se definen en mayusculas solo por buenas práctias

import random, getpass
import os

IMAGES = ['''
      +---+
      |   |
          |
          |
          |
          |
          |
    =========
''', '''
      +---+
      |   |
      O   |
          |
          |
          |
          |
    =========
''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
          |
    =========
''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
          |
    =========
''', '''
      +---+
      |   |
      O   |
     /|   |
      |   |
          |
          |
    =========
''', '''
      +---+
      |   |
      O   |
     /|\  |
      |   |
          |
          |
    =========
''', '''
      +---+
      |   |
      O   |
     /|\  |
      |   |
     /    |
          |
    =========
''', '''
      +---+
      |   |
      O   |
     /|\  |
      |   |
     / \  |
          |
    =========
''']

WORDS =[
  'guardia',
  'condones',
  'gato',
  'programacion',
  'smartphone',
]

def random_word():
    id_word=random.randint(0,len(WORDS)-1)
    return WORDS[id_word]

def show_board(hidden_word,tries):
    print(IMAGES[tries])
    print('\n\n')
    hidden_word_text=''.join(hidden_word)
    print(hidden_word_text)

def select(option):
    if option == 1:
        word=list(random_word())
    elif option == 2:
        word=''
        while not word.isalpha():
            word=getpass.getpass('ingresa la palabra:\n').lower()
            if not word.isalpha():
                print('''Ingresaste una palabra con caracteres no alfabeticos (puntos, comas, espacios, etc).

Por favor ingresa una sola palabra con caracteres alfabeticos.''')
        word=list(word)
    else: 
        print('Pon una opción de verdad')
        main()

    return word

def jugar_de_nuevo():
    jugar_de_nuevo='quizá'
    while jugar_de_nuevo!='si' or jugar_de_nuevo!='no':
        jugar_de_nuevo=str(input('Quieres volver a jugar? \nResponde: si o no. \n')).lower()
        if jugar_de_nuevo=='si':
            clear()
            print("""
                  ______  __  __  _____   ____    ____      ______  ____    _____       
                 /\  _  \/\ \/\ \/\  __`\/\  _`\ /\  _`\.  /\  _  \/\  _`\ /\  __`\     
                 \ \ \L\ \ \ \_\ \ \ \/\ \ \ \L\ \ \ \/\_\ \ \ \L\ \ \ \/\ \ \ \/\ \    
                  \ \  __ \ \  _  \ \ \ \ \ \ ,  /\ \ \/_/_ \ \  __ \ \ \ \ \ \ \ \ \    
                   \ \ \/\ \ \ \ \ \ \ \_\ \ \ \ \ \ \ \ \L\ \ \ \ \/\ \ \ \_\ \ \_\ \  
                    \ \_\ \_\ \_\ \_\ \_____\ \_\ \_\ \____/  \ \_\ \_\ \____/\ \_____\ 
                     \/_/\/_/\/_/\/_/\/_____/\/_/\/ /\/___/    \/_/\/_/\/___/  \/_____/ 
              """)
            main()
        elif jugar_de_nuevo=='no':
            exit()
        else:
            print('\n\nEscribe si o no, Pendejo\n\n')

def perdiste(tries,word_text):
    if tries ==7:
        print("""
        





        

            (         (    (     (    (                
             )\ )      )\ ) )\ )  )\ ) )\ )  *   )      
            (()/( (   (()/((()/( (()/((()/(` )  /( (    
            /(_)))\   /(_))/(_)) /(_))/(_))( )(_)))\   
            (_)) ((_) (_)) (_))_ (_)) (_)) (_(_())((_)  
            | _ \| __|| _ \ |   \|_ _|/ __||_   _|| __| 
            |  _/| _| |   / | |) |_|_ \__ \  | |  | _|  
            |_|  |___||_|_\ |___/|___||___/  |_|  |___| 
        



            """)
        print('La palabra era:     {}\n\n'.format(word_text))
        jugar_de_nuevo()

def ganaste(hidden_word):
    try:
        hidden_word.index(' ___ ')
    except ValueError:
        print("""



          ______  ______  __   __  ______  ______  ______  ______    
         /\  ___\/\  __ \/\ "-.\ \/\  __ \/\  ___\/\__  _\/\  ___\   
         \ \ \__ \ \  __ \ \ \-.  \ \  __ \ \___  \/_/\ \/\ \  __\   
          \ \_____\ \_\ \_\ \_\ "\_\ \_\ \_\/\_____\ \ \_\ \ \_____\ 
           \/_____/\/_/\/_/\/_/ \/_/\/_/\/_/\/_____/  \/_/  \/_____/ 




            

            """)
        print('\n\n\nFelicidades, eres el mejor del mundo mundial!! :3 \n\n')
        hidden_word_text=''.join(hidden_word).replace(' ','')
        print('la palabra es:\t{}\n'.format(hidden_word_text))
        jugar_de_nuevo()

def play(tries,letter_try,word,hidden_word):
    while True:
        print('\n\n\n')
        show_board(hidden_word,tries)
        print('\n\n')
        current_letter=''
        while len(current_letter) != 1 or not current_letter.isalpha():
            current_letter = str(input('Con que letra quieres probar?\n')).lower()
            clear()
            if not current_letter.isalpha():
                print('No se admiten caracteres no alfabeticos ni espacios.\n Intenta de nuevo.\n')
            elif len(current_letter) < 1:
                print('Por favor digita una letra.\n')

        letter_found = False
        
        for letter in range(len(word)):
            if word[letter]==current_letter:
                letter_found = True
                hidden_word[letter]='  '+current_letter+'  '
        
        if letter_found:
          print("Excelente, sigue asi :)\t\t\t\t\tVas {} intento(s) de 7".format(tries+1))
        else:
          print("Pesimo, intenta otra vez ¬¬\t\t\t\tVas {} intento(s) de 7".format(tries+1))


        word_text = ''.join(word)
        
        ganaste(hidden_word)

        if not letter_found:
            tries+=1
            letter_try.append(current_letter)
            perdiste(tries,word_text)

        print('letras fallidas')
        print(letter_try)


def clear(): #Funcion para limpiar las diferentes pantallas
    if os.name == "nt": # Windows
        os.system("cls")
    elif os.name == "posix": # Linux / Mac
        os.system("clear")

def main():
    try:
        option=int(input('escoge una opción:\n1. Una palabra aleatoria del sistema.\n2. Ingresa una palabra.\n'))
    except ValueError:
        print('ingresaste una letra, pendejo!\n\nPor favor ingresa el valor numerico de la opción\n\n')
        main()

    tries=0
    letter_try = list()
    word=select(option)

    hidden_word = [' ___ ']*len(word)
    
    play(tries,letter_try,word,hidden_word)

if __name__ == '__main__':
    print(' ______  __  __  _____   ____    ____      ______  ____    _____       ')
    print('/\  _  \/\ \/\ \/\  __`\/\  _`\ /\  _`\.  /\  _  \/\  _`\ /\  __`\     ')
    print('\ \ \L\ \ \ \_\ \ \ \/\ \ \ \L\ \ \ \/\_\ \ \ \L\ \ \ \/\ \ \ \/\ \    ') 
    print(' \ \  __ \ \  _  \ \ \ \ \ \ ,  /\ \ \/_/_ \ \  __ \ \ \ \ \ \ \ \ \   ')
    print('  \ \ \/\ \ \ \ \ \ \ \_\ \ \ \ \ \ \ \ \L\ \ \ \ \/\ \ \ \_\ \ \_\ \  ')
    print('   \ \_\ \_\ \_\ \_\ \_____\ \_\ \_\ \____/  \ \_\ \_\ \____/\ \_____\ ')
    print('    \/_/\/_/\/_/\/_/\/_____/\/_/\/ /\/___/    \/_/\/_/\/___/  \/_____/ ')
    main()