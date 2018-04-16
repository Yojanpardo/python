# -*- coding: utf-8 -*-
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts=[]

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
        input('presiona enter para continuar')

    def _print_contact(self, contact):
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('____________________________________')

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                break

        self._save()

        input('\nPresiona enter para continuar\n')

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower()==name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

        input('Presiona enter para continuar')

    def modify(self, name):
        for contact in self._contacts:
            if contact.name.lower()==name.lower():
                self._print_contact(contact)
                new_name = str(input('\n\n\nIngresa el nuevo nombre del contacto:\n'))
                new_phone = str(input('Ingresa el nuevo número telefónico del contacto:\n'))
                new_email = str(input('Ingresa el nuevo email del contacto:\n'))

                self._update_contact(contact, new_name, new_phone, new_email, name)

                break
        else:
            self._not_found()

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

    def _update_contact(self, contact, new_name, new_phone, new_email, old_name):
        self.delete(old_name)
        self.add(new_name, new_phone, new_email)
        self.save()

    def _not_found(self):
        print('''
******
*******
*******

Contact not found
''')


def main():

    contact_book = ContactBook()

    with open('contacts.csv', 'r', encoding='utf-8') as f:

        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            if row ==[]:
                continue
            else:
                contact_book.add(row[0], row[1], row[2])

    while True:
        try:
            command = int(input('''
\n\n\n\n\n\n\n\
Qué deseas hacer?

1. Añadir contacto
2. Actualizar contacto
3. Buscar contacto
4. Eliminar contacto
5. Listar contactos
0. Salir
\n\n\n\n\n\n
'''))
        except ValueError:
            print('Por favor ingresa un numero de la lista')
            input('Presiona enter para continuar')
            return main()

        if command == 1:
            name = str(input('Ingresa el nombre del contacto:\n'))
            phone = str(input('Ingresa el número telefónico del contacto:\n'))
            email = str(input('Ingresa el email del contacto:\n'))

            contact_book.add(name, phone, email)

        elif command == 2:
            name = str(input('ingresa el nombre del contacto que desas actualizar:\n'))
            contact_book.modify(name)

        elif command == 3:
            name = str(input('ingresa el nombre del contacto que desas buscar:\n'))
            contact_book.search(name)

        elif command == 4:
            name = str(input('Ingresa el nombre del contacto que deseas eliminar:\n'))
            contact_book.delete(name)

        elif command == 5:
            contact_book.show_all()

        elif command == 0:
            print('Hasta la próxima!')
            exit()

        else:
            print('por favor ingresa un valor correcto, pendejo')

if __name__ == '__main__':
    main()
