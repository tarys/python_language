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
            if i < len(elements)-1:
                if int(elements[i]) * int(elements[i + 1]) > 0:
                    data = [elements[i]]
                    data.append(elements[i + 1])
                    break
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
    count=0
    for i in range(1, len(elements)-1):
                if int(elements[i-1])<int(elements[i]) and int(elements[i])>int(elements[i + 1]) :
                    count+=1
    return count

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
    max = elements[0]
    data = [max]
    data.append(0)
    for i in range(1, len(elements)):
        if int(max_elements) < int(elements[i]):
            max = elements[i]
            data = [max]
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
    data=input().split()
    return data

def operation_data(elements):
    count=0
    for i in range(0, len(elements)-1):
        if int(elements[i]) != int(elements[i + 1]):
            count+=1
    return count

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
	elements[i*2] = elements[i*2 + 1] and elements[i*2 + 1]=elements[i*2]
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
    max = elements[0]
    min = elements[0]
    ind_min = 0
    ind_max = 0
    for i in range(0, len(elements)):
        if  int(min) > int(elements[i]):
            min = elements[i]
            ind_min = i
        if  int(max) < int(elements[i]):
            max = elements[i]
            ind_max = i
    elements[ind_min], elements[ind_max] = elements[ind_max], elements[ind_min]    
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

#task13----------------------------------------------------------- 



 """ 



 ��� ������ �����. ����������, ������� � ��� ��� ���������, ������ ���� �����. 



 ���������, ��� ����� ��� ��������, ������ ���� ����� �������� ���� ����, ������� ���������� ���������. 



 """ 



  



  



  



 result = 0 



  



 list_ = input().split() 



 for i in range (len(list_)):#��������� ������� 



  for j in range (i 1 , len(list_)):#���������� ��� ��������� �������� �������� � ������ 



  if list_[i] == list_[j]:#���������� �� 



  result  = 1 



 print( result ) 



  



 #----------------------------------------------------------------- 



  



  



 #task14----------------------------------------------------------- 



 """ 



 ��� ������. �������� �� ��� ��������, ������� ����������� � ������ ������ ���� ���. 



 �������� ����� �������� � ��� �������, � ������� ��� ����������� � ������. 



 """ 



  



  



  



 counter = 0 



 list_of_lonely_elements=[] 



  



 list_ = input() . split() 



  



 for i in range(len(list_)):#��������� ������� 



  counter = 0 # ������ �������� �������� �� ��������� 



  for j in range(len(list_)): #���������� �������� ������ 



  if (list_[i] == list_[j]) and i!=j: # ���� ������� ����� ������� � ��� �� ���� � ��� �� �������, ��: 



  counter = 1 



  if counter == 0: 



  list_of_lonely_elements.append(list_[i]) 



  



  



 for element in list_of_lonely_elements: 



  print(element, end = ' ') 



  



 #----------------------------------------------------------------- 



  



  



 #task15----------------------------------------------------------- 



 """ 



 N ������ ��������� � ���� ���, ����������� �� ����� ������� ������� �� 1 �� N. 



 ����� �� ����� ���� ������� K �����, ��� ���� i-� ��� ���� ��� ����� � �������� �� li �� ri ������������. 



 ����������, ����� ����� �������� ������ �� �����. 



 ��������� �������� �� ���� ���������� ������ N � ���������� ������� K. 



 ����� ���� K ��� ����� li, ri, ��� ���� 1? li? ri? N. 



  



 ��������� ������ ������� ������������������ �� N ��������, ��� j-� ������ ���� �I�, 



 ���� j-� ����� �������� ������, ��� �.�, ���� j-� ����� ���� �����. 



 """ 




 def form_of_list_(number): # Function which make a list 



  list_ = [] 



  list_ = ['I' for i in range(number)] 



  return(list_) 



  



  



 number, count_of_shots = input().split() 



  



 list_ = form_of_list_(int(number)) 



  



 for i in range (int(count_of_shots)): 



  start_pos, final_pos = input().split() 



  for j in range( int(start_pos)-1 , int(final_pos) ): 



  list_[j] = '.' 



  



 for element in list_: 



  print(element, end = '') 



  



 #----------------------------------------------------------------- 



  



 #task16------------------------------------------------------------ 



 """ 



 ��������, ��� �� ����� 8?8 ����� ���������� 8 ������ ���, ����� ��� �� ���� ���� �����. 



 ��� ���� ����������� 8 ������ �� �����, ����������, ���� �� ����� ��� ���� ������ ���� �����. 



 ��������� �������� �� ���� ������ ��� �����, ������ ����� �� 1 �� 8 � ���������� 8 ������. 



 ���� ����� �� ���� ���� �����, �������� ����� NO, ����� �������� YES. 



 """ 


  



  



 def form_list_(size):#this function create a new 2-D list sizeXsize (this function created by me) 



  list_ = (size * '0 ').split() 



  for i in range(len(list_)): 



  list_[i] = [] 



  list_[i] = (size * '0 ').split() 



  return list_ 



  




 def horizontal_vertical_test(list_):#this function make a test. If ion horizontal and vertical we have only 1 queen function retur 1, else 0.(created by me) 



  for i in range(len(list_)): 



  sum_of_horizontal = 0 



  sum_of_vertical = 0 



  for j in range(len(list_)): 



  sum_of_horizontal  = int(list_[i][j]) 



  sum_of_vertical  = int(list_[j][i]) 



  if sum_of_horizontal > 1 or sum_of_vertical > 1: 



  return 0 



  return 1 



  



  



 def diagonal_test(list):#this function for horizontal test(created by Anton Pidgayniy) 



  for i in range(len(list)): 



  sum1, sum2, sum3, sum4 = 0, 0, 0, 0 



  for j in range(len(list)): 



  if -1 < j - i < len(list): 



  sum1  = int(list[j - i][j]) 



  sum2  = int(list[j][j - i]) 



  sum3  = int(list[j - i][len(list) - j - 1]) 



  sum4  = int(list[len(list) - j - 1][j - i]) 



  if sum1 > 1 or sum2 > 1 or sum3 > 1 or sum4 > 1: 



  return 0 



  return 1 



  



  



 list_ = form_list_(8) 



  



 for i in range(8):# This is part of code where we read a coordinat's of Queen on the chess board(created by me) 



  i, j = input().split() 



  list_[int(i) - 1][int(j) - 1] = 1 



  



 if diagonal_test(list_) == 1 and horizontal_vertical_test(list_) == 1:#It's a part of code, where we print a result(create by Anton Pidgayniy) 



  print("NO") 



 else: 



  print("YES") 



  



 #----------------------------------------------------------------- 



  




