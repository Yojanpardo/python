# -*- coding: utf-8 -*-
# las constantes se definen en mayusculas solo por buenas práctias

import random
import getpass

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
      |
=========''']

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

def show_board(hidden_word,tries,hidden_word_aux):
    print(IMAGES[tries])
    print('\n\n')
    hidden_word_text=''.join(hidden_word_aux)
    print(hidden_word_text)

def main():
    option=int(raw_input('escoge una opción:\n1. Una palabra aleatoria del sistema.\n2. Ingresa una palabra.\n'))
    tries=0
    letter_try = list()

    if option == 1:
        word=list(random_word())
    elif option == 2:
        word=list(getpass.getpass('ingresa la palabra:\n'))
    else: 
        print('Pon una opción de verdad')

    hidden_word = [' ___ ']*len(word)
    hidden_word_aux = ['']*len(word)

    while True:
        print('\n\n\n')
        show_board(hidden_word,tries,hidden_word_aux)
        print('\n\n')
        current_letter = str(raw_input('con que letra quieres probar?\n'))
        letter_found = False
        
        for letter in range(len(word)):
            if word[letter]==current_letter:
                letter_found = True
                hidden_word_aux[letter]='  '+current_letter+'  ' 
                hidden_word[letter]=current_letter

        word_text = ''.join(word)
        
        if word==hidden_word:
            print("""


              ______  ______  __   __  ______  ______  ______  ______    
             /\  ___\/\  __ \/\ "-.\ \/\  __ \/\  ___\/\__  _\/\  ___\   
             \ \ \__ \ \  __ \ \ \-.  \ \  __ \ \___  \/_/\ \/\ \  __\   
              \ \_____\ \_\ \_\ \_\ "\_\ \_\ \_\/\_____\ \ \_\ \ \_____\ 
               \/_____/\/_/\/_/\/_/ \/_/\/_/\/_/\/_____/  \/_/  \/_____/ 
                

                """)
            print('\n\n\nFelicidades, eres el mejor del mundo mundial!! :3 ')
            hidden_word_text=''.join(hidden_word)
            print('la palabra es: {}'.format(hidden_word_text))
            break

        if not letter_found:
            tries+=1
            letter_try.append(current_letter)
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
                print('La palabra era: {}\n\n'.format(word_text))
                break
        print('letras fallidas')
        print(letter_try)

if __name__ == '__main__':
    print(' ______  __  __  _____   ____    ____      ______  ____    _____       ')
    print('/\  _  \/\ \/\ \/\  __`\/\  _`\ /\  _`\.  /\  _  \/\  _`\ /\  __`\     ')
    print('\ \ \L\ \ \ \_\ \ \ \/\ \ \ \L\ \ \ \/\_\ \ \ \L\ \ \ \/\ \ \ \/\ \    ') 
    print(' \ \  __ \ \  _  \ \ \ \ \ \ ,  /\ \ \/_/_ \ \  __ \ \ \ \ \ \ \ \ \   ')
    print('  \ \ \/\ \ \ \ \ \ \ \_\ \ \ \ \ \ \ \ \L\ \ \ \ \/\ \ \ \_\ \ \_\ \  ')
    print('   \ \_\ \_\ \_\ \_\ \_____\ \_\ \_\ \____/  \ \_\ \_\ \____/\ \_____\ ')
    print('    \/_/\/_/\/_/\/_/\/_____/\/_/\/ /\/___/    \/_/\/_/\/___/  \/_____/ ')
    main()