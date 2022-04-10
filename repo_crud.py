import user_interface as ui
import logger as log
import create_file as cf


def create():
    f = len(cf.dictionary)+1
    cf.dictionary[f] =  cf.create_string() 
    print(cf.dictionary)
    cf.file_create(cf.dictionary)
    log.logger()

def read():
    id_choice = ui.id()
    print(cf.dictionary[id_choice])
    log.logger()

def update():
    id_choice = ui.id()
    print(cf.dictionary[id_choice])
    old = input('Введите, что нужно изменить: ')
    new = input('Введите то, на что нужно изменить: ')
    cf.dictionary[id_choice] = cf.dictionary[id_choice].replace(old, new)
    log.logger()
    cf.file_create(cf.dictionary)

def delete():
    id_choice = ui.id()
    a = cf.dictionary
    del a[id_choice]
    log.logger()
    cf.file_create(a)

def result():
    id_choice = ui.choice()
    if id_choice == 1: create()
    elif id_choice == 2: 
        read()
        exit()
    elif id_choice == 3: update()
    else: delete()

