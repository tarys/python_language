# -*- coding: utf-8 -*-

"""
    Домашня робота №7
    Тема: "2d_array"
    Студент: Козирєв Антон Юрійович
    Група: КМ - 62
"""

from math import fabs

#Task_1----------------------------------------------------#

"""
    Условие
    Найдите индексы первого вхождения максимального элемента.
    Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
    Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.
    Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""

List2D = []
Var_List = input().split()
Var_N = int(Var_List[0])
Var_M = int(Var_List[1])
Break = False
Value = 0

for i in range(Var_N):
    List2D.append([int(j) for j in input().split()])

Maximal_element = int(List2D[0][0]) #Set as neutral element

for i in range(Var_N):
    for j in range(Var_M):
        if Maximal_element <= int(List2D[i][j]):
            Maximal_element = int(List2D[i][j])

for i in range(Var_N):
    if Break:
        break
    for j in range(Var_M):
        if Break:
            break
        Value = int(List2D[i][j])
        if Value == Maximal_element:
            print(i, j)
            Break = True
#----------------------------------------------------------#

#Task_2----------------------------------------------------#

"""
    Условие
    Дано нечетное число n.
    Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа).
    Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ.
    В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""

def place_element_at(field, row, column, distance, symbol):
    if (row == column) or ((distance - column - 1) == row) or ((distance - 1) // 2 == row) or ((distance - 1) // 2 == column):
        field[row][column] = symbol
    return field
    

Distance = int(input())
void = '.'
star = '*'
Field = [void] * Distance

for i in range(Distance):
    Field[i] = [void] * Distance
    
for i in range(Distance):
    for j in range(Distance):
        Field = place_element_at(Field, i, j, Distance, star)
        
for Row in Field:
    print(' '.join([str(element) for element in Row]))

#----------------------------------------------------------#

#Task_3----------------------------------------------------#

"""
    Условие
    Даны два числа n и m.
    Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
    В левом верхнем углу должна стоять точка.
"""

def place_element_at(field, row, column, symbol):
    if ((row % 2 == 0) and (column % 2 == 1)) or ((row % 2 == 1) and (column % 2 == 0)):
        field[row][column] = symbol
    return field

Value_List = input().split()
Desk_Row = int(Value_List[0])
Desk_Column = int(Value_List[1])

void = '.'
star = '*'
Field = [void] * Desk_Row

for i in range(Desk_Row):
    Field[i] = [void] * Desk_Column
    
for i in range(Desk_Row):
    for j in range(Desk_Column):
        Field = place_element_at(Field, i, j, star)
        
for Row in Field:
    print(' '.join([str(element) for element in Row]))

#----------------------------------------------------------#

#Task_4----------------------------------------------------#

"""
    Условие
    Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
    На главной диагонали должны быть записаны числа 0.
    На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
"""

def place_element_at(field, row, column):
    field[row][column] = int(fabs(row - column))
    return field
    
    

Value_N = int(input())

Field = [' '] * Value_N

for i in range(Value_N):
    Field[i] = [' '] * Value_N
    
for i in range(Value_N):
    for j in range(Value_N):
        Field = place_element_at(Field, i, j)
        
for Row in Field:
    print(' '.join([str(element) for element in Row]))

#----------------------------------------------------------#

#Task_5----------------------------------------------------#

"""
    Условие
    Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
    Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
    Числа, стоящие выше этой диагонали, равны 0.
    Числа, стоящие ниже этой диагонали, равны 2.
    Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""

def place_element_at(field, row, column, distance):
    if distance - 1 - column == row:
        field[row][column] = 1
    elif fabs(distance - 1 - column) > row:
        field[row][column] = 0
    else:
        field[row][column] = 2
    return field


Value_N = int(input())

Field = [' '] * Value_N

for i in range(Value_N):
    Field[i] = [' '] * Value_N
    
for i in range(Value_N):
    for j in range(Value_N):
        Field = place_element_at(Field, i, j, Value_N)
        
for Row in Field:
    print(' '.join([str(element) for element in Row]))

#----------------------------------------------------------#

#Task_6----------------------------------------------------#

"""
    Условие
    Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
    Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
    Решение оформите в виде функции swap_columns(a, i, j).
"""

def swap_columns(field, row, column1, column2):
    for i in range(row):
        Swap_element = field[i][column1]
        field[i][column1] = field[i][column2] 
        field[i][column2] = Swap_element
    return field
    
    
List_Value = input().split()
Row = int(List_Value[0])
Column = int(List_Value[1])
Field = []
        
for i in range(Row):
    Temporary_List = input().split()
    for i in range(Column):
        Temporary_List[i] = int(Temporary_List[i])
    Field.append(Temporary_List)
        
 
List_Swap = input().split()
Swap_Column1 = int(List_Swap[0])
Swap_Column2 = int(List_Swap[1])

Field = swap_columns(Field, Row, Swap_Column1, Swap_Column2)
        
for Row in Field:
    print(' '.join([str(element) for element in Row]))

#----------------------------------------------------------#