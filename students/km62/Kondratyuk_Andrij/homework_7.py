﻿# -*- coding: utf-8 -*-

#task1------------------------------------------------------------
"""
Задача «Максимум»
Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
""" 
n, m = [int(i) for i in input().split()]

a = [[int(j) for j in input().split()] for i in range(n)]

maximum = a[0][0]    

index_i = 0

index_j = 0

for i in range(len(a)):
    
    for j in range(len(a[i])):
        
	if maximum < a[i][j]:
            
	    maximum = a[i][j]
            
	    index_i=i
            
	    index_j=j

print(index_i,index_j)   
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Задача «Снежинка»
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
""" 
n = int(input())

a = [ ['.'] * n for i in range(n)]

for i in range(n):
    
    for j in range(n):
        
	if (i == j) or (n//2 == i) or (n//2 == j) or (n - j) == (i + 1):
            
	    a[i][j] = '*'
        
	else:
            
	    a[i][j] = '.'

for i in range(n):
    
    for j in range(n):
        
	print(a[i][j], end = ' ')
    
    print()
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Задача «Шахматная доска»
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
""" 
n, m = [int(i) for i in input().split()]

a = [['.'] * m for i in range(n)]

for i in range(n):
    
    for j in range(m):
        
	if (i % 2 == 0) and (j % 2 == 0):
            
	    a[i][j] = '.'
        
	elif (i % 2 == 1) and (j % 2 == 1):
            
	    a[i][j] = '.'
        
	else:
            
	    a[i][j] = '*'

for row in a:
    
    print(' '.join(row))
#----------------------------------------------------------------- 


#task4------------------------------------------------------------
"""
Задача «Диагонали, параллельные главной»
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
""" 
n = int(input())

a = [[abs(i - j) for j in range(n)] for i in range(n)]

for row in a:
    
    print(' '.join([str(i) for i in row]))
#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Задача «Побочная диагональ»
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
""" 
n = int(input())

a = [[0] * n for i in range(n)]

for i in range(n):
    
    for j in range(n):
        
	if i > j:
            
	    a[i][n-j-1] = 2
        
	else:
            
	    a[i][n-i-1] = 1

for row in a:
    
    print(' '.join([str(elem) for elem in row]))
#-----------------------------------------------------------------