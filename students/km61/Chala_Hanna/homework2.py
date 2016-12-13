'''
Homework №2
task 1
Минимум из двух чисел
Даны два целых числа. Выведите значение наименьшего из них.
'''
# The programme, which finds the least of two integer numbers.
# Entering two integer numbers.
num1=int(input())
num2=int(input())
# Checking, if the first number is bigger, than the second.
if num1>num2:
    print (num2)
# Otherwise, the first number is less, than the second.
else:
    print (num1)

'''
task 2
Знак числа
В математике функция sign(x) (знак числа) определена так: 
sign(x) = 1, если x > 0, 
sign(x) = -1, если x < 0, 
sign(x) = 0, если x = 0.
Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.
'''
# The programme, which gives the result of signum function.
# Inputting The variable (x)
x=int(input())
# Checking, if x is bigger than zero.
if x>0:
    print(1)
# Checking, if x is less than zero.
elif x<0:
    print(-1)
# Otherwise, x is equal to zero.
else:
    print (0)

'''
task 3
Шахматная доска
Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
'''
# The programme, which decides, if two given squares have the same colour.
# Inputting the coordinates of the two squares.
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Checking the consiquense, when 2 squares have the same color.
if (x1 + y1 + x2 + y2) % 2 == 0:
# The result, if ture.
    print('YES')
else:
# The result, if false.
    print('NO')

'''
task 4
Високосный год
Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
'''
# The programme, which determines if the year is leap.
# Input the year (integer number):
year=int(input())
# Checking the consequence of the leap year.
if (year%4==0 and not (year%100==0)) or (year%400==0):
# The result, if true.
    print ("LEAP")
else:
# The result, if false.
    print ("COMMON")

'''
task 5 
Минимум из трех чисел
Даны три целых числа. Выведите значение наименьшего из них.
'''
# The programme, which counts the minimum of three numbers.
# Inputting three integer numbers.
a = int(input())
b = int(input())
c = int(input())
# Checking, if a if the least number.
if b >= a <= c:
    print(a)
# Checking, if b is the least number.
elif a >= b <= c:
    print(b)
# Otherwise, c is the least number.
else:
    print(c)

'''
task 6
Сколько совпадает чисел
Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
'''
# The programme, which decides, how many of thre numbers are equal.
# Entering three integer numbers.
a = int(input())
b = int(input())
c = int(input())
# Checking, if all three numbers are equal.
if a == b == c:
    print(3)
# Checking, if two of the numbers are equal.
elif a == b or b == c or a == c:
    print(2)
# Otherwise, no number is equal to others.
else:
    print(0)

'''task 7
Ход ладьи
Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.
'''
# The programme, which decides, if the rock can get from 1 square to another in one step.
# Inputting the coordinates of the two squares.
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
# Checking the consiquense of the figure`s move.
if (x1==x2) or (y1==y2):
# The result, if ture.
    print ('YES')
else:
# The result, if false.
    print ('NO')

'''
task 8
Ход короля
Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.
'''
# The programme, which decides, if the king can get from 1 square to another in one step.
# Inputting the coordinates of the two squares.
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Checking the consiquense of the figure`s move.
if abs(x2-x1)<=1 and abs(y2-y1)<=1:
# The result, if ture.
    print ('YES')
else:
# The result, if false.
    print ('NO')

'''
task 9
Ход слона
Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.
'''
# The programme, which decides, if the bishop can get from 1 square to another in one step.
# Inputting the coordinates of the two squares.
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Checking the consiquense of the figure`s move.
if abs(x2-x1)==abs(y2-y1):
# The result, if ture.
    print ('YES')
else:
# The result, if false.
    print ('NO')

'''
task 10
Ход ферзя
Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.
'''
#The programme, which decides, if the qween can get from 1 square to another in one step.
# Inputting the coordinates of the two squares.
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Checking the consiquense of the figure`s move.
if abs(x2-x1)==abs(y2-y1) or (x1==x2) or (y1==y2):
# The result, if ture.
    print ('YES')
else:
# The result, if false.
    print ('NO')

'''
task 11
Ход коня
Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.
'''
#The programme, which decides, if the knight can get from 1 square to another in one step.
# Inputting the coordinates of the two squares.
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
# Checking the consiquense of the figure`s move.
if (abs(x2-x1)==2 and abs(y2-y1)==1) or (abs(x2-x1)==1 and abs(y2-y1)==2):
# The result, if ture.
    print ('YES')
else:
# The result, if false.
    print ('NO')

'''
task 12
Шоколадка
Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по прямой на две части. Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек. Программа получает на вход три числа: n, m, k и должна вывести YES или NO.
'''
''' The programme, which decides, if it is possible to divide the chocolate bar into a given amount of squares in one step.
'''
''' Inputting the number of horizontal and vertical squares in the bar, and the amount of the needed squares after dividing.
'''
n = int(input())
m = int(input())
k = int(input())
# Checking, if it is possible to divide.
if n * m >= k and (k % n == 0 or k % m == 0):
# The result, if true.
    print ("YES")
else:
# The result, if false.
    print ("NO")
