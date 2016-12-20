Series - 1
"""
Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.
"""
# Read an integer:
# a = int(input())
a=int(input())

# b = int(input())
b=int(input())

# Print a value:
for i in range(a,b+1):
# print(i)
	print(i)
Series - 2
"""
Given two integers A and B. Print all numbers from A to B inclusively, in increasing order, if A < B, or in decreasing order, if A ≥ B.
"""
# Read an integer:
# a = int(input())
a=int(input())

# b = int(input())
b=int(input())

if a<=b:
# if A < B
# Print a value
	for i in range(a,b+1):
# print(i)
   	print(i)
else:
# if A ≥ B
# Print a value
	for i in range(a,b-1,-1):
# print(i)
    	print(i)

Series - 3
"""
Given two integers A and B, A> BA> B. Bring all the odd numbers from A to B inclusive. In this task, you can do without if statement.
"""
# Read an integer:
# a = int(input())
a=int(input())

# b = int(input())
b=int(input())
# Print a value:
for i in range(a,b-1,-1):
    if i%2!=0:
# print(i)
        print(i)

Sum of ten numbers
"""
10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.
"""
#Read them and print their sum:
sum=0
for i in range(10):
# Print a value:
	sum+=int(input())
# print(sum)
print(sum)
Sum of N numbers
"""
N numbers are given in the input. Read them and print their sum.
"""
#Read them and print their sum:
sum=0
# n=int(input())
n=int(input())
# Print a value:
for i in range(n):
	sum+=int(input())
# print(sum)
print(sum)


Sum of cubes
"""
For the given integer N calculate the following sum:1^3+2^3+3^3+...+n^3.
"""
#Calculate the following sum:
sum=0
# n=int(input())
n=int(input())
# Print a value
for i in range(n+1):
	sum+=i**3
# print(sum)
print(sum)





Factorial
"""
In mathematics, the factorial of of an integer nn, denoted by n!n! is the following product:
n!=1×2×…×nn!=1×2×…×n
For the given integer nn calculate the value n!n!. Don't use math module in this exercise.

"""
#Calculate the amount of:
# n=int(input())
n=int(input())
#Read them and print their sum
sum=1
# Print a value
for i in range(n):
	sum*=i+1
# print(sum)
print(sum)

The sum of the factorials 
"""
For given integer nn compute the sum 1!+2!+3!+...+n!1!+2!+3!+...+n!

"""
#Calculate the amount of:
# n=int(input())
n=int(input())
#Read them and print their sum
sum=0
# Print a value
for i in range(n):
	fact=1
# Print a value

	for j in range(i+1):
    # Print a value
	fact*=j+1
	sum+=fact
# print(sum)
print(sum)


The number of zeros  
"""
Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.
You need to count the number of numbers that are equals to zero, not the number of zero digits.
 """
#Calculate the amount of:
# n=int(input())
n=int(input())
#Read them and print their sum
sum=0
# Print a value
for i in range(n):
	x=int(input())
	if x==0:
#x=0
    	sum+=1
# print(sum)
print(sum)






Ladder 
"""
For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to i without spaces between them. To do that, you can use the sep and end arguments for the function print().
"""
# Print a ladder of n steps:
# n=int(input())
n=int(input())
# Print a value
for i in range(1, n + 1):
# Print a value
    for j in range(1, i + 1):
# print(j, sep='', end='')
        print(j, sep='', end='')
# print()
	print()

Lost card
"""
There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.
Given a number N, then N − 1 integers - numbers on remaining cards (distinct integer in range from 1 to N). Your program should print a number on the lost card.

"""
# Program should print a number on the lost card:
# n=int(input())
n=int(input())

summ=0
needed_sum=0
# Print a value
for i in range(n-1):
	summ+=int(input())
	needed_sum+=i+1
needed_sum+=n
# print(needed_sum-summ)
print(needed_sum-summ)




