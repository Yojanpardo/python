# -*- coding: utf-8 -*-

class Lamp:
    _LAMPS = ['''






                      .
                 .    |    ,
                  \   '   /
                   ` ,-. '
                --- (   ) ---
                     \ /
                    _|=|_
                   |_____|
                ''',
                '''









                     ,-.
                    (   )
                     \ /
                    _|=|_
                   |_____|
    ''']

    def __init__(self, _is_turned_on):#esto es el constructos de la clase y se definen las variables de instancia
        self._is_turned_on = _is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def main():
    lamp = Lamp(_is_turned_on=False)

    while True:
        command = str(input('''



Escribe un comando
[p]render
[a]pagar
[s]alir


'''))
        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            exit()
if __name__ == '__main__':
    main()
