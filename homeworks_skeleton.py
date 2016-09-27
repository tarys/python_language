import yaml
import os

with open('students.yml', 'r') as students_list_file:
    students = yaml.load(students_list_file)

for group in students['groups']:
    directory = './students/' + group
    if not os.path.isdir(directory):
        os.makedirs(directory)

    for student in students['groups'][group]:
        student_directory = directory + '/' + student

        if not os.path.isdir(student_directory):
            os.makedirs(student_directory)

        file_name = student_directory + '/' + student + ".py"
        if not os.path.isfile(file_name):
            file = open(file_name, "w")
            file.write('print(\'Welcome aboard, {}!\')\n'.format(student.split('_')[1]))
            file.close()
