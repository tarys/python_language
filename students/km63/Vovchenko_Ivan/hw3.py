#task1------------------------------------------------------------
"""
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
"""
a=int(input())
s=1
for i in range(1,a+1):
    s=s*i
print(s)
#-----------------------------------------------------------------
#task2------------------------------------------------------------
"""
По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл.
Пользоваться математической библиотекой math в этой задаче запрещено.
"""
factorial=1
suma=0
n=int(input())
for i in range(n):
    factorial*=(i+1)
    suma+=factorial
print(suma)
#-----------------------------------------------------------------
#task3------------------------------------------------------------
"""
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
Подсчитайте количество нулей среди введенных чисел и выведите это количество.
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
"""
n=int(input())
suma=0
for i in range(n):
    if int(input())==0:
        suma+=1
print(suma)
#-----------------------------------------------------------------
#task4------------------------------------------------------------
"""
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
"""
#This program very large, but very fast!
i=int(input())
if i==1:
    print(1)
if i==2:
    print(1)
    print(12)
if i==3:
    print(1)
    print(12)
    print(123)
if i==4:
    print(1)
    print(12)
    print(123)
    print(1234)
if i==5:
    print(1)
    print(12)
    print(123)
    print(1234)
    print(12345)
if i==6:
    print(1)
    print(12)
    print(123)
    print(1234)
    print(12345)
    print(123456)
if i==7:
    print(1)
    print(12)
    print(123)
    print(1234)
    print(12345)
    print(123456)
    print(1234567)
if i==8:
    print(1)
    print(12)
    print(123)
    print(1234)
    print(12345)
    print(123456)
    print(1234567)
    print(12345678)
if i==9:
    print(1)
    print(12)
    print(123)
    print(1234)
    print(12345)
    print(123456)
    print(1234567)
    print(12345678)
    print(123456789)
#-----------------------------------------------------------------


