#task1------------------------------------------------------------
"""
	Write a program that takes three numbers and prints their sum.
	Every number is given in a separate line.
"""



# This program read three numbers and prints their sum:
first_number = int(input())
second_number = int(input())
third_number= int(input())
sum=(first_number+second_number+third_number)
print(sum)
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
	Write a program that reads the two lengths of the base and the height in the right triangle and prints its area.	
	Every number is given in a separate line.
"""



# program of calculating the area of triangle:
b = int(input()) #base of rectangle
h = int(input()) #height of rectangle
print(b*h*0.5) #area of triangle
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
	N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. 
	How many apples will get each single student? How many apples will remain in the basket?
	The program gets the numbers N and K. It should print the two numbers: answers for the questions above
"""



'''
    program of calculation how many apples 
    will get each single student and how many 
    apples will remain in the basket
    
    N-students and K-aplles
'''
N = int(input())
K = int(input())
print(K//N) # how many apples will get each single student
print(K%N) #how many apples will remain in the basket
#-----------------------------------------------------------------


#task4------------------------------------------------------------
'''
	Given the integer N - how many minutes are passed since some midnight. How many hours and minutes are displayed on the 24h digital clock?
	The program should print the two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59). 
	Take into account that the starting midnight could be several days ago, so the number N can be substantially big.
'''



# program print the number of hours and minutes
# N - how many minutes are passed since midnight
N = int(input())
N=N%1440 # go out 1440 minutes
print(N//60,N%60) # print hours and minutes
#-----------------------------------------------------------------


#task5------------------------------------------------------------
'''
	Write a program that greets the user by printing the word "Hello", 
	the name of the user and the exclamation mark after it. See the examples below.
'''


# program print "Hello, 'name'!"
# name-user input
name = input()
print('Hello'+ ', '  + name + '!')
#-----------------------------------------------------------------



#task6------------------------------------------------------------
'''
	Write a program that reads an integer number and prints its previous and next numbers. See the examples below. 
	Remember that you can convert the numbers to strings using the function str.
'''


# program that reads an integer number
# and prints its previous and next numbers
number = int(input())
print('The next number for the number '+ str(number) + ' is ' + str(number+1) + '.')
print('The previous number for the number ' + str(number) + ' is '+ str(number-1) + '.'  )
#-----------------------------------------------------------------



#task7------------------------------------------------------------
'''
	One school decided to form three new groups and furnish the individual classrooms for each of them. 
	Each school desk is for two students. Given the number of students in each group, 
	print the smallest possible number of school desks that should be purchased.
	The program gets three integers: the number of students in each of three groups.
'''


# program of calculating how many school desks 
# we need to N students (of three groups)
student=int(input()) # first group
desk=student//2+student%2
student=int(input()) # second group
desk=desk+student//2+student%2
student=int(input()) # third group
desk=desk+student//2+student%2
print(desk)
#-----------------------------------------------------------------
