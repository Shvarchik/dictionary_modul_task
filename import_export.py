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

def export_file():
    with open('database.csv') as f:
        writer = csv.writer(f)
        for row in import_file():
            writer.writerow(row)


print (import_file())
print()

with open('database.csv') as f:
    print(f.read())