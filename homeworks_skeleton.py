import yaml
import os

with open('students.yml', 'r') as students_list_file:
    students = yaml.load(students_list_file)

for group in students['groups']:
    directory = './students/' + group
    if not os.path.isdir(directory):
        os.makedirs(directory)

    for student in students['groups'][group]:
        file_name = directory + '/' + student + ".py"
        if not os.path.isfile(file_name):
            file = open(file_name, "w")
            for i in range(10):
                file.write('def homework_{number}():\n    print(\'put your code here\')\n\n\n'.format(number=i+1))
            file.close()
