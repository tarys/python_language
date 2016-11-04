print ('Home work №5') 
print() 

 #task1 
 
#input
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
#output
import math
def distance (x1,y1,x2,y2):
    return (math.sqrt((x2-x1)**2+(y2-y1)**2))
print(distance(x1,y1,x2,y2))

#task2
#input
a=float(input())
n=float(input())
def power(a,n):
    if n<0:
        a=1/a
        n=-n
    res=1
    if a==0: return 0
    while n>0: 
        res=res*a
        n=n-1
    return res
#output
print(power(a,n))

#task3 
#input
a = float(input())
n = int(input())
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
#output
print(power(a,n))


#task4 
#input
n = int(input())
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
#output
print(fib(n))





