'''Домашня робота №3
task 1
'''
'''
Ряд - 1
Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
'''
# A programme, which prints all integer numbers from the first to the second.
# Input 2 integer numbers:
num1=int(input())
num2=int(input())
''' counting all numbers between the first and the second plus one, 
as the cycle “for” doesn`t take into account the last number. 
''' 
    for num in range(num1,num2+1):
# Printing the result (numbers between the first and the second).
        print(num)

'''
task 2
Ряд - 2
Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.
'''
''' A programme, which prints all integer numbers from the first to the second, 
if the first number is smaller, than the second, 
and from the second to the first in another situation. 
'''
# Input 2 integer numbers:
num1=int(input())
num2=int(input())
# checking, if the first number is smaller, than the second:
if num1<num2:
''' counting all numbers between the first and the second plus one, 
as the cycle “for” doesn`t take into account the last number. 
'''
    for num in range(num1,num2+1):
# Printing the result (numbers between the first and the second).
        print(num)
# the first number is not smaller, than the second:
else:
# counting all numbers from the second to the first number 
    for num in range(num1,num2-1,-1):
# Printing the result (numbers from the second to the first).
        print(num)

'''
task 3
Ряд - 3
Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно. В этой задаче можно обойтись без инструкции if.
'''
# A programme, which prints all integer odd numbers from the first to the second
# Input 2 integer numbers:
num1 = int(input())
num2 = int(input())
# counting all odd numbers from the first to the second 
for num in range((num1-1)+num1%2, num2-1, -2) :
# Printing the result
    print(num, end=" ")

'''
task 4
Сумма десяти чисел
Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.
'''
# A programme, which counts the sum of 10 integer numbers.
# Printing the sum of inputted 10 numbers
print(sum(int(input()) for num in range (10)))

'''
task 5
Сумма N чисел
Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел. Какое наименьшее число переменных нужно для решения этой задачи?
'''
# The programme, which counts the sum of several numbers.
# Printing the sum of the number of integer numbers.
print(sum(int(input()) for num in range(int(input( )))))

'''task 6
Сумма кубов
По данному натуральном n вычислите сумму 13+23+33+...+n3.
'''
# The programme, which counts the sum of the cubes of several numbers.
# Inputting the number of numbers (from 1 to nums) and the variable sum.
sum=0
nums=int(input())
''' Choosing numbers from one to the inputted number plus one (because of the characteristic property or cycle “for”
'''
for num in range (1, nums+1):
# Cubing each number
    cube=(num**3)
# Counting the sum of cubed numbers
    sum += cube
print (sum)

'''task 7
Факториал
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
'''
# The programme, which counts the factorial of an inputted integer number.

# Inputting the number (the basic variate value of factorial).
fact_num=1
# Choosing all numbers from one to some inputted number, of which to cout factorial.
for num in range(1,int(input())+1):
# Multiplying all numbers
    fact_num = fact_num * num
# Printing the result
print(fact_num)

'''
task 8
Сумма факториалов
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено.
'''
# The programme, which counts the sum of several factorials (from 1! To n!).
# Input the maximal number.
num=int(input())
# Settind the basic variate value of factorial and sum.
fact=1
sum = 0
# Choosing all numbers from 1 to the maximal.
for i in range (1,num+1):
# Counting the factorial of each number.
    fact *= i
# Counting the sum of factorials.
    sum += fact
# Printing the result.
print (sum)

'''
task 9
Количество нулей
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
'''
# The programme, which counts the amount of numbers equal to sero.
# Entering the amount of numbers to input
Emount = int(input())
# Setting the basic variate value of the number of zeros.
num=0
# Choosing all the inputted numbers.
for i in range(Emount):
  num = int(input())
# Checking, if the number equals zero.
  if num==0: 
# Adding one to the number of zeros, if the inputted number equals zero.
    num+=1 
# Printing the result.
print(num)

'''task 10
Лесенка
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
'''
# The programme, which makes a ladder from numbers.
# Inputting a number (amount of numbers on the last step):
num = int(input())
# Choosing all numbers from the set.
for i in range(num):
# Choosing all numbers from one to the number from the previous operation.
    for j in range(1, i+2):
# Printing the result.
        print(j, end='')
    print()


'''task 11
Потерянная карточка
Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки.
Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
'''
''' The programme, which looks for the missing card, when the user gives the numbers of all other cards and the amount of cards.
'''
# Inputting the number of cards
n=int(input())
# Counting the sum of all numbers on the cards.
sum = (n*(n+1))/2
# Choosing all cards, accept one (missing).
for i in range (n-1):
# Inputting the known numbers.
   knewn=int(input())
# Making the sum equal to the sum minus the knewn numbers (equals the unknown number).
   sum -= knewn
# Printing the result (number of the unknown card).
print (sum)
