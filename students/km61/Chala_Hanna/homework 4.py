'''
task 1
Список квадратов
По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
'''
# The programme, which prints the squares of all numbers less or equal to the given.
# Inputting the integer number.
N=int(input())
i=1
# Checking all elements until they are less or equal to the given number.
while i**2<=N:
# Square each number and print them.
    print (i**2)
    i+=1

'''
task 2
Минимальный делитель
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
'''
# The programme, which gives the least integer devisor of the given number, accept 1.
# Inputting the integer number.
n = int(input())
i = 2
# Checking numbers, until one of them is the divisor of the given.
while n%i != 0:
    i += 1
# Printing the least divisor.
print(i)


'''
task 3
Степень двойки
По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.
Операцией возведения в степень пользоваться нельзя!
'''
''' The programme, which finds the biggest degree of two, less or equal to the given integer number.
'''
# Inputting the integer number.
n=int(input())
i=0
# Checking all degrees of two, less or equal than the inputted number.
while 2**i <=n:
    i+=1
# Printing the biggest degree of two.
print (i-1,2**(i-1))

'''
task 4
Утренняя пробежка
В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
Программа получает на вход действительные числа x и y и должна вывести одно натуральное число.
'''
''' Programme, that determines the number of the day, when the distance of the runner equals the given number, if he increases on 10 percent from the previous.
'''
# Inputting the starting number of kilometers and the finishing number (integer).
Starting_num=int(input())
Finishing_num=int(input())
day=1
# Increasind the number of kilometres on 10 percent until it is less then the finishing number.
while starting_num<finishing_num:
    starting_num=1.1*starting_num
# Increasing each day.
    day=day+1
# Printing the result ( the integer number of the days).
print (day)

'''
task 5
Банковские проценты
Вклад в банке составляет x рублей. Ежегодно он увеличивается на p процентов, после чегодробная часть копеек отбрасывается. Определите, через сколько лет вклад составит не менее yрублей.
Выражение «дробная часть копеек отбрасывается» означает, что если у вас оказалось 123.4567 рублей, т. е. 123 рубля и 45.67 копеек, то после округления у вас получится 123 рубля и 45 копеек, т.е. 123.45 рублей.
Программа получает на вход три натуральных числа: x, p, y и должна вывести одно целое число.
'''
''' The programme, that determines how many years are needed to make the deposit equal to the given number, if it increases on p percent each year.
'''
''' Inputting the beginning amount of money, the number of percents each year and the finishing deposit.
'''
given_amount=int(input())
p=int(input())
finishing_deposit=int(input())
year=0
# Checking all numbers, when the given_amount is less than finishing_deposit.
while given_amount<finishing_deposit:
# Adding one year each time, when the condition is true.
    year+=1
# Adding the given amount
    given_amount+= ((given_amount/100)*p)
    given_amount= (given_amount*100)//1/100
# Printing a result.
print(year)

'''
task 6
Длина последовательности
Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке. Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0). Числа, следующие за числом 0, считывать не нужно.
'''
# The programme, which gives the number of the elements in the sequence, ending with zero.
i=0
# The condition to start inputting the elements.
while True:
# Inputting the elements.
    n=int(input())
# Stop inputting if the element is zero.
    if n==0:
        break
# Counting the elements.
    i += 1
# Printing the result.
print (i)

'''
task 7
Сумма последовательности
Определите сумму всех элементов последовательности, завершающейся числом 0. В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно.
'''
# The programme, which determines the sum of all elements in the sequence, ending with zero.
i=0
# The condition to start inputting the elements.
while True:
# Inputting the elements.
    n=int(input())
# Stop inputting if the element is zero.
    if n==0:
        break
# Counting the sum of the elements (adding the amount of each element).
    i +=n
# Printing the result.
print (i)

'''
task 8
Среднее значение последовательности
Определите среднее значение всех элементов последовательности, завершающейся числом 0.
'''
#The programme, which counts the average of the sequence, ending with zero.
a = 0
b = -1
n = 1
# The condition to start inputting the elements.
while n:
# Inputting the elements.
    n = int(input())
# Adding the elements.
    a = a + n
# Adding the number of elements
    b = b + 1
# Printing the average of the sequence.
print(a/b)

'''
task 9
Максимум последовательности
Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности.
'''
#The programme, which finds the maximal element of the sequence.
# Inputting the elements.
n = int(input())
max = 0
# Inputting the elements until one of them equals zero.
while n != 0:
# Checking if the element is bigger than zero (maximum).
    if n > max:
# If the condition is true, than the element is maximal.
       max = n
    n = int(input())
# Printing the result.
print(max)

'''
task 10
Индекс максимума последовательности
Последовательность состоит из натуральных чисел и завершается числом 0. Определите индекс наибольшего элемента последовательности. Если наибольших элементов несколько, выведите индекс первого из них. Нумерация элементов начинается с нуля.
'''
# The programme, which finds the index of maximal element in the sequence.
number = 1 
max = 0 
i = 0 
index = 0 
# Enterring numbers, until one of them is zero. 
while number != 0: 
# Enterriong the elements of the sequence.
    number = int(input()) 
# Identifying the biggest element (Checking, if any element is bigger than the basic value of max)
    if number > max: 
        max = number 
# Counting the indexes of elements, until reaching the biggest.
        index = i 
    i += 1 
# Printing the result.
print(index)

'''
task 11
Количество четных элементов последовательности
Определите количество четных элементов в последовательности, завершающейся числом 0.
'''
# The programme, which finds the number of even elements in the sequence, that ends with zero.
element = -1
amount = -1
# Inputting the elements, until one of them is zero.
while element != 0:
    element = int(input())
# Checking, if the element is even.
    if element % 2 == 0:
# Counting the number of even elements.
        amount += 1
# Printing the result.
print(i)

'''
task 12
Количество элементов, которые больше предыдущего
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.
'''
# The programme, which finds the number of elements, which are bigger, than the previous one.
num = 1 
prev_el = 0 
i = 0 
# Ending inputting, when one of the elements is zero.
while num != 0: 
    num = int(input()) 
# Comparing elements with the previous.
    if num > prev_el: 
# Checking, if the previous element is not zero.
        if prev_el != 0: 
# Adding to the number of elenents those, which confirm the conditions.
            i += 1 
    prev_el = num
# Printing the result.
print(i)

'''
task 13
Второй максимум
Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго по величине элемента в этой последовательности. Гарантируется, что в последовательности есть хотя бы два элемента.
'''
# Programme, which finds the second maximal element.
num = 1 
first = 0 
sec = 0 
# Inputting elements, until one of them is zero.
while num != 0: 
    num = int(input()) 
# Finding the maximal element.
# Defining, which of the elements is the first and second maximum
    if num > first: 
        sec = first 
        first = num 
    elif num > sec: 
        sec = num 
# Printing the smaller maximum.
print(sec)

'''
task 14
Количество элементов, равных максимуму
Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
'''
# The programme counts the number of element, equal to the maximal.
num = 1 
max = 0 
i = 1 
# Inputting the elements, until one of them is zero.
while num != 0: 
    num = int(input()) 
# Checking, if the element is maximal.
    if num > max: 
        i = 1 
        max = num 
# Finding the elements, equal to maximal.
    elif num == max: 
# Adding the number of such elements.
        i += 1 
# Printing the result.
print(i)

'''
task 15
Числа Фибоначчи
Последовательность Фибоначчи определяется так:
φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
По данному числу n определите n-е число Фибоначчи φn.
Эту задачу можно решать и циклом for.
'''
#The programm finds a Fibonacci number from the index
#Inputting an index
N = int(input())
phi_previous = 0
phi = 1
# Checking the condition in every element of the sequence
for i in range(N - 1):
# Counting the n-th Fibonacci number 
    phi, phi_previous = phi + phi_previous, phi
# Printing the number, depending on the result of the condition.
print(phi if N > 0 else 0)

'''
task 16
Стандартное отклонение
Определите стандартное отклонение для данной последовательности натуральных
чисел, завершающейся числом 0.
'''
#The programme to find  standard deviation.
#Inputtting the basic number
number=int(input())
n=0
sum=0
sum_square=0
# Continue, until zero.
while number!=0:
    sum+=number
    sum_squar+=(number**2)
    n+=1
# Inputting the next number
    number=int(input())
sum*=sum
# Printing the result
print(((sum_squar-sum/n)/(n-1))**0.5)
