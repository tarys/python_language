#task1--------------------------------------------------------------------
'''
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию
distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и
(x2,y2). Считайте четыре действительных числа и выведите результат работы
этой функции. 
'''

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
def distance(x1,y1,x2,y2):
    dis=((x2-x1)**2+(y2-y1)**2)**(1/2)
    return dis
print (distance(x1,y1,x2,y2))
    
#--------------------------------------------------------------------------


#task2---------------------------------------------------------------------
'''
Дано действительное положительное число a и целоe число n.
Вычислите a^n. Решение оформите в виде функции power(a, n). 
'''

def neg_degree(a,n):
    if n<0:
        res=1/(a**abs(n))
        return res
    else:
        res=a**n
        return res
print(neg_degree(float(input()), float(input())))
    
#--------------------------------------------------------------------------


#task3---------------------------------------------------------------------
'''
Дано действительное положительное число a и целое неотрицательное число n.
Вычислите an не используя циклы, возведение в степень через ** и функцию
math.pow(), а используя рекуррентное соотношение a^n=a⋅a^(n-1).
Решение оформите в виде функции power(a, n). 
'''

def power(a,n):
    res=1
    for i in range (1,n+1):
        res=res*a
    return res
print(power(float(input()),int(input())))

#--------------------------------------------------------------------------


#task4----------------------------------------------------------------------
'''
Напишите функцию fib(n), которая по данному целому неотрицательному n
возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы —
используйте рекурсию. 
'''
   
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = int(input())
print(fib(n))
            
#---------------------------------------------------------------------------
