#task1------------------------------------------------------------
"""
Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.
Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""


#default
massive=[]
maxweight=0
maxheight=0
#input blok
height,weight = input().split()

for i in range(int(height)):
    massive.append(input().split())
    
for i in range(int(height)):
    for j in range(int(weight)):
        if int(massive[i][j])>int(massive[maxheight][maxweight]):
            maxheight=i
            maxweight=j
print(maxheight,maxweight)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Дано нечетное число n. Создайте двумерный массив из n?n элементов,
заполнив его символами "." (каждый элемент массива является строкой из одного символа).
Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ.
В результате единицы в массиве должны образовывать изображение звездочки.
Выведите полученный массив на экран, разделяя элементы массива пробелами. 
"""



number = int(input())

list_=[['.'] * number for i in range(number)]
for i in range(number):
    for j in range(number):
        if i == ( number // 2 ) :
            list_[i][j]='*'
        if j == ( number // 2 ) :
            list_[i][j]='*'
        if i==j:
            list_[i][j]='*'
        if (i+j)==number-1:
            list_[i][j]='*'
            
for i in range(number):
    print()
    for j in range(number):
        print(list_[i][j],end=' ')

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Даны два числа n и m. Создайте двумерный массив размером n?m
и заполните его символами "." и "*" в шахматном порядке.
В левом верхнем углу должна стоять точка.
"""



def list_create(n,m,list_):
    for i in range(int(n)):
        list_.append(('. '*int(m)).split())
    return list_
#default
list_=[]
#input
n,m=input().split()
#main  
list_=list_create(n,m,list_)

for i in range(int(n)):
        if i%2!=0:
            for j in range(0,int(m),2):
                list_[i][j]='*'
        else:
            for j in range(1,int(m),2):
                list_[i][j]='*'
#print
for i in range(int(n)):
    if i!=0:
        print()
    for j in range(int(m)):
        print(list_[i][j],end=' ')

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дано число n. Создайте массив размером n?n и заполните его по следующему правилу.
На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1.
На следующих двух диагоналях числа 2, и т.д. 
"""



def print_array(array):
    for str in array:
        print()
        for elem in str:
            print(elem,end=' ')
n=int(input())

array=[[0] * n for i in range(n)]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i<j:
                array[i][j]=array[i+1][j]+1
            if j<i:
                array[i][j]=array[i][j+1]+1
print_array(array)

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Дано число n. Создайте массив размером n?n и заполните его по следующему правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""



def create_list(n,list_):
    for i in range(n):
        list_.append(('0 '*n).split())
    return(list_)
#default
list_=[]
#input
n=int(input())
#main
list_=create_list(n,list_)

for i in range(n):
    for j in range(n):
        if i+j==n-1:
            list_[i][j]=1
        if i+j>n-1:
            list_[i][j]=2
#print          
for i in range(n):
    if i!=0:
        print()
    for j in range(n):
        print(list_[i][j], end=' ')

#-----------------------------------------------------------------

 
#task6------------------------------------------------------------
"""
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.
Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.
Решение оформите в виде функции swap_columns(a, i, j). 
"""



def swap_columns(a, i, j):
    for k in range(n):
        a[k][j],a[k][i]=a[k][i],a[k][j]
    return a
def print_array(array):
    for str in array:
        print()
        for elem in str:
            print(elem,end=' ')
n,m=input().split()
n,m=int(n),int(m)
array=[input().split() for i in range(n)]
i,j=input().split()
i,j=int(i),int(j)
print_array(swap_columns(array,i,j))

#-----------------------------------------------------------------