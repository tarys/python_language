#task1------------------------------------------------------------
"""
Даны два целых числа A и B (при этом A ≤ B). Выведите все числа 
от A до B включительно.
"""

a=int(input('Введите целое число a:'))
b=int(input('Введите целое число b:'))
for i in range(a,b+1):
    print(i)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Даны два целых числа A и В. Выведите все числа от A до B 
включительно, в порядке возрастания, если A < B, или в порядке 
убывания в противном случае.
"""

a=int(input('Введите целое число a:'))
b=int(input('Введите целое число b:'))
if a<b:
    for i in range(a,b+1):
         print(i)
else:
    for i in range(a,b-1,-1):
        print(i)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Даны два целых числа A и В, A>B.
Выведите все нечётные числа от A до B включительно.
В этой задаче можно обойтись без инструкции if.
"""

a=int(input('Введите целое число a:'))
b=int(input('Введите целое число b:'))
a -= ~a & 1
b += ~b & 1
print(" ".join([str(i) for i in range(a, b - 1 , -2)]))

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дано 10 целых чисел. Вычислите их сумму.
Напишите программу, использующую наименьшее число переменных.
"""

print(sum(int(input('Введите число:'))for i in range(10)))

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Дано несколько чисел. Вычислите их сумму.
Сначала вводите количество чисел N, затем вводится ровно N целых 
чисел.Какое наименьшее число переменных нужно для решения этой 
задачи?
"""

print(sum(int(input('Введіть число:')) for i in range(int(input('Введіть кількість цілих чисел:')))))

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
По данному натуральном n вычислите сумму 1^3+2^3+3^3+...+n^3. 
"""

s=0
n = int (input())
for i in range(i,n+1):
    s=s+i**3
print(s)

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Факториалом числа n называется произведение 1 × 2 × ... × n. 
Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться 
математической библиотекой math в этой задаче запрещено. 
"""

fac=1
n = int(input())
for i in range (1,n+1,1):
    fac = fac*i
print(fac)

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В 
решении этой задачи можно использовать только один цикл.  
Пользоваться математической библиотекой math в этой задаче 
запрещено.
"""

fac=1
summ=0
n = int (input ())
for i in range(1,n+1):
    fac=fac*i
    summ=summ+fac
print(summ)

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Дано N чисел: сначала вводится число N, затем вводится ровно N 
целых чисел. Подсчитайте количество нулей среди введенных чисел и 
выведите это количество. Вам нужно подсчитать количество чисел, 
равных нулю, а не количество цифр. 
"""

n = int (input())
kol = 0
for i in range(n):
    num = int(input())
    if num==0:
        kol+=1
print(kol)

#-----------------------------------------------------------------


#task10-----------------------------------------------------------
"""
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я 
ступенька состоит из чисел от 1 до i без пробелов. 
"""

n = int(input())
for i in range (n):
    for j in range(1,i+2):
        print(j,end='')
    print()

#-----------------------------------------------------------------
