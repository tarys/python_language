# your code ---'Input, print and numbers'---------------------------------------------------------

#task1
"""Write a program that takes three numbers and prints their sum. """
#Every number is given in a separate line
a = int(input()) 
b = int(input()) 
# int, because a, b, c==numbers
c = int(input())
print(a+b+c)
#task2
"""Write a program that reads the two lengths of the base and the height in the right triangle and prints its area. """
#Every number is given in a separate line
b = int(input())
h = int(input())
# int, because h, b,==numbers

print(0.5*b*h)
#task3
"""N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will get each single student? How many apples will remain in the basket?"""
#Program gets the numbers N and K
n=int(input())
k=int(input())
# int, because k, n==numbers

#n!=0
print(k//n)
print(k%n)
#task4
"""Given the integer N - how many minutes are passed since some midnight. How many hours and minutes are displayed on the 24h digital clock?"""
# Program should print the two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).
minute=int(input())
minute=minute%1440
print(minute//60, minute%60)
#task5
"""Write a program that greets the user by printing the word "Hello", the name of the user and the exclamation mark after it."""
# See the examples below
name = input()
print('Hello'+ ', '  + name + '!')
#task6
"""Write a program that reads an integer number and prints its previous and next numbers. See the examples below. Remember that you can convert the numbers to strings using the function str."""
a = int(input())
# int, because a==number
print('The next number for the number '+ a + ' is '+a+1 '.')
print('The previous number for the number ' + a + ' is '+ '.')
#task7
"""One school decided to form three new groups and furnish the individual classrooms for each of them. Each school desk is for two students. Given the number of students in each group, print the smallest possible number of school desks that should be purchased."""
# program gets three integers: the number of students in each of three groups
student=int(input())
desk=student//2+student%2
student=int(input())
desk=desk+student//2+student%2
student=int(input())
desk=desk+student//2+student%2
print(desk)
goes here