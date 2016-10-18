#task1------------------------------------------------------------
"""
Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
"""
#Program prints numbers from a to b(a>b)
a = int(input('Enter range start'))
b = int(input('Enter range end'))
print('Numbers from',a, 'to', b)
for i in range(a, b + 1):
    print(i)





#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Даны два целых числа A и В. 
Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.

"""
#Program prints numbers from a to b or from b to a
a = int(input('Enter range start'))
b = int(input('Enter range end'))
print('Numbers from', a, 'to', b)
if a <= b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a ,b - 1, - 1):
        print(i)


#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Даны два целых числа A и В, A>BA>B. Выведите все нечётные числа от A до B включительно. В этой задаче можно обойтись без инструкции if.
"""
#Program prints odd numbers from a to b 
a = int(input('Enter range start'))
b = int(input('Enter range end'))
print('Numbers from', a, 'to', b)
for i in range(a, b - 1, - 1):
    if i % 2 != 0:
        print(i)

#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.
"""

#Program calculates sum of 10 numbers entered by user
sum = 0
for i in range(10):
    sum += int(input('Enter number'))
print('Sum of 10 number:', sum)



#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Дано несколько чисел. Вычислите их сумму. 
Сначала вводите количество чисел N, затем вводится ровно N целых чисел. 
Какое наименьшее число переменных нужно для решения этой задачи?

"""
#Program calculates sum of n numbers entered by user
sum = 0
n = int(input('Enter amount of numbers'))
for i in range(n):
    sum += int(input('Enter number'))
print('Sum of n numbers:', sum)


#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
По данному натуральном n вычислите сумму 13+23+33+...+n3.
"""
#Program calculates sum of cubes from 1 to n 
sum = 0
n=int(input('Enter amount of numbers'))
for i in range(n + 1):
    sum += i ** 3
print('Sum of cubes from 1 to', n, ':', sum)

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Факториалом числа n называется произведение 1 × 2 × ... × n. 
Обозначение: n!.
По данному натуральному n вычислите значение n!. 
Пользоваться математической библиотекой math в этой задаче запрещено.
"""

#Program calculates factorial of number n 
n = int(input('Enter number'))
factorial = 1
for i in range(n):
    factorial *= i + 1
print('N! = ', sum)



#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!. 
В решении этой задачи можно использовать только один цикл.
Пользоваться математической библиотекой math в этой задаче запрещено.



"""

#Program prints amount of zeros entered by user
n = int(input('Enter amount of numbers'))
amount = 0
for i in range(n):
    x = int(input('Enter number'))
    if x == 0:
        amount += 1
print('Amount of zeros', amount)


#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. 
Подсчитайте количество нулей среди введенных чисел и выведите это количество. 
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
"""
#Program calculates sum of the factorials from 1 to n
n = int(input('Enter number'))
sum = 0
for i in range(n):
    fact=1
    for j in range(i+1):
        factorial*=j+1
    sum += factorial
print('Sum of factorials from 1 to', n, '=', sum)


#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
"""

#Program prints some "ladder" of numbers 
n = int(input('Enter amount of stairs'))
print('Ladder')
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end ='')
    print()


#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Для настольной игры используются карточки с номерами от 1 до N. 
Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). 
Программа должна вывести номер потерянной карточки.
Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
"""

#Program prints number of lost card and numbers on cards must be from 1 to n
n = int(input('Enter amount of cards'))
sum = 0 
needed_sum = 0
for i in range(n-1):
    sum += int(input('Enter number on card from 1 to n, without duplicates:'))
    needed_sum += i + 1
needed_sum += n
print('Lost card', needed_sum - sum)

#-----------------------------------------------------------------
