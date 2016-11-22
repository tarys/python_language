#task1------------------------------------------------------------
"""
	Given the two integers, print the least of them.
"""



#program which print minimum of two numbers
first_number=int(input())
second_number=int(input())
if first_number>=second_number:
    print(second_number)
else :
    print(first_number)
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
	The sign function sign(x) in mathematics is defined as follows: 
	sign(x) = 1, if x > 0, 
	sign(x) = -1, if x < 0, 
	sign(x) = 0, if x = 0.
	For the given integer X print the value sign(x). Try to use the cascade if-elif-else for it.
"""



# program of printing sign function of x
x=int(input())
if x>0 :
    print('1')
elif x<0:
    print('-1')
else:
    print("0")
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
	Given the three integers, print the least of them.
"""


# program which print minimum of three numbers
first_number=int(input())
second_number=int(input())
third_number=int(input())
if first_number>=second_number>=third_number or second_number>=first_number>=third_number :
    print(third_number)
elif third_number>=second_number>=first_number or second_number>=third_number>=first_number :
    print(first_number)
elif first_number>=third_number>=second_number or third_number>=first_number>=second_number:
    print(second_number)
#-----------------------------------------------------------------


#task4------------------------------------------------------------
'''
	Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
	The rules in Gregorian calendar are as follows:
	a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
	a year is always a leap year if its number is exactly divisible by 400
'''



# program of cheaking of year (leap or common)
year_number=int(input())
if (year_number%4 == 0) and (year_number%100 != 0) :
    print('LEAP')
elif year_number%400==0 :
    print('LEAP')
else:
    print("COMMON")
#-----------------------------------------------------------------


#task5------------------------------------------------------------
'''
	Given three integers. Determine how many of them are equal to each other. The program must print one of the numbers:
	3 (if all are same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).
'''


# program which printing how many equal numbers
first_number=int(input())
second_number=int(input())
third_number=int(input())
if first_number!=second_number and second_number!=third_number and third_number!=first_number :
    print(0)
elif (first_number==second_number and first_number!=third_number) :
    print (2)
elif first_number==third_number and first_number!=second_number:
    print(2)
elif second_number==third_number and second_number!=first_number:
    print(2)
else :
    print (3)
#-----------------------------------------------------------------



#task6------------------------------------------------------------
'''
	Chess rook moves horizontally or vertically. Given two different cells of the chessboard, 
	determine whether a rook can go from the first cell to the second in one move.
	The program receives the input of four numbers from 1 to 8, each specifying the column and row number,		
	first two - for the first cell, and then the last two - for the second cell. The program should output YES
	if a rook can go from the first cell to the second in one move, or NO otherwise.
'''


# program of cheaking of moving chees rook
# x1,y1 coordinates of first cell
# x2,y2 coordinates of second cell
# if chees rook can move from first cell to second print YES
# in other variant-NO
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if (x1==x2 and y1!=y2) or (y2==y1 and x1!=x2):
    print("YES")
else :
    print("NO")
#-----------------------------------------------------------------



#task7------------------------------------------------------------
'''
	Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
	The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first 
	cell, and then the last two - for the second cell.
'''


# program of showing color of cell on chees board
# if colours are diffrent program print NO
# in other case print YES
# x1,y1 coordinates first cell; x2,y2 coordinates second cell
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
# первая клетка
# клетка белая если один из индексов парный а другой не парный
# клетка черная если оба индекса парные или оба не парные
if (x1%2 != 0 and y1%2 == 0) or (x1%2 ==0 and y1%2 != 0): 
    a1=(1) #1-белый цвет
elif (x1%2 != 0 and y1%2 != 0) or (x1%2 == 0 and y1%2 == 0):
    a1=(0) #0-черный цвет

# вторая клетка    
if (x2%2 != 0 and y2%2 == 0) or (x2%2 ==0 and y2%2 != 0) :
    a2=(1) #1-белый цвет
elif (x2%2 != 0 and y2%2 != 0) or (x2%2 == 0 and y2%2 == 0):
    a2=(0) #0-черный цвет

if a1==a2:
    print("YES")
else:
    print("NO")
#-----------------------------------------------------------------


#task8------------------------------------------------------------
'''
	Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard,
	determine whether a king can go from the first cell to the second in one move.
	The program receives the input of four numbers from 1 to 8, each specifying the column and row number, 
	first two - for the first cell, and then the last two - for the second cell. The program should output 
	YES if a king can go from the first cell to the second in one move, or NO otherwise.
'''


# program of cheaking chees king moving
# x1,y1 coordinates first cell; x2,y2 coordinates second cell
# if chees king can move from first cell to second print YES
# in other variant-NO
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if x2>=(x1-1) and x2<=(x1+1) and y2>=(y1-1) and y2<=(y1+1):
    print("YES")
elif x1==x2 and y1==y2:
    print("YES")
else:
    print("NO")
#-----------------------------------------------------------------


#task9------------------------------------------------------------
'''
	Chess bishop moves diagonally to any number of cells. Given two different cells of the chessboard,
	determine whether a bishop can go from the first cell to the second in one move.
	The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
	first two - for the first cell, and then the last two - for the second cell. 
	The program should output YES if a Bishop can go from the first cell to the second in one move, or NO otherwise.
'''


# program of cheaking moving chess bishop
# x1,y1 coordinates first cell; x2,y2 coordinates second cell
# if chees bishop can move from first cell to second print YES
# in other variant-NO

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())


if (x1+y1)==(x2+y2) or (x1-y1)==(x2-y2) :
    print("YES")
else :
    print("NO")
#-----------------------------------------------------------------


#task10------------------------------------------------------------
'''
	Chess queen moves horizontally, vertically or diagonally to any number of cells. 
	Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
	The program receives the input of four numbers from 1 to 8, each specifying the column
	and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES
	if a queen can go from the first cell to the second in one move, or NO otherwise.
'''


# program of cheaking of moving chess queen
# x1,y1 coordinates first cell; x2,y2 coordinates second cell
# if chees queen can move from first cell to second print YES
# in other variant-NO

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if (x1+y1)==(x2+y2) or (x1-y1)==(x2-y2) : #диагональ
    print("YES")
elif (x1==x2 and y1!=y2) or (x1!=x2 and y1==y2): #горизонталь или вертикаль
    print("YES")
elif x1==x2 and y1==y2: #стоит на месте
    print("YES")
else:
    print("NO")
#-----------------------------------------------------------------


#task11------------------------------------------------------------
'''
	Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically,
	or two cells vertically and one cells horizontally. Given two different cells of the chessboard,
	determine whether a knight can go from the first cell to the second in one move.
	The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
	first two - for the first cell, and then the last two - for the second cell. The program should output 
	YES if a knight can go from the first cell to the second in one move, or NO otherwise.
'''


# program of cheaking of moving chess knight
# x1,y1 coordinates first cell; x2,y2 coordinates second cell
# if chees knight can move from first cell to second print YES
# in other variant-NO

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if (x2==(x1+2) or x2==(x1-2)) and (y2==(y1+1) or y2==(y1-1)): # вверх\вниз
    print("YES")
elif (x2==x1-1 or x2==x1+1) and (y2==y1+2 or y2==y1-2): # вправо\влево
    print("YES")
else:
    print("NO")
#-----------------------------------------------------------------


#task12------------------------------------------------------------
'''
	Chocolate bar has the form of a rectangle divided into n×mn×m portions. Chocolate bar can be split into
	two parts according to the pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.
	The program reads three integers: n, m, and k. It should print YES or NO.
'''


'''
    chocolate n x m area, if we can split into two parts by 
    k squares print YES, in other variant-NO
'''
n=int(input())
m=int(input())
k=int(input())
if ((k%n==0)or(k%m==0))and(k<=n*m):
    print("YES")
else:
    print("NO")
#-----------------------------------------------------------------
