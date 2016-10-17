#task1------------------------------------------------------------
"""
Даны два целых числа. Выведите значение наименьшего из них.
"""
#Program prints minimum of two numbers
first_number=int(input('Enter first number'))
second_number=int(input('Enter second number'))
if first_number>second_number:
    print('Minimum:',second_number)
else:
    print('Minimum:',first_number)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.
"""
#Program calculates sign(x)
x=int(input('Enter number'))
if x<0:
    print('sign(x)=',-1)
elif x==0:
    print('sign(x)=',0)
else:
    print('sign(x)=',1)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Даны три целых числа. Выведите значение наименьшего из них.
"""
#Program prints minimum of three numbers
first_number=int(input('Enter first number'))
second_number=int(input('Enter second number'))
third_number=int(input('Enter third number'))
if (first_number<second_number) and (first_number<third_number):
    print('Minimum of three numbers:',first_number)
elif (second_number<first_number) and (second_number<third_number):
    print('Minimum of three numbers:',second_number)
else:
    print('Minimum of three numbers:',third_number)


#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дано натуральное число.
Требуется определить, является ли год с данным номером високосным. 
Если год является високосным, то выведите YES, иначе выведите NO. 
Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
"""

#Program prints "LEAP" if year is leap, or "COMMON" if year is common
year=int(input())
if ((year%4==0) and (year%100!=0)) or (year%400==0):
    print("LEAP")
else:
    print("COMMON")

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Даны три целых числа
Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
"""

#Program prints amount of equal numbers 
first_number=int(input('Enter first number'))
second_number=int(input('Enter second number'))
third_number=int(input('Enter third number'))
if first_number==second_number and second_number==third_number:
    print("Amount of equal numbers is 3")
elif first_number==second_number or second_number==third_number or first_number==third_number_number:
    print("Amount of equal numbers is 2")
else:
    print("Amount of equal numbers is 0")

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Шахматная ладья ходит по горизонтали или вертикали. 
Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.
"""

#Program prints "YES" if rock can move to entered coordinats, and "NO" if can't
rook_first_cordinat=int(input('Enter rook first cordinat'))
rook_second_cordinat=int(input('Enter rook second cordinat'))
square_first_cordinat=int(input('Enter square first cordinat'))
square_second_cordinat=int(input('Enter square second cordinat'))
if rook_first_cordinat==square_first_cordinat or rook_second_cordinat==square_second_cordinat:
	print("YES")
else:
    print("NO")

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Заданы две клетки шахматной доски.
Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
"""
#Program prints "YES" if two chess cells have the same color, or "NO" if have not 
first_cordinat_first_cell=int(input('Enter first cordinat first cell'))
second_cordinat_first_cell=int(input('Enter second cordinat first cell'))
first_cordinat_second_cell=int(input('Enter first cordinat second cell'))
second_cordinat_second_cell=int(input('Enter second cordinat second cell'))
if (first_cordinat_first_cell+second_cordinat_first_cell)%2==(first_cordinat_second_cell+second_cordinat_second_cell)%2:
    print("YES")
else:
    print("NO")


#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. 
Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.
"""
#Program prints "YES" if king can move to cell, or "NO" if he can't
kings_first_cordinat=int(input('Enter kings first cordinat'))
kings_second_cordinat=int(input('Enter kings second cordinat'))
square_first_cordinat=int(input('Enter square first cordinat'))
square_second_cordinat=int(input('Enter square second cordinat'))
if abs(square_first_cordinat-kings_first_cordinat)<=1 and abs(square_second_cordinat-kings_second_cordinat)<=1:
    print("YES")
else:
    print("NO")

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Шахматный слон ходит по диагонали. 
Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.
"""

#Program prints "YES"if bishop can move to cell, and "NO" if he can't
bishops_first_cordinat=int(input('Enter bishops first cordinat'))
bishops_second_cordinat=int(input('Enter bishops second cordinat'))
square_first_cordinat=int(input('Enter square first cordinat'))
square_second_cordinat=int(input('Enter square second cordinat'))
if abs(square_first_cordinat-bishops_first_cordinat)==abs(square_second_cordinat-bishops_second_cordinat):
    print("YES")
else:
    print("NO")


#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
Шахматный ферзь ходит по диагонали, горизонтали или вертикали. 
Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.
"""
#Program prints "YES" if queen can move to cell, and "NO" if she can't
queens_first_cordinat=int(input('Enter queens first cordinat))
queens_second_cordinat=int(input('Enter queens second cordinat'))
square_first_cordinat=int(input('Enter square first cordinat'))
square_second_cordinat=int(input('Enter square second cordinat'))
if abs(square_first_cordinat-queens_first_cordinat)==abs(square_second_cordinat-queens_second_cordinat) or queens_first_cordinat==square_first_cordinat or queens_second_cordinat==square_second_cordinat:
    print("YES")
else:
    print("NO")

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот.
 Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.
"""
#Program prints "YES"if knight can move to cell, and "NO" if he can't
knights_first_cordinat=int(input('Enter knights first cordinat'))
knights_second_cordinat=int(input('Enter knights second cordinat'))
square_first_cordinat=int(input('Enter square first cordinat'))
square_second_cordinat=int(input('Enter square second cordinat'))
if abs(square_first_cordinat-knights_first_cordinat)==1 and abs(knights_second_cordinat-square_second_cordinat)==2: 
    print("YES")
elif abs(square_second_cordinat-knights_second_cordinat)==1 and abs(square_first_cordinat-knights_first_cordinat)==2:
	print("YES")
else:
    print("NO")

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Шоколадка имеет вид прямоугольника, разделенного на n×m долек. 
Шоколадку можно один раз разломить по прямой на две части. 
Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек. 
Программа получает на вход три числа: n, m, k и должна вывести YES или NO.
"""
#Program prints "YES" if user can divide chocolate bar into k pieces, or "NO" if he can't
chocolate_bar_rows_amount=int(input())
chocolate_bar_cows_amount=int(input())
k=int(input())
if k<=chocolate_bar_cows_amount*chocolate_bar_rows_amount and (k%chocolate_bar_cows_amount==0 or k%chocolate_bar_rows_amount==0):
    print("YES")
else:
    print("NO")


#-----------------------------------------------------------------