from random import randint
import string

def birthday(length):
    birthdays = [] 
    for i in range(0, length):
        data = [str(randint(1, 31)), str(randint(1, 12)), str(randint(1970, 2005))]
        str_birthday = str(".".join(data))
        birthdays.append(str_birthday)
    return birthdays

def phone_number(length):
    phone_numbers = []
    for i in range(0, length):
        string = '+79'
        for j in range (9):
            string += str(randint(0, 9)) 
        phone_numbers.append(string)
    return phone_numbers
def create_dict():
    surname = ['Иванов', 'Петров', 'Сидоров', 'Зайцев', 'Васильев', 'Волков']
    name = ['Иван', 'Петр', 'Василий', 'Александр', 'Виктор', 'Андрей']
    position = ['секретарь', 'оператор', 'администратор', 'водитель', 'курьер', 'директор']
    address = ['ул. Ленина 35', 'ул. Тверская 40/2', 'ул. Революции 76', 'ул. Дубравная 5', 'ул. Цветная 17', 'ул. Спасская 1']
    birthdays = birthday(6)
    phone_numbers =phone_number(6)

    return dict([(i, f'{surname[randint(0,5)]}; {name[randint(0,5)]}; {birthdays[randint(0,5)]}; {position[randint(0,5)]}; {address[randint(0,5)]}; {phone_numbers[randint(0,5)]}') for i in range(1, 101)])