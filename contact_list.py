# -*- coding: utf-8 -*-

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

    def _update_contact(self, contact, new_name, new_phone, new_email, old_name):
        self.delete(old_name)
        self.add(new_name, new_phone, new_email)

    def _not_found(self):
        print('''
******
*******
*******

Contact not found
''')


def main():

    contact_book = ContactBook()

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
