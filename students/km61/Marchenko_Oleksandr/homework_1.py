#task1------------------------------------------------------------
"""
Напишите программу, которая считывает три числа и выводит их сумму. Каждое число записано в отдельной строке.
"""
#Program calculate sum of three numbers
number_one = int(input('Enter first number'))                                                                                                                       
number_two = int(input('Enter second number'))
number_three = int(input('Enter third number'))
sum = number_one + number_two + number_three
print('Sum of three numbers=',sum)


#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь. 
Каждое число записано в отдельной строке.
"""
#Program calculates area of a right triangle
first_cathetus = float(input('Enter first cathetus'))
second_cathetus = float(input('Enter second cathetus'))
print('Area of triangle =', second_cathetus * first_cathetus / 2)



#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. 
Сколько яблок достанется каждому школьнику? 
Сколько яблок останется в корзинке? 
Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
"""
#Program prints amount of apples pupils will get, and amount of apples what will be in a basket
pupils_amount = int(input('Enter pupils amount'))
apples_amount = int(input('Enter apples amount'))
print('Amount of apples pupils will get=', apples_amount // pupils_amount)
print('Amount of apples what will be in a basket=', apples_amount % pupils_amount)


#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент. 
Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). 
Учтите, что число n может быть больше, чем количество минут в сутках.
"""

#Program prints time on clocks after n minutes passed 
minutes_amount = int(input('Enter amount of the minutes passed'))
hours_amount = minutes_amount // 60
print('Time on clocks',hours_amount % 24, minutes_amount % 60)

#-----------------------------------------------------------------

#task5------------------------------------------------------------
"""
Напишите программу, которая приветствует пользователя, выводя слово Hello, введенное имя и знаки препинания по образцу.
"""

#Program says hello to user 
user_name=input('Enter your name')
print("Hello,", user_name + "!")


#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).
"""

#Program prints previous and next numbers for entered number
number=int(input('Enter number'))
print("The next number for the number",number, "is", str(number + 1) + ".")
print("The previous number for the number", number, "is", str(number - 1) + ".") 



#-----------------------------------------------------------------

#task7------------------------------------------------------------
"""
В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты. 
За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников? 
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
"""
#Program prints amount of tables needed for entered pupils amount
pupils_amount = int(input('Enter pupils amount in first form'))
tables_amount = pupils_amount // 2 + pupils_amount % 2
pupils_amount = int(input('Enter pupils amount in second form'))
tables_amount = desk_amount+pupils_amount // 2 + pupils_amount % 2
pupils_amount = int(input('Enter pupils amount in third form'))
tables_amount = tebles_amount + pupils_amount // 2 + pupils_amount % 2
print('Needed tables amount =' tables_amount)
#-----------------------------------------------------------------

