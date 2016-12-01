#task1---------------------------
"""
Задача «Максимум»
Найдите индексы первого вхождения максимального элемента.
Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.
Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.'
"""
#input---
n, m = [int(i) for i in input().split()]  #input matrix's size: n-height, m-width
matrix = [[int(i) for i in input().split()]for j in range(n)]  #create a matrix
#default-
max = matrix[0][0]
index_1 = 0
index_2 = 0
#main----
for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if max < matrix[i][j]:
			max = matrix[i][j]
			index_1 = i
			index_2 = j
#print---
print(index_1, index_2)  #print row number and column number
#--------------------------------
#task2---------------------------
"""
Задача «Снежинка»
Дано нечетное число n. Создайте двумерный массив из n×n элементов,
заполнив его символами "." (каждый элемент массива является строкой из одного символа).
Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ.
В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""
#input---
n = int(input())  #input matrix size
#main----
matrix = [['.'] * n for i in range(n)]  #create matrix filled up with '.'
for i in range(n):
	matrix[i][i] = '*'  #fill up main diagonal with '*'
	matrix[n // 2][i] = '*'  #fill up middle row with '*'
	matrix[i][n // 2] = '*'  #fill up middle column with '*'
	matrix[i][n - i - 1] = '*'  #fill up side diagonal with '*'
#print---
for row in matrix:
	print(' '.join(row))  #print matrix
#--------------------------------
#task3---------------------------
"""
Задача «Шахматная доска»
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
В левом верхнем углу должна стоять точка.
"""
#input---
n, m = [int(i) for i in input().split()]  #input n-height, m-width
#main----
matrix = [["."] * m for i in range(n)]  #create matrix filled up with '.'
for i in range(n):  #number of rows
	for j in range(m):  #number of columns
		if i % 2 == 0 and j % 2 == 0:
			matrix[i][j] = "."  #fill up odd elements of odd rows with '.'
		elif i % 2 == 1 and j % 2 == 1:
			matrix[i][j] = "."  #fill up even elements of even rows with '.'
		else:
			matrix[i][j] = "*"  #fill up everything else with '*'
#print---
for i in range(n):
	for j in range(m):
		print(matrix[i][j], end=' ')
	print()  #print final matrix
#--------------------------------
#task4---------------------------
"""
Задача «Диагонали, параллельные главной»
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1.
На следующих двух диагоналях числа 2, и т.д.
"""
#input---
n = int(input())  #input size of the matrix
#main----
matrix = [[0] * n for i in range(n)]  #create matrix filled up with '0'
for row in range(n):
	for i in range(n):
		for j in range(n):
			if i < j:
				matrix[i][j] = matrix[i + 1][j] + 1  #fill up upper diagonals with numbers
			if j < i:
				matrix[i][j] = matrix[i][j + 1] + 1  #fill up downmost diagonals with numbers
#print---
for i in range(n):
	for j in range(n):
		print(matrix[i][j], end=' ')
	print()  #print final matrix
#--------------------------------
#task5---------------------------
"""
Задача «Побочная диагональ»
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""
#input---
n = int(input())  #input size
#main----
matrix = [[0] * n for i in range(n)]  #create matrix filled up with '0'
for i in range(n):
	for j in range(n):
		matrix[i][n - i - 1] = 1  #fill up side diagonal with '1'
		if i > j:
			matrix[i][n -j - 1] = 2  #fill up space under side diagonal with '2'
#print---
for i in range(n):
	for j in range(n):
		print(matrix[i][j], end=' ')
	print()  #print final matrix
#--------------------------------
#task6---------------------------
"""
Задача «Поменять столбцы»
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
Решение оформите в виде функции swap_columns(a, i, j).
"""
def swap_columns(a, i, j):  #function to swap columns
	for k in range(n):
		a[k][j], a[k][i] = a[k][i], a[k][j]  #swap columns
	return matrix

def print_matrix(matrix):  #function to print matrix
	for row in matrix:
		for element in row:
			print(element, end = ' ')
		print()
#main----
n, m = [int(i) for i in input().split()]  #input number of rows and columns
matrix = [input().split() for i in range(n)]  #create matrix
i, j = [int(i) for i in input().split()]  #input number of rows and columns
#print---
print_matrix(swap_columns(matrix,i,j))  #print final matrix
#--------------------------------
