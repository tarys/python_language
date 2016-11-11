#Завдання1-----------------------------------------------------------------------------------
"""
Даны два целых числа A и B (при этом A ? B). Выведите все числа от A до B включительно.
"""
first_number=int(input())#Введенння першого числа
second_number=int(input())#Введенння першого числа
i=first_number#Присвоєння змінній і значення першого числа
x=second_number-first_number#
for a in range(x):#Цикл з 0 до х
    print(i)#Виведення "і"
    i+=1#Присвоєння значенню "і" значення і+1
print(i)#виведення "і""

#Завдання2-----------------------------------------------------------------------------------
"""
Даны два целых числа A и В. Выведите все числа от A до B включительно, 
в порядке возрастания, если A < B, или в порядке убывания в противном случае.
"""
first_number=int(input())#Введенння першого числа
second_number=int(input())#Введенння другого числа
if first_number<=second_number: #Умова зростання
    for i in range(first_number,second_number+1):#Цикл від першого числа, що введе користувач до другого+1
        print(i)#вивести "і"
else:#інакше    
    for i in range(first_number,second_number-1,-1):#Цикл від другого числа, що введе користувач до першого+1
        print(i)#вивести "і"

#Завдання3-----------------------------------------------------------------------------------
"""
Даны два целых числа A и В, A>BA>B. Выведите все нечётные числа от A до B включительно.
В этой задаче можно обойтись без инструкции if.
"""
first_number = int(input())#Введення першого числа
second_number = int(input())#Введення другого числа
for i in range(first_number,second_number-1,-1):#Цикл від першого до другого
    if i%2==1:#Перевірка на парність
        print(i)#Виведення і
    temporalvariable=i#Введення тимчасової змінної
if i%2==1 and i!=temporalvariable:#Перевірка на парність та належність попередньому значенню
    print(i)#Виведення і

#Завдання4-----------------------------------------------------------------------------------
"""
Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.
"""
#Програма для визначення суми 10 цілих чисел
sum=0#Присвоєння змінній значення 0
for i in range(10):#Цикл від 0 до 9
    number=int(input())#Введення числа користувачем
    sum+=number#Знаходження суми чисел
print(sum)#Виведення суми чисел

#Завдання5-----------------------------------------------------------------------------------
"""
Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, 
затем вводится ровно N целых чисел. Какое наименьшее число переменных нужно для решения этой задачи?
"""
#Програма для визначення суми N цілих чисел
sum=0#Присвоєння змінній значення 0
number_of_number=int(input())#Цикл від 0 до N
for i in range(number_of_number):#Введення числа користувачем
    sum+=int(input())#Знаходження суми чисел
print(sum)#Виведення суми чисел

#Завдання6-----------------------------------------------------------------------------------
"""
По данному натуральном n вычислите сумму 1**3+2**3+3**3+...+n**3.
"""
#Програма для визначення суми n кубів
sum=0#Присвоєння змінній значення 0
number_of_cube=int(input())#Введення кількості чисел
for i in range(number_of_cube+1):#Цикл від 0 до N
    sum+=i**3#Сума кубів
print(sum)#Виведення суми кубів

#Завдання7-----------------------------------------------------------------------------------
"""
Факториалом числа n называется произведение 1 ? 2 ? ... ? n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
"""
#Програма для знаходження факторіалу
number_of_factorial=int(input())#Введення числа користувачем
factorial=1#Присвоєння змінній значення 1
for i in range(number_of_factorial):#Цикл від 0 до n
    factorial*=i+1#Знаходження факторіалу
print(factorial)#виведення факторіалу

#Завдання8-----------------------------------------------------------------------------------
"""
По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл.
 Пользоваться математической библиотекой math в этой задаче запрещено.
"""
#Програма для визначення суми факторіалів
number_of_factorial=int(input())#Введення числа користувачем
sum=0#Присвоєння змінній значення 0
for i in range(number_of_factorial):#Цикл від 0 до n
    fact=1#Присвоєння змінній значення 1
    for j in range(i+1):#Цикл від j до i
        fact*=j+1 #Знаходження факторіалу
    sum+=fact#Знаходження суми

#Завдання9-----------------------------------------------------------------------------------
"""
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. 
Подсчитайте количество нулей среди введенных чисел и выведите это количество. 
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
"""
#Програма для визначення кількості нулей
number_of_zero=int(input())#Введення числа користувачем
sum=0#Присвоєння змінній значення 0
for i in range(number_of_zero):#Цикл від 0 до числа, що введе користувач
    number=int(input())#Введення числа користувачем
    if number==0:# Умова для знаходження 0 
        sum+=1#Знаходження суми чисел 0
print(sum)#Виведення суми чисел 0