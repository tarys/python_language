#task1------------------------------------------------------------

"""
Program prints squares from 1 to n 
"""
n=int(input('Enter number'))
i=1
print('Squares from 1 to n:')
while i*i<=n: 
 print(i*i)
 i+=1
#---------------------------------------------------------------- 
#task2------------------------------------------------------------

"""
Program prints minimum devider for n 
"""
n=int(input('Enter number'))
devider=2
while n%devider!=0:
 devider+=1
print('Minimum divider for n=',devider)

#----------------------------------------------------------------
#task3------------------------------------------------------------

"""
Program prints 2 in max involution<=n 
"""
n=int(input('Enter number'))
involution=0
while 2**involution<=n:
 involution+=1
if 2**involution>=n:
 involution=involution-1
print('Max ivlolution of 2=',involution,'2 in max involution<=n:',2**involution)
#----------------------------------------------------------------
#task4------------------------------------------------------------

"""
Program prints number of day on which the running athlete is not less than y kilometers.

"""
x=int(input('Enter how much fif the athlete run in the first day'))
y=int(input('Enter how much he must run'))
day=1
while x<y:
    x+=x*0.1
    day+=1
print('Number of day on which the running athlete is not less than y kilometers:',day)
#----------------------------------------------------------------
#task5------------------------------------------------------------

"""
Program prints year on which contribution is not less than y rubles.
"""
x=int(input('Enter bank deposit'))
p=int(input('Enter percent'))
y=int(input('Enter needed sum'))
year=0
while x<y:
    x+=x*p/100
    x=int(x*100)
    x=float(x/100)
    year+=1
print('Year on which contribution is not less than y rubles',year)
#----------------------------------------------------------------
#task6------------------------------------------------------------

"""
Program calculates sum of sequence

"""
a=1
sum=0
while a!=0:
    a=int(input('Enter number in sequence'))
    sum+=a
print('Sum of sequence',sum)
#----------------------------------------------------------------
#task7------------------------------------------------------------

"""
Program calculates the average value of the sequence
"""
sum=0
amount=0
while True:
    a=int(input('Enter number in sequence'))
    if a==0:
        break
    sum+=a
    amount+=1
print('The average value of the sequence=',sum/amount)

«Максимум последовательности»
#Program prints maximum of sequence
max=0
while True:
    a=int(input('Enter number of sequence'))
    if a==0:
       break
    if a>max:
       max=a
print('maximum of sequence',max)
#----------------------------------------------------------------
#task8------------------------------------------------------------

"""
Program prints index of maximum of sequence
max=0
amount=0
id=1
while True:
    a=int(input('Enter number in sequence'))
    if a==0:
       break
   amount+=1
   if max<a:
       max=a
       id=amount-1
print('index of maximum of sequence',id)
#----------------------------------------------------------------
#task9------------------------------------------------------------

"""
Program prints amount of even elements in sequence
"""
amount=0
while True:
   a=int(input('Enter number in sequence'))
   if a==0:
      break
   if a%2==0:
       amount+=1
print('amount of even elements in sequence',amount)
#----------------------------------------------------------------
#task10------------------------------------------------------------

"""
Program prints amount of elements bigger then previous
"""
amount=0
a=int(input('Enter number in sequence'))
while True:
   b=a
   a=int(input('Enter number in sequence'))
   if a==0:
       break
   if a>b:
       amount+=1
print('amount of elements bigger then previous',amount)
#----------------------------------------------------------------
#task11------------------------------------------------------------

"""
Program prints second maximum in sequence

"""
a=int(input('Enter number in sequence'))
max=a
second_max=0
while a!=0:
    a=int(input('Enter number in sequence'))
    if a>max:
        second_max=max
        max=a
    if a>second_max and a<max:
        second_max=a
print('second maximum in sequence',second_max)
#----------------------------------------------------------------
#task12------------------------------------------------------------

"""
Program prints amount of elements equal to maximum 
a=int(input('Enter number in sequence'))
amount=1
max=a
while a!=0:
    a=int(input('Enter number in sequence'))
    if a==max:
        amount+=1
    if a>max:
        max=a
        amount=1
print('amount of elements equal to maximum',amount)
#----------------------------------------------------------------
#task13------------------------------------------------------------

"""
Program prints number of fibonachi sequence
"""
a,b=0,1
n=int(input('Enter number of fibonachi sequence'))
for i in range(1,n+1):
    a,b=b,a+b
print('number of fibonachi sequence',a)
#----------------------------------------------------------------
#task14------------------------------------------------------------

"""
Program prints index of number of fibonachi sequence
"""
a=0
b=1
c=0
n=0
A=int(input('Enter number of fibonachi sequence'))
while a<A:
    c=b
    b=a+b
    a=c
    n+=1
if a==A:
    print('index of number of fibonachi sequence',n)
else:
    print('Entered number is not a number of fibonachi sequence')
#----------------------------------------------------------------	
#task15------------------------------------------------------------

"""
Program prints the maximum number of consecutive equal elements
"""
amount=1
max=1
a=int(input('Enter number in sequence'))
while a!=0:
    b=a
    a=int(input('Enter number in sequence'))
    if b==a:
        amount+=1
    elif amount>max:
        max=amount
        amount=1
    else:
        amount=1
print('the maximum number of consecutive equal elements',max)

#----------------------------------------------------------------
#task15------------------------------------------------------------

"""
Program calculates standard deviation of sequence
"""
import math
a=int(input('Enter number in sequence'))
amount=1
sum=a
res=0
square_sum=a*a
while a!=0:
    a=int(input('Enter number in sequence'))
    amount+=1
    sum+=a
    square_sum+=a*a
amount+=-1
s=sum/amount
res=math.sqrt((square_sum-2*s*sum+amount*s*s)/(amount-1))
print('standard deviation of sequence',res)
#----------------------------------------------------------------