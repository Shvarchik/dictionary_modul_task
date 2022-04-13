import user_interface as ui
import logger as log
import create_file as cf
import import_export as ie

def create_new():
    cf.file_create()
    log.logger('создание файла')

def create():
    data = ie.import_file()
    id = (input("Введите ID: "))
    fam = input("Введите фамилию: ")
    name = input("Введите имя: ")
    bd = input('Введите дату рождения: ')
    poz = input("Введите должность: ")
    adr = input("Введите адрес: ")
    tel = input('Введите телефон: ')
    new_record =  [id,fam,name,bd,poz,adr,tel]
    data.append(new_record)
    ie.export_file(data)
    log.logger('новая запись в файле')
    
def read():
    id_choice = ui.choice(3)
    print (ie.import_file()[id_choice-1])
    log.logger('чтение записи')
      
def update():
    id_choice = ui.choice(3)
    data = ie.import_file()
    print(data[id_choice-1])
    old = input('Введите, что нужно изменить: ')
    new = input('Введите то, на что нужно изменить: ')
    for i in range (0,len(data[id_choice])):
        if data [id_choice-1][i] == old:
            data [id_choice-1][i] = new
    print(data[id_choice-1])
    ie.export_file(data)
    log.logger('внесение изменений')
    
def delete():
    id_choice = ui.choice(3)
    data = ie.import_file()
    while id_choice > len(data):
        print ('записи с таким номером не существует, попробуйте еще раз: ')
        id_choice = ui.id() 
    data.pop(id_choice-1)
    for i in range (id_choice-1,len(data)):
        data [i][0] = str(i+1)
    ie.export_file(data)
    log.logger('удаление записи')
    

def result():
    id_choice = ui.choice(1)
    while id_choice != 0:
        if id_choice == 1: create_new()
        elif id_choice == 2: create()
        elif id_choice == 3: read()
        elif id_choice == 4: update()
        else: delete()
        if ui.choice(2) == 0: exit()
        else: id_choice = ui.choice(1)



