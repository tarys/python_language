Sum of three numbers 
"""
Write a program that takes three numbers and prints their sum. Every number is given in a separate line.
"""
# This program takes three numbers and prints their sum:
# a = int(input())
a = int(input())
# b = int(input())
b = int(input())
# c = int(input())
c = int(input())

# print (a+b+c)

print(a+b+c)

Area of a right triangle 
"""
Write a program that reads the two lengths of the base and the height in the right triangle and prints its area. Every number is given in a separate line.
"""
# This program reads the two lengths of the base and the height in the right triangle and prints its area:
# b = int(input())
# b – the base
b = int(input())
# h = int(input())
# h – the heignt
h = int(input())
#print(0.5*b*h)

print(0.5*b*h)


Apple sharing
"""
N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will get each single student? How many apples will remain in the basket?
The program gets the numbers N and K. It should print the two numbers: answers for the questions above.

"""
#The program gets the numbers N and K. It should print the two numbers: 
#n=int(input())
#k=int(input())

n=int(input())
k=int(input())
#How many apples will get each single student?
# print(k//n)

print(k//n)
#How many apples will remain in the basket?
# print(k%n)

print(k%n)

Digital clock
"""
Given the integer N - how many minutes are passed since some midnight. How many hours and minutes are displayed on the 24h digital clock?
The program should print the two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59). Take into account that the starting midnight could be several days ago, so the number N can be substantially big.
"""
# The program should print the two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).
# n = int(input())
n = int(input())
#hours
hours = n % (60 * 24) // 60
#minutes
minutes = n % 60
# print(hours, minutes))

print(hours, minutes))

Hello, Harry!
"""
Write a program that greets the user by printing the word "Hello", the name of the user and the exclamation mark after it. See the examples below.
"""
# This program should enter the phrase "Hello" name and an exclamation point after :
name = input()
# read a single line and store it in the variable "name"
# Print ('Hello'+ ', '  + name + '!')
print('Hello'+ ', '  + name + '!')

Previous and next
"""
Write a program that reads an integer number and prints its previous and next numbers. See the examples below. Remember that you can convert the numbers to strings using the function str.

The next number for the number 179 is 180.
The previous number for the number 179 is 178
"""
#This program reads an integer number and prints its previous and next numbers:
# a = input()

a = input()
# print('The next number for the number '+ a + ' is '+ '.')
print('The next number for the number '+ a + ' is '+ '.')

# print('The previous number for the number ' + a + ' is '+ '.'  )
print('The previous number for the number ' + a + ' is '+ '.'  )

School desks
"""
One school decided to form three new groups and furnish the individual classrooms for each of them. Each school desk is for two students. Given the number of students in each group, print the smallest possible number of school desks that should be purchased.
The program gets three integers: the number of students in each of three groups.
"""
# The program gets three integers: the number of students in each of three groups:
# student=int(input())
# 1 class
student=int(input())
# Each school desk is for two students
desk=student//2+student%2
# student=int(input())
# 2 class
student=int(input())
# Each school desk is for two students
desk=desk+student//2+student%2
# student=int(input())
# 3 class
student=int(input())
# Each school desk is for two students

desk=desk+student//2+student%2
# print(desk)

print(desk)




