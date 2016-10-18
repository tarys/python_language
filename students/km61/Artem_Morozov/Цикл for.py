#task1------------------------------------------------------------
"""
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
"""
#Program calculates factorial of number n 
n=int(input('Enter number'))
factorial=1
for i in range(n):
    factorial*=i+1
print('N!=',sum)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!.
Пользоваться математической библиотекой math в этой задаче запрещено.

"""
#Program calculates sum of the factorials from 1 to n
n=int(input('Enter number'))
sum=0
for i in range(n):
    fact=1
    for j in range(i+1):
        factorial*=j+1
    sum+=factorial
print('Sum of factorials from 1 to',n,'=',sum)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
 Подсчитайте количество нулей среди введенных чисел и выведите это количество. 
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
"""
#Program prints amount of zeros entered by user
n=int(input('Enter amount of numbers'))
amount=0
for i in range(n):
    x=int(input('Enter number'))
    if x==0:
        amount+=1
print('Amount of zeros',amount)

#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
"""
#Program prints "ladder" of numbers 
n=int(input('Enter amount of stairs'))
print('Ladder')
for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    print()

#-----------------------------------------------------------------