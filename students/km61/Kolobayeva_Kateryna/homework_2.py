Minimum of two numbers
"""
Given the two integers, print the least of them.
"""
#This program print the least of the two integers:
# x = int(input())

x = int(input())
# y = int(input())

y = int(input())
if x > y:
# x > y
   print(y)
else:
# x< y
    print(x)


Sign function
"""
The sign function sign(x) in mathematics is defined as follows: 
 sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0.
For the given integer X print the value sign(x). Try to use the cascade if-elif-else for it.
"""
# The sign function:
# x  = int(input())

x  = int(input())
if x > 0:
# sign(x) = 1, if x > 0
    print ("1")
elif x < 0:
# sign(x) = -1, if x < 0
    print("-1")
else:
# sign(x) = 0, if x = 0
    print("0")

Minimum of three numbers
"""
Given the three integers, print the least of them
"""
# This program print the least of the three integers:
# x = int(input())
x = int(input())

# y = int(input())
y = int(input())

# z = int(input())
z = int(input())
if x > y and z > y:
# x > y , z > y
   print(y)
elif y > x and z > x:
# y > x , z > x
    print(x)
elif y > z and x > z:
# y > z ,  x > z
    print(z)
else:
#print(x)
    print(x)


Leap year
"""
Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
The rules in Gregorian calendar are as follows:
•	a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
•	a year is always a leap year if its number is exactly divisible by 400

"""	
# This program check if this year is a leap year:
# x = int(input())
x = int(input())

# a year is a leap year if its number is exactly divisible by 4 and is not exactly
divisible by 100
if x % 4 ==0 and x % 100 != 0:
# print ("LEAP")
    print ("LEAP")

# a year is always a leap year if its number is exactly divisible by 400
elif x % 400 == 0:
# print ("LEAP")
    print ("LEAP")
#if not
else:
# print("COMMON")
    print("COMMON")


Equal numbers
"""
Given three integers. Determine how many of them are equal to each other. The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).
"""
# The program must print one of the numbers:
# x = int(input())
x = int(input())

# y = int(input())
y = int(input())

# z = int(input())
z = int(input())

if x == y == z :
#if all are same
# print(3)
    print(3)

elif x == y or x == z or z == y:
# if two of them are equal to each other and the third is different
# print(2)
        print(2)

else:
# if all numbers are different
# print(0)

    print(0)



Rook move
"""
Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.
"""
# The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise:
# first two - for the first cell
b = int(input())
c = int(input())
# the last two - for the second cell
d = int(input())

if a==c or b==d:
# if a rook can go from the first cell to the second in one move
# print("YES")
    print("YES")
else:
# if a rook can not  go from the first cell to the second in one move
# print("NO")
    print("NO")

Chess board
"""
 Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.
"""
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number:
# first two - for the first cell
x1=int(input())
y1=int(input())
# the last two - for the second cell
x2=int(input())
y2=int(input())

if (x1+y1)%2==(x2+y2)%2:
# If they are painted in one color
#print ("YES")
    print("YES")
else:
# If they are not  painted in one color
#print ("No")
    print("NO")
King move
"""
Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.
"""
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number:
# first two - for the first cell
x1=int(input())
y1=int(input())

# the last two - for the second cell
x2=int(input())
y2=int(input())

if abs(x1-x2)<2 and abs(y1-y2)<2:
# if a king can go from the first cell to the second in one move
# print("YES")
    print("YES")
else:
# if a king can not go from the first cell to the second in one move
# print("NO")
    print("NO")

Bishop move
"""
Chess bishop moves diagonally to any number of cells. Given two different cells of the chessboard, determine whether a bishop can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a Bishop can go from the first cell to the second in one move, or NO otherwise.
"""
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number:
# first two - for the first cell
x1=int(input())
y1=int(input())
# the last two - for the second cell
x2=int(input())
y2=int(input())

if abs(x1-x2)==abs(y1-y2):
# if a Bishop can go from the first cell to the second in one move
# print("YES")
    print("YES")
else:
# if a Bishop can not go from the first cell to the second in one move
# print("NO")
    print("NO")



Queen move
"""
Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.
"""
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number:
# first two - for the first cell
x1=int(input())
y1=int(input())

# the last two - for the second cell 
x2=int(input())
y2=int(input())

if (abs(x1-x2)==abs(y1-y2)) or ((x1==x2) or (y1==y2)):
# if a queen can go from the first cell to the second in one move
# print("YES")
    print("YES")

else:
# if a queen can not go from the first cell to the second in one move
# print("NO")
    print("NO")


Knight move
"""
 Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.

"""
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number:
# first two - for the first cell
x1=int(input())
y1=int(input())

# the last two - for the second cell 
x2=int(input())
y2=int(input())

if (abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==2):
# if a knight  can go from the first cell to the second in one move
# print("YES")
    print("YES")
else:
# if a knight can not go from the first cell to the second in one move
# print("NO")
    print("NO")
Chocolate bar
"""
Chocolate bar has the form of a rectangle divided into n×mn×m portions. Chocolate bar can be split into two parts according to the pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.
The program reads three integers: n, m, and k. It should print YES or NO.

"""
# Determine whether it is possible to split it so that one of the parts will have exactly k squares:
# The program reads three integers
m = int(input())
n = int(input())
k = int(input())

# Chocolate bar can be split into two parts according to the pattern
if (k%n==0 or k%m==0) and (k<=m*n):
# If chocolate can be divided
# print ("YES")
    print ("YES")

else:
# If not  chocolate can be divided
# print ("NO")
    print ("NO")



