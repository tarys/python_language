﻿#task1------------------------------------------------------------
"""
Даны два целых числа A и B (при этом A ? B). Выведите все числа от A до B включительно.
"""
A=int(input())
B=int(input())
for i in range(A, B+1, 1):
    print(i)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.
"""
A=int(input())
B=int(input())
if B>A:
    for i in range(A, B+1, 1):
        print(i)
else:
    for i in range(A+1, B-1, -1):
        print(i)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Даны два целых числа A и В, A>BA>B. Выведите все нечётные числа от A до B включительно. В этой задаче можно обойтись без инструкции if.
"""
A=int(input())
B=int(input())
for i in range(B, A+1, 2):
    print(i)

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.
"""
sum=0
for i in range(1,11,1):
    n=int(input())
    sum+=n
print(sum)

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел. 
Какое наименьшее число переменных нужно для решения этой задачи?
"""
n=int(input())
sum=0
for i in range(1,11,1):
    n=int(input())
    sum+=n
print(sum)

#-----------------------------------------------------------------

#task6------------------------------------------------------------
"""
По данному натуральном n вычислите сумму 1**3+2**3+3**3+...+n3.
"""
sum = 0
n = int(input())
for i in range(1, n + 1):
    sum += i**3
print(sum)

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Факториалом числа n называется произведение 1 ? 2 ? ... ? n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.

"""
sum = 1
n = int(input())
for i in range(1, n + 1):
    sum *= i
print(sum)

#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
По данному натуральному n ? 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
"""
n = int(input())
if n<=9:
    for i in range(n):
        for j in range(1, i+2):
            print(j, end='')
        print()
else:
    print('wrong n')

#-----------------------------------------------------------------

