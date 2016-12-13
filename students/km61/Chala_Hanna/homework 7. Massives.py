'''
Task 1
Найдите индексы первого вхождения максимального элемента. 
Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. 
Если таких элементов несколько, то выводится тот, у которого меньше номер строки, 
а если номера строк равны то тот, у которого меньше номер столбца.
'''
n, m = [int(i) for i in input().split()]

a = [[int(i) for i in input().split()] for j in range(n)]

max = a[0][0]
index_i = 0
index_j = 0
for i in range(n):
    for j in range(m):
        if a[i][j]>max:
            max = a[i][j]
            index_i = i
            index_j = j
print (index_i, index_j)


'''
Task 2
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа). 
Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. 
В результате единицы в массиве должны образовывать изображение звездочки. 
Выведите полученный массив на экран, разделяя элементы массива пробелами.
'''
n = int(input()) 

a = [['.' for i in range(n)] for j in range(n)] 

for i in range (n): 
    for j in range (n): 
        if (i==j) or (i==(n-j)-1) or (j==n//2) or (i==n//2): 
            a[i][j] = '*' 
        else: 
            a [i][j] = '.' 

for i in range (n): 
    for j in range (n): 
        print (a[i][j], end =' ') 
print ()


'''
Task 3
Даны два числа n и m. Создайте двумерный массив размером n×m 
и заполните его символами "." и "*" в шахматном порядке. 
В левом верхнем углу должна стоять точка.
'''
n, m = [int(i) for i in input().split()]

a = [['.' for j in range(m)] for i in range(n)] 

for i in range (n): 
    for j in range (m): 
        if ((i%2!=0) and (j%2!=0)) or ((i%2==0) and (j%2==0)): 
            a[i][j] = '.' 
        else: 
            a [i][j] = '*' 

for i in range (n): 
    for j in range (m): 
        print (a[i][j], end =' ') 
    print ()

	
	
'''
Task 4
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. 
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. 
На следующих двух диагоналях числа 2, и т.д.
'''
n = int(input()) 

a = [['.' for i in range(n)] for j in range(n)] 
for i in range (n): 
    for j in range (n): 
        a[i][j] = abs(i-j)
        
for i in range (n): 
    for j in range (n): 
        print (a[i][j], end =' ') 
    print ()

	
	
'''
Task 5
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
'''
n = int(input()) 

a = [['.' for i in range(n)] for j in range(n)] 
for i in range (n): 
    for j in range (n): 
        if i==(n-j)-1:
            a[i][j] = 1
        elif i<(n-j)-1:
            a[i][j] = 0
        else:
            a[i][j] = 2
        
for i in range (n): 
    for j in range (n): 
        print (a[i][j], end =' ') 
    print ()
	
	
'''
Task 6
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.

Решение оформите в виде функции swap_columns(a, i, j).
'''
n,m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]
i,j = [int(i) for i in input().split()]
def swap_columns(a, i, j):
    for x in range (len(a)):
        a[x][i], a[x][j] = a[x][j], a[x][i]
swap_columns(a, i,j)
for i in range (n): 
    for j in range (m): 
        print (a[i][j], end =' ') 
    print ()	


