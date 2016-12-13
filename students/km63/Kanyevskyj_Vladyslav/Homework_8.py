'''
Дано нечетное число n. Создайте двумерный массив из n×n элементов, 
заполнив его символами "." (каждый элемент массива является строкой из 
одного символа). Затем заполните символами "*" среднюю строку массива, 
средний столбец массива, главную диагональ и побочную диагональ. В 
результате единицы в массиве должны образовывать изображение звездочки. 
Выведите полученный массив на экран, разделяя элементы массива пробелами.
'''
#input
num = int(input())
#def
a = [['.'] * num for i in range(num)]
index = num//2
for i in range(len(a)):
    for j in range(len(a[i])):
        if(i==index or j == index or i == j or i == num-j-1):
            a[i][j] = '*'
#output
for lists in a:
    for elem in lists:
        print(elem,end=' ')
    print()
#-----------------------------------------------------------------------
'''
Дано число n. Создайте массив размером n×n и заполните его 
по следующему правилу. На главной диагонали должны быть записаны 
числа 0. На двух диагоналях, прилегающих к главной, числа 1. На 
следующих двух диагоналях числа 2, и т.д.
'''
#input
num = int(input())
#def
a = [[0] * num for i in range(num)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if(i == j):
            a[i][j] = 0
        for c in range(num):
            if(i == j-c or i == j+c):
                a[i][j] = c
#output
for lists in a:
    for elem in lists:
        print(elem, end=' ')
    print()
#-----------------------------------------------------------------------
'''
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
'''
#input
num = int(input())
#def
a = [[0]*num for i in range(num)]
for i in range(len(a)):
    for j in range(len(a[i])):
        if(i > num-j-1):
            a[i][j] = 2
        if(i == num-j-1):
            a[i][j] = 1
#output
for lists in a:
    for elem in lists:
        print(elem, end = ' ')
    print()
#-----------------------------------------------------------------------
