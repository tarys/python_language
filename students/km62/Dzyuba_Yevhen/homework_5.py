#Дзюба Євген км-62 дз№5
#1)спосіб 1 
from math import sqrt
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print(distance(x1, x2, y1, y2))
#2способ 
x1 = float(input())
y1 = float(input())
x2= float(input())
y2= float(input())
S = ((x2-x1)**2+(y2-y1)**2)**(1/2)
print (S)
#2)	
def power(a,n):
    res=a**n
    return res
print(power(float(input()),float(input())))
#3)	
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(float(input()), int(input())))

#4)	
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = int(input())
print(fib(n))
