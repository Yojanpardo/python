# -*- coding: utf-8 -*-
from lamp import Lamp

def main():
    lampara = Lamp(_is_turned_on=False)

    while True:
        command = str(input('''



Escribe un comando
[p]render
[a]pagar
[s]alir


'''))
        if command == 'p':
            lampara.turn_on()
        elif command == 'a':
            lampara.turn_off()
        else:
            exit()
if __name__ == '__main__':
    main()
