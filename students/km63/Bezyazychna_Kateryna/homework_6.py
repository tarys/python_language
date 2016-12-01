#task1--------------------------
"""
�������� ��� �������� ������ � ������� ��������� (�� ���� A[0], A[2], A[4], ...).
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    data = []

    for i in range(0, len(elements), 2):

        data.append(elements[i])

    return data



def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))

#-----------------------------------------


#task2--------------------------
"""
�������� ��� ������ �������� ������.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    data = []

    for i in elements:

        if int(i) % 2 == 0:

            data.append(i)

    return data



def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))


#-----------------------------------------


#task3--------------------------
"""
��� ������ �����. �������� ��� �������� ������, ������� ������ ����������� ��������.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    data = []

    for i in range(0, len(elements)):

        if i < len(elements)-1:

            if int(elements[i]) < int(elements[i + 1]):

                data.append(elements[i +1])

    return data



def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))
#-----------------------------------------


#task4--------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, 
�������� ��� �����. ���� �������� ��������� ������ ����� ��� � �� �������� ������. 
���� ����� ��� ������� ��������� � �������� ������ ����.
"""
def input_data():

    data = input().split()

    return data


def operation_data(elements):

    data = []

    for i in range(0, len(elements)):

        if len(data) == 0:

            if i < len(elements)-1:

                if int(elements[i]) * int(elements[i + 1]) > 0:
                    data = [elements[i]]

                    data.append(elements[i + 1])

    return data


def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))









#-----------------------------------------


#task5--------------------------
"""
��� ������ �����. ����������, ������� � ���� ������ ���������, 
������� ������ ���� ����� �������, � �������� ���������� ����� ���������. 
������� �������� ������ ������� �� �����������, ��������� � ��� ������������ �������.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    counter = 0

    for i in range(1, len(elements)-1):

        if int(elements[i-1]) < int(elements[i]) > int(elements[i+1]):
            counter +=1

    return counter
 


def print_data(output_data):

    print (output_data)



print_data(operation_data(input_data()))

#-----------------------------------------


#task6--------------------------
"""
��� ������ �����. �������� �������� ����������� �������� � ������, 
� ����� ������ ����� �������� � ������. ���� ���������� ��������� ���������, 
�������� ������ ������� �� ���.
"""
def input_data():
    data = input().split()
    return data
    
def operation_data(elements):

    data = []

    max_elements = elements[0]

    data = [max_elements]

    data.append(0)

    for i in range(1, len(elements)):

        if int(max_elements) < int(elements[i]):

            max_elements = elements[i]

            data = [max_elements]

            data.append(i)
       
    return data
    
def print_data(output_data):
    for i in output_data:
        print (i, end=' ')

print_data(operation_data(input_data()))

#-----------------------------------------
#task7--------------------------
"""
���� ������� � ������ �����. 
�� ����� ����������� ��� ������������ ���������� ��� ����� � �����. 
�������� ��� ��� �������.
��������� �������� �� ���� �������������� ������������������ ����������� �����, 
���������� ���� ������� �������� � �����. ����� ����� �������� ����� X � ���� ����. 
��� ����� �� ������� ������ ����������� � �� ��������� 200.

�������� �����, ��� ������� ���� ������ ������ � �����. 
���� � ����� ���� ���� � ���������� ������, ����� ��, ��� � ����, 
�� �� ������ ������ ����� ���.
"""
def input_data():

    data = input().split()

    return data


def operation_data(elements):

    hight = int(input())

    position = 0

    while position < len(elements) and int(elements[position]) >= hight:

        position += 1

    return position


def print_data(output_data):

        print (output_data + 1)



print_data(operation_data(input_data()))

#-----------------------------------------
#task8--------------------------
"""
��� ������, ������������� �� ���������� ��������� � ���. 
����������, ������� � ��� ��������� ���������.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    counter = 0

    for i in range(0, len(elements)-1):

        if int(elements[i]) != int(elements[i + 1]):

            counter +=1

    return counter



def print_data(output_data):

        print (output_data + 1)



print_data(operation_data(input_data()))

#-----------------------------------------
#task9--------------------------
"""
����������� �������� �������� ������ (A[0] c A[1], A[2] c A[3] � �. �.). 
���� ��������� �������� �����, �� ��������� ������� �������� �� ����� �����.
"""
def input_data():

    data = input().split()

    return data

    

def operation_data(elements):

    for i in range(0, len(elements)//2):

	elements[i*2], elements[i*2 + 1] = elements[i*2 + 1], elements[i*2]
    return element


def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))

#-----------------------------------------
#task10--------------------------
"""
� ������ ��� �������� ��������. 
��������� ������� ����������� � ������������ ������� ����� ������.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    max_element = elements[0]

    min_element = elements[0]

    index_min = 0

    index_max = 0

    for i in range(0, len(elements)):

        if  int(min_element) > int(elements[i]):

            min_element = elements[i]

            index_min = i

        if  int(max_element) < int(elements[i]):

            max_element = elements[i]

            index_max = i
    
    elements[index_min], elements[index_max] = elements[index_max], elements[index_min]    
    return elements



def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))


#-----------------------------------------
#task11--------------------------
"""
��� ������ �� ����� � ������ �������� � ������ k. 
������� �� ������ ������� � �������� k, 
������� ����� ��� ��������, ������� ������ �������� � �������� k.
��������� �������� �� ���� ������, ����� ����� k. 
��������� �������� ��� ��������, � ����� ����� ������� ��������� ������� 
������ ��� ������ ������ pop() ��� ����������.

��������� ������ ������������ ����� ��������������� � ������, 
� �� ������ ��� ��� ������ ���������. ����� ������ ������������ �������������� ������. 
����� �� ������� ������������ ����� pop(k) � ����������.
"""
def input_data():

    data = input().split()

    return data


def operation_data(elements):

    k = int(input())

    for i in range(k, len(elements) - 1):

        elements[i] = elements[i + 1]

    elements.pop()

    return elements
    

def print_data(output_data):

    for i in output_data:
        print (i, end=' ')
        


print_data(operation_data(input_data()))


#-----------------------------------------
#task12--------------------------
"""
��� ������ ����� �����, ����� k � �������� C. 
���������� �������� � ������ �� ������� � �������� k �������, 
������ C, ������� ��� ��������, ������� ������ �� ����� k, ������.
��������� ��� ���� ���������� ��������� � ������ �������������, 
����� ���������� ������ � ��� ����� ����� ����� �������� ����� �������, 
��������� ����� append.

������� ���������� ������������ ��� � ��������� ������, �� ����� ����� 
��� ������ � �� �������� ��������������� ������.
"""
def input_data():

    data = input().split()

    return data

    

def operation_data(elements):

    data = input().split()

    elements.append(data[1])

    for i in range(len(elements) - 1, int(data[0]), -1):

        elements[i] = elements[i - 1]

    elements[int(data[0])] = int(data[1])

    return elements

    

def print_data(output_data):
   for i in output_data:

        print (i, end=' ')
  
      

print_data(operation_data(input_data()))


#-----------------------------------------
#task13--------------------------
"""
��� ������ �����. ����������, ������� � ��� ��� ���������, 
������ ���� �����. ���������, ��� ����� ��� ��������, 
������ ���� ����� �������� ���� ����, ������� ���������� ���������.
"""
def input_data():

    data = input().split()

    return data

    

def operation_data(elements):

    suma=0

    for j in range(0,len(elements)):

        b=elements[j]

        for i in range(j+1,len(elements)):

            if b==elements[i]:

                suma+=1

    return suma

    

def print_data(output_data):

        print (output_data)

        

print_data(operation_data(input_data()))




#-----------------------------------------


#task14--------------------------
"""
��� ������. �������� �� ��� ��������, 
������� ����������� � ������ ������ ���� ���. 
�������� ����� �������� � ��� �������, 
� ������� ��� ����������� � ������.
"""
def input_data():

    data = input().split()

    return data

    

def operation_data(elements):
    data=[]

    for i in range(0, len(elements)):

        counter = 0

        for j in range(0, len(elements)):

            if elements[i] == elements[j]:

                counter += 1

        if counter == 1:

            data.append(elements[i])

    return data
 
    

def print_data(output_data):

    for i in output_data:

        print (i, end=' ')

        
print_data(operation_data(input_data()))            

#-----------------------------------------

#task15--------------------------
"""
N ������ ��������� � ���� ���, ����������� �� ����� ������� ������� �� 1 �� N. 
����� �� ����� ���� ������� K �����, ��� ���� i-� ��� ���� ��� ����� � 
�������� �� li �� ri ������������. ����������, ����� ����� �������� 
������ �� �����.
��������� �������� �� ���� ���������� ������ N � ���������� ������� K. 
����� ���� K ��� ����� li, ri, ��� ���� 1? li? ri? N.

��������� ������ ������� ������������������ �� N ��������, ��� j-� ������ 
���� �I�, ���� j-� ����� �������� ������, ��� �.�, ���� j-� ����� ���� �����.
"""
s = input().split(' ')

outs = ["I" for i in range(int(s[0]))]


for i in range(int(s[1])):

    ns = input().split(' ')

    for f in range(int(ns[0])-1, int(ns[1])):

        outs[f] = "."

for i in outs:

    print(i, end='')

#-----------------------------------------
#task16--------------------------
"""
�������
��������, ��� �� ����� 8?8 ����� ���������� 8 ������ ���, ����� ��� �� 
���� ���� �����. ��� ���� ����������� 8 ������ �� �����, ����������, 
���� �� ����� ��� ���� ������ ���� �����.
��������� �������� �� ���� ������ ��� �����, 
������ ����� �� 1 �� 8 � ���������� 8 ������. 
���� ����� �� ���� ���� �����, �������� ����� NO, ����� �������� YES.
"""
list1 = []
list2 = []
for i in range(8):
    s = input().split(' ')
    s[0] = int(s[0])
    s[1] = int(s[1])
    list1.append(s[0])
    list2.append(s[1])
if len(list1) == len(set(list1)) and len(list2) == len(set(list2)):
    print('NO')
else:
    print('YES')
#-----------------------------------------

