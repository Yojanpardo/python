
def main():
    with open('aleph.txt', 'r') as opened_file:
        #print(opened_file.readlines())
        counter = 0
        for line in opened_file:
            counter += line.count('Beatriz')

        print('Beatriz se encuentra {} veces en el texto'.format(counter))

if __name__ == '__main__':
    main()
