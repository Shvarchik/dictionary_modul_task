from random import randint
import dictionary_create as dc

# dictionary = dc.create_dict()
# def file_create(dictionary):
#     with open('database.csv', 'w') as file:
#         for i in dictionary:
#            file.write('{}; {}\n'.format(i,dictionary[i]))

def file_create():
    with open('database.csv', 'w') as file:
        for i in dc.create_dict():
            file.write('{}; {}\n'.format(i,dc.create_dict()[i]))


def create_string():
    surname = ['Иванов', 'Петров', 'Сидоров', 'Зайцев', 'Васильев', 'Волков']
    name = ['Иван', 'Петр', 'Василий', 'Александр', 'Виктор', 'Андрей']
    position = ['секретарь', 'оператор', 'администратор', 'водитель', 'курьер', 'директор']
    address = ['ул. Ленина 35', 'ул. Тверская 40/2', 'ул. Революции 76', 'ул. Дубравная 5', 'ул. Цветная 17', 'ул. Спасская 1']
    birthdays = dc.birthday(6)
    phone_numbers =dc.phone_number(6)

    new_string = (f'{surname[randint(0,5)]}; {name[randint(0,5)]}; {birthdays[randint(0,5)]}; {position[randint(0,5)]}; {address[randint(0,5)]}; {phone_numbers[randint(0,5)]}')
    return new_string
