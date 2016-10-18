#task1------------------------------------------------------------
"""
Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
"""
#The program, which shows the sequence between two numbers
int_first_number = int(input("Enter the first number: "))
int_second_number = int(input("Enter the second number: "))
if (int_first_number > int_second_number):
    print("Number 1 must be less or equal then number 2")
for i in range(int_first_number, int_second_number + 1 ):
    print(i)
#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.
"""
#The program, which shows the sequence between two numbers
int_number_1 = int(input("Enter the first number: "))
int_number_2 = int(input("Enter the second number: "))
if (int_number_1 < int_number_2):       #if int_number_1 < int_number_2
    for i in range(int_number_1, int_number_2 + 1):
        print(i)
if (int_number_1 > int_number_2):       #if int_number_1 > int_number_2
    for k in range(int_number_1, int_number_2 - 1, -1):
        print(k)
elif(int_number_1 == int_number_2):
    print(int_number_1)
#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
Даны два целых числа A и В, A>BA>B. Выведите все нечётные числа от A до B включительно. В этой задаче можно обойтись без инструкции if.
"""
#Program which shows all odd numbers between number 1 and number 2
#number_1 > number_2
int_number_1 = int(input("Enter the first mumber: "))
int_number_2 = int(input("Enter the second mumber: "))

for i in range(int_number_1, int_number_2 - 1, -1):
    if (i % 2 != 0):
        print(i)
#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.
"""
# Program for addition of 10 numbers
Sum = 0
for i in range(1, 11):
   number = int((input('Enter number: ')))
   Sum = Sum + number

print("Sum = ", Sum)
#-----------------------------------------------------------------

#task5------------------------------------------------------------
"""
Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел. Какое наименьшее число переменных нужно для решения этой задачи?
"""
#Program calculates sum of n numbers entered by user
quantity_numbers = int(input("Enter the quantity of the numbers: "))
Sum = 0
for i in range(1, quantity_numbers + 1):
   number = int(input("Enter the number: "))
   Sum = Sum + number

print("Sum = ", Sum)
#-----------------------------------------------------------------

#task6------------------------------------------------------------
"""
По данному натуральном n вычислите сумму 1^3+2^3+3^3+...+n^3.
"""
# Program calculates sum of cubes from 1 to n 
amount_numbers = int(input('Enter the amount of numbers: '))
sum_cubes = 0
for i in range (1, amount_numbers + 1):
    sum_cubes = sum_cubes + i ** 3
print('The result is ', sum_cubes)
#-----------------------------------------------------------------

#task7------------------------------------------------------------
"""
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
"""
# Program calculating the factorial of N
N_factorial = int(input('Enter the number of factorials: '))
res_factorial = 1
for i in range (1, N_factorial + 1):
    res_factorial *= i
print('The result is ', res_factorial)
#-----------------------------------------------------------------

#task8------------------------------------------------------------
"""
По данному натуральном n вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено.
"""
# Program, calculating sum of the factorial of N
Num_factorial = int(input('Enter the number of factorial: '))
Res_factorial = 1
Sum_factorial = 0
for i in range(1, Num_factorial + 1):
    Res_factorial *= i
    Sum_factorial += Res_factorial 
print("Result is", Sum_factorial)
#-----------------------------------------------------------------

#task9------------------------------------------------------------
"""
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
"""
# Program counting the zero numbers from the range of input numbers
range_numbers = int(input('Enter the quantity pf the numbers: '))
quantity_zero = 0
for i in range(1, range_numbers + 1):
    number = int(input('Enter the number: '))
    if (number == 0):
        for k in range(0, 1):
            quantity_zero += 1 
print(quantity_zero)

#-----------------------------------------------------------------

#task10-----------------------------------------------------------
"""
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
"""
# program building the 'ledder' using numbers
number_to_built = int(input())
for i in range(1, number_to_built + 1):
    for j in range(1,i+1):
        print(j, end='')
    print()
#-----------------------------------------------------------------

