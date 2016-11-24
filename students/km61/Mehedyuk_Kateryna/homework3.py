# your co---'For loop with range'--------------------
 #task1
 """Given two integers A and B (A<= B). 
#Print all numbers from A to B inclusively."""
 a=int(input())
b=int(input())
#int, because a, b==numbers
for i in range(a,b+1):
    print(i)
 #task2
 """Given two integers A and B. Print all numbers from A to B inclusively, in increasing order, if A < B, or in decreasing order, if A>= B"""
 a=int(input())
b=int(input())
#int, because a, b==numbers
if a<=b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
#task3
"""10 numbers are given in the input. Read them and print their sum. """
# Use as few variables as you can
sum=0
for i in range(10):
    sum+=int(input())
print(sum)
#task4
"""N numbers are given in the input. Read them and print their sum."""
sum=0
n=int(input())
#int, because n==numbers
for i in range(n):
    sum+=int(input())
print(sum)
#task5
"""For the given integer N calculate the following sum of cubes."""
sum=0
n=int(input())
#int, because n==numbers
for i in range(n+1):
    sum+=i**3
print(sum)
#task6
"""In mathematics, the factorial of of an integer n, denoted by n! is the following product:n!=1*2*…*n"""
# Don't use math module in this exercise
n=int(input())
#int, because n==factorial
sum=1
for i in range(n):
    sum*=i+1
print(sum)
#task7
"""Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it."""
# need to count the number of numbers that are equals to zero, not the number of zero digits
n=int(input())
#int, because n==numbers
sum=0
for i in range(n):
    x=int(input())
    if x==0:
        sum+=1
print(sum)
#task8
"""For given integer n compute the sum 1!+2!+3!+...+n!1!+2!+3!+...+n!."""
#This problem has a solution with only one cycle, so try to discover it. And don't use the math library :)
n=int(input())
sum=0
for i in range(n):
    fact=1
    for j in range(i+1):
        fact*=j+1
    sum+=fact
print(sum)
#task9
"""There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards."""
#Given a number N, then N − 1 integers - numbers on remaining cards (distinct integer in range from 1 to N). Your program should print a number on the lost card
n=int(input())
summ=0 
needed_sum=0
for i in range(n-1):
    summ+=int(input())
    needed_sum+=i+1
needed_sum+=n
print(needed_sum-summ)
#task10
"""For given integer n ? 9 print a ladder of n steps. The k-th step consists of the integers from 1 to i without spaces between them.""" 
#To do that, you can use the sep and end arguments for the function print().
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    print()

de goes here