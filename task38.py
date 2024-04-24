def input_surname():
    return input('Введите фамилию контакта: ').title()
def input_name():
    return input('Введите имя контакта: ').title()
def input_patronymic():
    return input('Введите отчество контакта: ').title()
def input_phone():
    return input('Введите телефон контакта: ')
def input_adress():
    return input('Введите город контакта: ').title()

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    return f'{surname} {name} {patronymic}: {phone}\n{adress}\n\n'

def add_contact():
    contact_str = create_contact()
    with open ("phonebook.txt", 'a', encoding = 'utf-8') as file:
        file.write(contact_str)

def print_contacts():
    with open ("phonebook.txt", 'r', encoding = 'utf-8') as file:
        contacts_str = file.read()
    #print([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)

def search_contact():
    print(
            'Возможные варианты поиска:\n'
            '1. По фамилии\n'
            '2. По имени\n'
            '3. По отчеству\n'
            '4. По телефону\n'
            '5. По адресу\n'
            )
    var = input('Выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод')
        var = input('Выберите вариант поиска: ')
    i_var = int(var) - 1


    search = input('Введите данные для поиска: ').title()
    with open ("phonebook.txt", 'r', encoding = 'utf-8') as file:
        contacts_str = file.read()
    #print([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    #print(contacts_list)

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:
            print(str_contact)

def change_contact():
    pass

'''
Простите, но у меня ничего не получается. Я совсем запутался. Подскажите, пожалуйста, где я могу рассмотреть
пример работающего кода телефонного справочника с возможностями изменения и удаления данных?
'''

def delete_contact():
    with open ("phonebook.txt", 'r', encoding = 'utf-8') as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')
    contact = input('Введите контакт для удаления: ')
    if contact in contacts_str():
        contacts_str.remove(contact)
        with open ("phonebook.txt", 'w', encoding = 'utf-8') as file:
            file.write(contacts_list)
    else:
        print('Некорректный ввод')

    #     contacts_str = file.read()
    # contacts_list = contacts_str.rstrip().split('\n\n')
    # for n, contact in enumerate(contacts_list, 1):
    #     print(n, contact)
    # cont = search_contact()
    # contacts_list = contacts_str.rstrip().split('\n\n')
    # n = 0
    # int = input('Выберите контакт для удаления: ')
    # while int > n:
    #     print('Некорректный ввод')
    #     int = input('Выберите вариант поиска: ')
    # else:

    #     for cont in contacts_list:
    #         file.write(contacts_str)


def interface():
    with open ("phonebook.txt", 'a', encoding = 'utf-8'):
        pass

    var = 0
    while var != '6':
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Изменить контакт\n'
            '5. Удалить контакт\n'
            '6. Выход\n'
            )
        var = input('Выберите вариант действия: ')
        while var not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            var = input('Выберите вариант действия: ')
        print()

        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                change_contact()
            case '5':
                delete_contact()
            case '6':
                print('До свидания')
        print()

if __name__ == '__main__':
    interface()
