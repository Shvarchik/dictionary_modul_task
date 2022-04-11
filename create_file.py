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


