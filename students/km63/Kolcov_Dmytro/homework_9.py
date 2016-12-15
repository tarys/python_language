#task1------------------------------------------------------------
"""
��� ������ �����. ����������, ������� � ��� ����������� ��������� �����.
"""
liste = set(input().split())
print (len(liste))
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
���� ��� ������ �����. ����������, ������� ����� ���������� ������������ ��� � ������ ������, ��� � �� ������.
"""
list_1 = set(input().split())
list_2 = set(input().split())
new_list = list_1 & list_2
print (len(new_list))
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
�� ������� ������ �������� ������������������ ����� ����� ������. ��� ������� ����� �������� ����� YES (� ��������� ������),
���� ��� ����� ����� ����������� � ������������������ ��� NO, ���� �� �����������.
"""
liste = input().split()
for i in range (len (liste)):
    if liste[i] in liste[:i]:
        print ('YES')
    else:
        print ('NO')
#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
��� �����: � ������ ������ �������� ����� �����, ����� ���� ���� ������. ����������, ������� ��������� ���� ���������� � ���� ������.

������ ��������� ������������������ ������������ �������� ������ ������, ����� ��������� ����� ��� ������� ������ �������� ��� ��������� ����� ������.
"""
nam = int(input())
liste = set()
for i in range (nam):
    liste = liste | set(input().split())
print (len(liste))
#-----------------------------------------------------------------

#task9------------------------------------------------------------
"""
������ �� ���������� ��������� ���������� ��������� ����� ����� ��������� ���������� ������. ����� ���������� ������� ������ ����� ��� ���������, � ������� ������ ����� ���� �� ���� �� ����������.

� ������ ������ ������ ���������� ����������. ��� ������� �� ���������� ������ �������� ���������� ������, ������� �� �����, � ����� - �������� ������, �� ������ � ������.

� ������ ������ �������� ���������� ������, ������� ���� ��� ���������. ������� �� ������ ������ - ������ ����� ������. ����� - ���������� ������, 
������� ����� ���� �� ���� ��������, �� ��������� ������� - ������ ����� ������. ����� ����� �������� � ������������������ �������, �� ������ �� ������.
"""
def inpute(count):
    liste = set()
    for i in range(count):
        liste.add(input())
    return (liste)
liste = []
languages = set()
schools = set()
count_of_schools = int(input())
for j in range (count_of_schools):
    count_of_languages = int(input())
    liste.append(inpute(count_of_languages))
for j in range (count_of_schools-1):
    schools = schools | liste[j] & liste[j+1]
for j in range (count_of_schools-1):
    languages = languages | liste[j] | liste[j+1]
print (len(schools))
for i in range (len(schools)):
    print (list(schools)[i])
print (len(languages))
for i in range (len(languages)):
    print (list(languages)[i])
#-----------------------------------------------------------------