# -*- coding: utf-8 -*-

def main():
    with open('numeros.txt', 'w') as f:
        for number in range(10):
            f.write(str(number))

if __name__ == '__main__':
    main()
