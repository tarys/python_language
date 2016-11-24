# your code--'Conditions: if, then, else'------------------------------
#task1
"""Given the two integers, print the least of them"""
x = int(input())
y = int(input())
# int, because x, y==numbers
if x > y:
   print(y)
else:
    print(x)
#task2
"""The sign function sign(x) in mathematics is defined as follows: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0."""
#For the given integer X print the value sign(x)
#Try to use the cascade if-elif-else for it.
x  = int(input())
# int, because x, ==number
if x > 0:
    print ("1")
elif x < 0:
    print("-1")
else:
    print("0")
 #task3
 """Given the three integers, print the least of them"""
 x = int(input())
y = int(input())
z = int(input())
# int, because x, y, z==numbers

if x > y and z > y:
   print(y)
elif y > x and z > x:
    print(x)
elif y > z and x > z:
    print(z)
else:
    print(x)
 #task4
    """Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
#The rules in Gregorian calendar are as follows:

#a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
#a year is always a leap year if its number is exactly divisible by 400"""
x = int(input())
# int, because x,==number

if x % 4 ==0 and x % 100 != 0:
    print ("LEAP")
elif x % 400 == 0:
    print ("LEAP")
else:
    print("COMMON")
 #task5
    """Given three integers. Determine how many of them are equal to each other."""
#The program must print one of the numbers: 3 (if all are same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different)
    x = int(input())
y = int(input())
z = int(input())
# int, because x, y, z==numbers
if x == y == z :
    print(3)
elif x == y or x == z or z == y:
        print(2)
else:
    print(0)
  #task6
   """Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move."""
#The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise
   a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==c or b==d:
    print("YES")
else:
    print("NO")
 #task7
    """Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO."""
#The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell
    x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if (x1+y1)%2==(x2+y2)%2:
    print("YES")
else:
    print("NO")
  #task8
    """x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
# int, because x1, x2, y1, y2==numbers
if abs(x1-x2)<2 and abs(y1-y2)<2:
    print("YES")
else:
    print("NO")
 #task9
    """Chess bishop moves diagonally to any number of cells. Given two different cells of the chessboard, determine whether a bishop can go from the first cell to the second in one move."""
    x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
# int, because x1, x2, y1, y2==numbers
if abs(x1-x2)==abs(y1-y2):
    print("YES")
else:
    print("NO")
#task10
"""Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move."""
#The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
# int, because x1, x2, y1, y2==numbers
if (abs(x1-x2)==abs(y1-y2)) or ((x1==x2) or (y1==y2)):
    print("YES")
else:
    print("NO")
 #task11
 """Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move."""
#The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise
 x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
# int, because x1, x2, y1, y2==numbers
if (abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==2):
    print("YES")
else:
    print("NO")
#task12
"""Chocolate bar has the form of a rectangle divided into n*m portions. Chocolate bar can be split into two parts according to the pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares."""
#The program reads three integers: n, m, and k. It should print YES or NO.
m = int(input())
n = int(input())
k = int(input())
#int, because n, k, m==parts of numbers

if (k%n==0 or k%m==0) and (k<=m*n):
    print ("YES")
else:
    print ("NO")
 goes here