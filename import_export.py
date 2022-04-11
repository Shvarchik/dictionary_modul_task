import csv
import repo_crud as rc

def import_file():
    array_list = []
    with open('database.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            new_string = str(row).split(';')
            array_list.append(new_string)
    return (array_list)

def export_file(data):
    with open('database.csv','w') as file:
        for row in data:
            file.write(f'{str(row)}\n')
        
# with open('database.csv', 'w', newline='') as file:
     # writer = csv.writer(file)
     # for row in data:
     #     writer.writerow(row)

# data = import_file()
# export_file(data)