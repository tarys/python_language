'''
Homework №1.
task 1
Sum of three numbers
Напишите программу, которая считывает три числа и выводит их сумму. Каждое число записано в отдельной строке.
# The programme, which counts the sum of three given numbers.
'''
# Inputting 3 integer numbers.
num1 = int(input())
num2 = int(input())
num3 = int(input())
# Counting and printing the sum of three inputted numbers.
print(num1+num2+num3)

'''
task 2 
Area of a right triangle
Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь. Каждое число записано в отдельной строке.
# the programme, which counts the flat of the right triangle, when the user gives its cathets.
'''
# Inputting cathets. 
a = int(input())
b = int(input())
# Counting and printing the flat.
print(a*b/2)

'''
task 3
Hello, Harry!
Напишите программу, которая приветствует пользователя, выводя слово Hello, введенное имя и знаки препинания по образцу:
# The programme, which greets the user, after he gives his name.
'''
# Inputting the user`s name.
user_name = input()
# Greeting the user with his name.
print("Hello, ", user_name,"!", sep = "")

'''
task 4
Previous and next
Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).
# The programme, which counts the next and the previous number for the given number.
'''
# Inputting the given number.
num= int(input())
# Printing the next number.
print("The next number for your number ", num," is ",num+1,".", sep = "")
# Printing the previous number.
print("The previous number for your number ",num," is ",num-1,".", sep ="")

'''
task 5
Apple sharing
n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке? Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
'''
# The programme, which counts the amount of apples after dividing them between several students.
# Entering the amount of students
students = int(input())
# Entering the amount of apples, which were divided.
apples = int(input())
# Counting the amount of apples, left in the box.
print(apples//students)
print(apples%students)


'''
task 6
Digital clock
Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать электронные часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59). Учтите, что число n может быть больше, чем количество минут в сутках.
'''
'''The programme, which counts the number of hours and minutes, when the user gives the number of minutes passed, since the beginning of the day.
'''
# Entering the number of minutes
minutes = int(input())
# Counting the number of  days (1440 = 24* 60)
minutes = int(minutes % 1440)
# Counting The number of  hours.
print( minutes // 60)
# Counting the number of minutes
print( minutes % 60)

'''
task 7
School desks
В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты. За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
'''
# Inputting amount of students in each class.
students_class1 = int(input())
students_class2 = int(input())
students_class3 = int(input())
# Printing the minimal number of desks.
print(students_class1%2+students_class2%2+students_class3%2+students_class1//2+students_class2//2+students_class3//2)
