from random import randint
import dictionary_create as dc

#dictionary = { 1: 'Иванов; Александр; 10.8.2001; администратор; ул. Революции 76; +79971628368',
 #2: 'Волков; Андрей; 17.5.1997; администратор; ул. Цветная 17; +79287195720',
 #3: 'Иванов; Андрей; 21.6.1994; секретарь; ул. Революции 76; +79266170302',
 #4: 'Волков; Иван; 21.5.1971; директор; ул. Цветная 17; +79178131240',
 #5: 'Васильев; Александр; 21.6.1994; оператор; ул. Революции 76; +79767653675'}
dictionary = dc.create_dict()
def file_create(dictionary):
    with open('database.csv', 'w') as file:
        for i in dictionary:
            file.write(f'{dictionary[i]}\n')


# def birthday(length):
#     birthdays = [] 
#     for i in range(0, length):
#         data = [str(randint(1, 31)), str(randint(1, 12)), str(randint(1970, 2005))]
#         str_birthday = str(".".join(data))
#         birthdays.append(str_birthday)
#     return birthdays

# def phone_number(length):
#     phone_numbers = []
#     for i in range(0, length):
#         string = '+79'
#         for j in range (9):
#             string += str(randint(0, 9)) 
#         phone_numbers.append(string)
#     return phone_numbers

def create_string():
    surname = ['Иванов', 'Петров', 'Сидоров', 'Зайцев', 'Васильев', 'Волков']
    name = ['Иван', 'Петр', 'Василий', 'Александр', 'Виктор', 'Андрей']
    position = ['секретарь', 'оператор', 'администратор', 'водитель', 'курьер', 'директор']
    address = ['ул. Ленина 35', 'ул. Тверская 40/2', 'ул. Революции 76', 'ул. Дубравная 5', 'ул. Цветная 17', 'ул. Спасская 1']
    birthdays = dc.birthday(6)
    phone_numbers =dc.phone_number(6)

    new_string = (f'{surname[randint(0,5)]}; {name[randint(0,5)]}; {birthdays[randint(0,5)]}; {position[randint(0,5)]}; {address[randint(0,5)]}; {phone_numbers[randint(0,5)]}')
    return new_string
