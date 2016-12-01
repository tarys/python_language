#task1------------------------------------------------------------
"""
Найдите индексы первого вхождения максимального элемента. 
Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. 
Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""

from random import random

print('Matrix will be filled by random elements from 0 to 100')
width = int(input('Enter width of matrix '))
height = int(input('Enter height of matrix '))

array = []



for i in range(height):
	b = []
	for j in range(width):
		a = int(random() * 100)
		b.append(a)
	array.append(b)


		

print('-------------------------------------------------------')


max_i = [0, 0]
max_element = 0

for i in range(height):
	for j in range(width):
		if array[i][j] > max_element:
			max_element = array[i][j]
			max_i[0] = i
			max_i[1] = j

print('Element with indexes ', max_i[0], ',', max_i[1], ' (', max_element, ') is the largest')			

#task2------------------------------------------------------------
"""
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа). 
Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. 
В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.""

"""

n = int(input('Enter side of matrix '))

if n % 2 == 0:
	print('invalid')
	exit(0)

array = []

def output(array):
	for i in range(len(array)):
		for j in range(len(array[i])):
			print(array[i][j], end = '  ')
		print('\n')	

for i in range(n):
	b = []
	for j in range(n):
		a = '.'
		b.append(a)
	array.append(b)


for i in range(n):
	for j in range(n):
		if (j == n // 2) or (i == n // 2) or (i == j) or (i + j == n - 1):
			array[i][j] = '*'

output(array)

#task3------------------------------------------------------------
"""
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. 
В левом верхнем углу должна стоять точка.
"""

width = int(input('Enter width of matrix '))
height = int(input('Enter height of matrix '))

array = []

def output(array):
	for i in range(len(array)):
		for j in range(len(array[i])):
			print(array[i][j], end = '  ')
		print('\n')	

for i in range(height):
	b = []
	for j in range(width):
		a = '.'
		b.append(a)
	array.append(b)

		


for i in range(width):
	if i %	2 == 1:
		array[0][i] = '*'

for i in range(1, height):
	for j in range(width):
		if array[i - 1][j] == '.':
			array[i][j] = '*'



output(array)		

#task4------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. 
На следующих двух диагоналях числа 2, и т.д.
"""

n = int(input('Enter the size of a matrix '))
array = []

def output(array):
	for i in range(len(array)):
		for j in range(len(array[i])):
			print(array[i][j], end = '   ')
		print('\n')	

for i in range(n):
	b = []
	for j in range(n):
		a = 0
		b.append(a)
	array.append(b)

for k in range(1, n):
    for i in range(n - k):
        for j in range(n - k):
            if i == j:
                array[i][j + k] = k 
                array[i + k][j] = k

output(array)

#Can`t figure out how to do like 3332210122333, so I did it like 432101234. Really need your hint :)

#task5------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""

n = int(input('Enter the size of a matrix '))
array = [0] * n

def output(array):
	for i in range(len(array)):
		for j in range(len(array[i])):
			print(array[i][j], end = '   ')
		print('\n')	

for i in range(n):
    array[i] = [0] * (n - i - 1) + [1] + [2] * i

output(array)   

#task6------------------------------------------------------------
"""
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.

Решение оформите в виде функции swap_columns(a, i, j).
"""

