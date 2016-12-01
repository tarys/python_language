#task1------------------------------------------------------------

"""
Program prints numbers from a to b(a>b)
"""
a=int(input('Enter range start'))
b=int(input('Enter range end'))
print('Numbers from',a,'to',b)
for i in range(a,b+1):
    print(i)

#----------------------------------------------------------------
#task2------------------------------------------------------------

"""
Program prints numbers from a to b or from b to a
"""
a=int(input('Enter range start'))
b=int(input('Enter range end'))
print('Numbers from',a,'to',b)
if a<=b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)

#----------------------------------------------------------------
#task3------------------------------------------------------------

"""
Program prints odd numbers from a to b 
"""
a=int(input('Enter range start'))
b=int(input('Enter range end'))
print('Numbers from',a,'to',b)
for i in range(a,b-1,-1):
    if i%2!=0:
        print(i)

#----------------------------------------------------------------
#task4------------------------------------------------------------

"""
Sum of ten numbers
"""
sum=0
for i in range(10):
    sum+=int(input('Enter number'))
print('Sum of 10 number:',sum)

#----------------------------------------------------------------
#task5------------------------------------------------------------

"""
Sum of  N numbers
"""
sum=0
n=int(input('Enter amount of numbers'))
for i in range(n):
    sum+=int(input('Enter number'))
print('Sum of n numbers:',sum)

#----------------------------------------------------------------
#task6------------------------------------------------------------

"""
Sum of  cubes
"""
sum=0
n=int(input('Enter amount of numbers'))
for i in range(n+1):
    sum+=i**3
print('Sum of cubes from 1 to',n,':',sum)

#----------------------------------------------------------------
#task7------------------------------------------------------------

"""
Factorial
"""
n=int(input('Enter number'))
factorial=1
for i in range(n):
    factorial*=i+1
print('N!=',sum)

#----------------------------------------------------------------
#task8------------------------------------------------------------

"""
The number of  zeros
"""
#Program prints amount of zeros entered by user
n=int(input('Enter amount of numbers'))
amount=0
for i in range(n):
    x=int(input('Enter number'))
    if x==0:
        amount+=1
print('Amount of zeros',amount)

#----------------------------------------------------------------
#task9------------------------------------------------------------

"""
The sum of  the factorials
"""
n=int(input('Enter number'))
sum=0
for i in range(n):
    fact=1
    for j in range(i+1):
        factorial*=j+1
    sum+=factorial
print('Sum of factorials from 1 to',n,'=',sum)

#----------------------------------------------------------------
#task10------------------------------------------------------------

"""
Ladder
"""
n=int(input('Enter amount of stairs'))
print('Ladder')
for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    print()

#----------------------------------------------------------------
#task11------------------------------------------------------------

"""
Lost card
"""
#Program prints number of lost card, numbers on cards must be from 1 to n
n=int(input('Enter amount of cards'))
sum=0 
needed_sum=0
for i in range(n-1):
    sum+=int(input('Enter number on card from 1 to n, without duplicates:'))
    needed_sum+=i+1
needed_sum+=n
print('Lost card',needed_sum-sum)
#----------------------------------------------------------------
