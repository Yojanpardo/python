# -*- coding: utf-8 -*-
# las constantes se definen en mayusculas solo por buenas práctias

import random

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
  'programación',
  'smartphone',
]

def random_word():
    id_word=random.randint(0,len(WORDS)-1)
    return WORDS[id_word]

def show_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)


def main():
    word=random_word()
    hidden_word = ['-']*len(word)
    tries=0

    while True:
        show_board(hidden_word,tries)
        current_letter = str(raw_input('con que letra quieres probar?\n'))

        letter_found = False

        for letter in range(len(word)):
            if word[letter]==current_letter:
                letter_found = True
                hidden_word[letter]=current_letter
        
        if not letter_found:
            tries+=1
        


if __name__ == '__main__':
    print(' ______  __  __  _____   ____    ____      ______  ____    _____       ')
    print('/\  _  \/\ \/\ \/\  __`\/\  _`\ /\  _`\   /\  _  \/\  _`\ /\  __`\     ')
    print('\ \ \L\ \ \ \_\ \ \ \/\ \ \ \L\ \ \ \/\_\ \ \ \L\ \ \ \/\ \ \ \/\ \    ') 
    print(' \ \  __ \ \  _  \ \ \ \ \ \ ,  /\ \ \/_/_ \ \  __ \ \ \ \ \ \ \ \ \   ')
    print('  \ \ \/\ \ \ \ \ \ \ \_\ \ \ \ \ \ \ \ \L\ \ \ \ \/\ \ \ \_\ \ \_\ \  ')
    print('   \ \_\ \_\ \_\ \_\ \_____\ \_\ \_\ \____/  \ \_\ \_\ \____/\ \_____\ ')
    print('    \/_/\/_/\/_/\/_/\/_____/\/_/\/ /\/___/    \/_/\/_/\/___/  \/_____/ ')
    main()