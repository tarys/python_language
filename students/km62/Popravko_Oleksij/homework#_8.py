#task1------------------------------------------------------------
"""
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""


n=int(input())
a=[['.' for j in range(n)] for i in range(n)]
for i in range(n):
    j=i
    a[i][j]='*'
    a[n//2][j]='*'
    a[i][n//2]='*'
    a[n-i-1][j]='*'
for i in a:
 print(' '.join([str(m) for m in i]))

#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д. 
"""


n = int(input())
a = [ [x for x in range(i,0,-1)]+[0]+[x for x in range(1,n-i)] for i in range(n)]
for row in a:
    print(' '.join([str(x) for x in row]))

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.  
"""


n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
 a[i][n - i - 1] = 1
for i in range(n):
 for j in range(n - i, n):
  a[i][j] = 2
for row in a:
 for elem in row:
  print(elem, end=' ')
print()
#-----------------------------------------------------------------




