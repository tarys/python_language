#TASK_1------------------------------------------------------------------------
'''

	Найдите индексы первого вхождения максимального элемента.
 	Выведите два числа: номер строки и номер столбца, в 
	которых стоит наибольший элемент в двумерном массиве. 
	Если таких элементов несколько, то выводится тот, у 
	которого меньше номер строки, а если номера строк равны 
	то тот, у которого меньше номер столбца.
	Программа получает на вход размеры массива n и m, затем 
	n строк по m чисел в каждой.
'''

raw_inp=input().split(' ')
n = int(raw_inp[0]); m = int(raw_inp[1])
line = [input() for i in range(n)]
mas = (' '.join(line)).split()
mas = [int(i) for i in mas]
print(((mas.index(max(mas)))//m), (mas.index(max(mas)))//n)
#------------------------------------------------------------------------------

#TASK_2------------------------------------------------------------------------
'''

Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его 
символами "." (каждый элемент массива является строкой из одного символа). Затем
заполните символами "*" среднюю строку массива, средний столбец массива, главную
диагональ и побочную диагональ. В результате единицы в массиве должны 
образовывать изображение звездочки. Выведите полученный массив на экран, 
разделяя элементы массива пробелами.
'''

size = int(input())
matrix = [['.'] * size for i in range(size)]
for i in range(size):
    matrix[i][i] = '*'
    matrix[size // 2][i] = '*'
    matrix[i][size // 2] = '*'
    matrix[i][size - i - 1] = '*'
for row in matrix:
    print(' '.join(row))
#------------------------------------------------------------------------------

#TASK_3------------------------------------------------------------------------
'''

Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его си
мволами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
'''

raw = input().split()
n = int(raw[0]); m = int(raw[1])
mas = [(".*."[1-(i%2):2-(i%2)+1])*(m//2) for i in range(1,n+1)]
for row in mas:
    print(' '.join(row))

#-----------------------------------------------------------------------------


#TASK_4------------------------------------------------------------------------
'''

Дано число n. Создайте массив размером n×n и заполните его по следующему правилу
На главной диагонали должны быть записаны числа 0. На двух диагоналях, 
прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
'''

n = int(input())
matrix = [[abs(i - j) for j in range(n)] for i in range(n)]
for row in matrix:
    print(' '.join([str(i) for i in row]))
#-----------------------------------------------------------------------------


#TASK_5------------------------------------------------------------------------
'''

Дано число n. Создайте массив размером n×n и заполните его по следующему 
правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
'''

def func(i,j,n):
    if i+j+1==n: return 1
    elif i+j+1>n: return 2
    else: return 0
        
n = int(input())
matrix = [[func(i,j,n) for j in range(n)] for i in range(n)]
for row in matrix:
    print(' '.join([str(i) for i in row]))
#------------------------------------------------------------------------------

#TASK_6------------------------------------------------------------------------
'''

Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами
i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем элементы массива, затем 
числа i и j.
Решение оформите в виде функции swap_columns(a, i, j).
'''

def swap_colums(matrix, i, j):
    for raw in range(len(matrix)):
        matrix[raw][i], matrix[raw][j] = matrix[raw][j], matrix[raw][i]
    return matrix
raw = input().split(); n=int(raw[0]); m=int(raw[1])
matrix = [input().split() for i in range(n)]
raw = input().split(); c1=int(raw[0]); c2=int(raw[1])
matrix = swap_colums(matrix, c1, c2)
for raw in matrix:
    print(' '.join([str(i) for i in raw]))
#--------------------------------------------------------------------------------
