import yaml
import os

with open('students.yml', 'r') as students_list_file:
    students = yaml.load(students_list_file)

    for group in students['groups']:
        for student in students['groups'][group]:
            student_directory = './students/' + group + '/' + student

            if not os.path.isdir(student_directory):
                os.makedirs(student_directory)

            file_name = student_directory + '/welcome.py'
            if not os.path.isfile(file_name):
                file = open(file_name, "w")
                student_name = student.split('_')[1]
                file.write('print(\'Welcome aboard, {}!\')\n'.format(student_name))
                file.close()
