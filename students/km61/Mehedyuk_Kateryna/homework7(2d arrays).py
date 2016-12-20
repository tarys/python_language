#task1
Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.
matrix = input().split()
n = int(matrix[0])
m = int(matrix[1])
max_i = 0
max_j = 0
a = [[int(j) for j in input().split()] for i in range(n)]
for i in range(0, n):
     for j in range(0, m):
         if a[i][j] > a[max_i][max_j]:
             max_i = i
             max_j = j
print(max_i, max_j)
#task2
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
snow = int(input())
j,t = int(snow-1),int((snow-1)/2)
a = [['.'] * t + ['*'] + ['.'] * t for i in range(snow)]
a[t] = ['*'] * snow
for i in range(snow):
     a[i][i] = '*'
     a[j][i] = '*'
     j -= 1
for row in a:
     print(' '.join([str(elem) for elem in row]))
#task3
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
n,m=[int(i) for i in input().split()]
for i in range(n):
     for j in range(m):
         if (i+j)%2==0:
             print(".",end=" ")
         else:
             print("*",end=" ")
     print()
#task4
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
n = int(input())
a = [["."] * n for i in range(n)]
for i in range(n):
     for j in range(n):
         a[i][j] = abs(j - i)
 
for row in a:
     print(' '.join([str(elem) for elem in row]))
#task4
n = int(input())
a = [["."] * n for i in range(n)]
for i in range(n):
     for j in range(n):
         a[i][j] = abs(j - i)
 
for row in a:
     print(' '.join([str(elem) for elem in row]))
#task5
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
     a[i][(n - 1) - i] = 1
     for j in range(n - i, n):
         a[i][j] = 2
 
for row in a:
     print(' '.join([str(elem) for elem in row]))
#task6
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
for x in range(n):
     a[x][i], a[x][j] = a[x][j], a[x][i]
 
for row in a:
     print(' '.join([str(a) for a in row]))
