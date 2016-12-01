#task1--------------------------
"""
Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""
size = [int(s) for s in input().split()]
vector = []
for i in range (int(size[0])):
    row = input().split()
    for i in range (len(row)):
        row[i] = int(row[i])
    vector.append(row)
index_i = 0
index_j = 0
max_element = vector[0][0]
for i in range (len(vector)):
    for j in range (len(vector[i])):
        if max_element < vector[i][j]:
            max_element = vector[i][j]
            index_i = i
            index_j = j
print(index_i, index_j)
#-------------------------------
#task2--------------------------
"""
Дано нечетное число n. Создайте двумерный массив из n?n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""
n = int(input())
vector = [['.'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            vector[i][j] = '*'
        elif i == n//2 :
            vector[i][j] = '*'
        elif j == n//2 :
            vector[i][j] = '*'
        elif j == n - i - 1:
            vector[i][j] = '*'
for i in range(n):
    for j in range(n):
        print(vector[i][j], end=' ')            
print()





#-------------------------------
#task3--------------------------
"""
Даны два числа n и m. Создайте двумерный массив размером n?m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.


"""


data = input().split()
matrix = []
matrix = [['.'] * int(data[1]) for i in range(int(data[0]))]

for i in range(int(data[0])):
    for j in range(int(data[1])):
        if (i + j) % 2 == 1:
            matrix[i][j] = '*'
for i in range(int(data[0])):
    for j in range(int(data[1])):
        print(matrix[i][j], end=' ')            
    print()



#-------------------------------
#task4--------------------------
"""
Дано число n. Создайте массив размером n?n и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
"""
size = int(input())
matrix = [0] * size
for i in range(size):
    matrix[i] = [0] * size
for k in range(1, size):
    for i in range(size-k):
        for j in range(size-k):
            if i == j:
                matrix[i][j+k] = k
                matrix[i+k][j] = k
for i in range(size):
    for j in range(size):
        print(matrix[i][j], end=' ')
    print()
#-------------------------------
#task5--------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.


"""
size = int(input())
matrix = [[0] * size for i in range(size)]
for i in range(size):
    matrix[i][size - i - 1] = 1
for i in range(size):
    for j in range(size - i, size):
        matrix[i][j] = 2
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
#-------------------------------
#task6--------------------------
"""
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.

Решение оформите в виде функции swap_columns(a, i, j).
"""
def swap_columns(matrix, i, j):
    for z in range (a):
        buf=matrix[z][i]
        matrix[z][i]=matrix[z][j]
        matrix[z][j]=buf
    return
size = input().split()
a=int(size[0])
b=int(size[1])
matrix = []
for k in range(a):
    row = input().split()
    for k in range(len(row)):
        row[k] = int(row[k])
    matrix.append(row)
size = input().split()
i=int(size[0])
j=int(size[1])
swap_columns(matrix, i, j)
for i in range(a):
    for j in range(b):
        print(matrix[i][j], end=' ')
    print()
#-------------------------------
