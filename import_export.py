import csv
import repo_crud as rc

def import_file():
    array_list = []
    with open('database.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            new_string = row[0].split(';')    # строка из CSV считывыются как список с одним элементом-строкой
                                              # из этой строки row[0] по разделителю ";" получаем список строк
            array_list.append(new_string)
    return (array_list)

def export_file(data):
    with open('database.csv','w') as file:
        for row in data:
            file.write(f"{';'.join(row)}\n")  # из списка строк row получаем строку с разделителем ";"
                                              #  в файл пишется СТРОКА
