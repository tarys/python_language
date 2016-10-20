#Задача №1 -------------------------------------------------------------
"""
По данному целому числу N распечатайте все квадраты натуральных чисел, 
не превосходящие N, в порядке возрастания.
"""



n = int(input())
i=1
while(i**2 <= n):
    print(i**2,end=' ')
    i = i + 1
#-----------------------------------------------------------------------


#Задача №2--------------------------------------------------------------
"""
Дано целое число, не меньшее 2. 
Выведите его наименьший натуральный делитель, отличный от 1.
"""



i = 2
n = int(input())
while(i <= n):
    if n%i==0:
        print(i)
        break
    i = i + 1
#-----------------------------------------------------------------------


#Задача №3--------------------------------------------------------------
"""
Задача №3 
По данному натуральному числу N найдите наибольшую целую степень двойки, 
не превосходящую N. Выведите показатель степени и саму степень.

Операцией возведения в степень пользоваться нельзя!
"""



n = int(input())
i = 1
p = 2
while(p <= n):
    if(p*2 <= n):
        p *= 2
        i = i + 1
    else:
        break
print(i,p)

#-----------------------------------------------------------------------


#Задача №4--------------------------------------------------------------
"""
ДВ первый день спортсмен пробежал x километров, а затем он каждый день 
увеличивал пробег на 10% от предыдущего значения. По данному числу y 
определите номер дня, на который пробег спортсмена составит не менее y 
километров.

Программа получает на вход действительные числа x и y и должна вывести 
одно натуральное число.
"""



x = int(input())
y = int(input())
counter = 0
while(x < y):
    counter +=1
    x += x*0.1
print(counter+1)

#-----------------------------------------------------------------------


#Задача №5--------------------------------------------------------------
"""
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p 
процентов, после чего дробная часть копеек отбрасывается. Определите, 
через сколько лет вклад составит не менее y рублей.

Выражение «дробная часть копеек отбрасывается» означает, что если у вас 
оказалось 123.4567 рублей, т. е. 123 рубля и 45.67 копеек, то после 
округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.

Программа получает на вход три натуральных числа: x, p, y и должна 
вывести одно целое число.
"""



x=float(input())
p=int(input())
y=int(input())

i=0
while x<y:
    x=x+x*p/100
    x=float(int(x*100))/100
    i+=1
print(i)

#-----------------------------------------------------------------------


#Задача №6--------------------------------------------------------------
"""
Программа получает на вход последовательность целых неотрицательных 
чисел, каждое число записано в отдельной строке. Последовательность 
завершается числом 0, при считывании которого программа должна закончить 
свою работу и вывести количество членов последовательности (не считая 
завершающего числа 0). Числа, следующие за числом 0, считывать не нужно.


"""



counter = 0
while(int(input()) != 0):
    counter += 1
else:
    print(counter)

#-----------------------------------------------------------------------


#Задача №7--------------------------------------------------------------
"""
Определите сумму всех элементов последовательности, завершающейся 
числом 0. В этой и во всех следующих задачах числа, следующие за первым 
нулем, учитывать не нужно.
"""



counter = 0
while True:
    x = int(input())
    if(x == 0):
        break    
    else:    
        counter += x;
print(counter)
#-----------------------------------------------------------------------


#Задача №8--------------------------------------------------------------
"""
Определите среднее значение всех элементов последовательности, 
завершающейся числом 0.
"""



sum = 0;
counter = 0;
while True:
    x = int(input())
    if(x != 0):
        sum += x
        counter += 1
    else:
        break
print(sum/counter)

#-----------------------------------------------------------------------


#Задача №9--------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите значение наибольшего элемента последовательности.
"""



max = 0
while True:
    x = int(input())
    if(x != 0):
       if(max < x):
           max = x
    else:
        break
print(max)

#-----------------------------------------------------------------------

#Задача №10-------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите индекс наибольшего элемента последовательности. Если 
наибольших элементов несколько, выведите индекс первого из них. 
Нумерация элементов начинается с нуля.
"""



max = 0
counter = 0
maxcounter = 0
while True:
    x = int(input())
    if(x != 0):
        counter += 1
        if(max < x):
           max = x
           maxcounter = counter
    else:
        break
print(maxcounter-1)
#-----------------------------------------------------------------------

#Задача №11-------------------------------------------------------------
"""
Определите количество четных элементов в последовательности, 
завершающейся числом 0.
"""



counter = 0
while True:
    x = int(input())
    if(x != 0):
       if(x % 2 == 0):
           counter += 1
    else:
        break
print(counter)

#-----------------------------------------------------------------------

#Задача №12-------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите, сколько элементов этой последовательности больше предыдущего 
элемента.
"""



counter = 0
prev = 0
while True:
    n = int(input())
    if(n != 0):
        if(n > prev):
            prev = n
            counter += 1
        else:
            prev = n
    else:
        break
print(counter-1)

#-----------------------------------------------------------------------
#Задача №13-------------------------------------------------------------
"""
Последовательность состоит из различных натуральных чисел и завершается 
числом 0. Определите значение второго по величине элемента в этой 
последовательности. Гарантируется, что в последовательности есть хотя 
бы два элемента.
"""



max = 0
notmax = 0
while True:
    n = int(input())
    if(n != 0):
        if(n > max):
            notmax = max
            max = n
        if(n > notmax and n < max):
            notmax = n
    else:
        break
print(notmax)

#-----------------------------------------------------------------------
#Задача №14-------------------------------------------------------------
"""
Последовательность состоит из натуральных чисел и завершается числом 0. 
Определите, сколько элементов этой последовательности равны ее 
наибольшему элементу.
"""



counter = 1
max = 0
while True:
    n = int(input())
    if(n != 0):
        if(n == max):
            counter += 1
        if(max < n):
            counter = 1
            max = n
    else:
        break
print(counter)

#-----------------------------------------------------------------------
#Задача №15-------------------------------------------------------------
"""
Определите количество четных элементов в последовательности, 
завершающейся числом 0.
"""



counter = 0
while True:
    x = int(input())
    if(x != 0):
       if(x % 2 == 0):
           counter += 1
    else:
        break
print(counter)

#-----------------------------------------------------------------------

#Задача №18-------------------------------------------------------------
"""
Дана последовательность натуральных чисел x1x1, x2x2, ..., xnxn. Стандартным отклонением называется величина
σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾√
σ=(x1−s)2+(x2−s)2+…+(xn−s)2n−1
где s=x1+x2+…+xnns=x1+x2+…+xnn — среднее арифметическое последовательности.

Определите стандартное отклонение для данной последовательности натуральных чисел, завершающейся числом 0.
"""



import math
variables = []
sm = 0
ssq = 0
while True:
    n = int(input())
    if(n==0):
        break;
    variables.append(n)
for i in range(len(variables)):
    sm+=variables[i-1]
s = sm/len(variables)
for i in range(len(variables)):
    ssq += (variables[i]-s)**2
divis = ssq/(len(variables)-1)
answer = math.sqrt(divis)
print(answer)
#-----------------------------------------------------------------------
