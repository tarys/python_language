#task1-----------------------
"""
Даны четыре действительных числа: x1, y1, x2, y2.
 Напишите функцию distance(x1, y1, x2, y2),
 вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
 Считайте четыре действительных числа и выведите результат работы этой функции.
"""
import math
def distance(x1, y1, x2, y2):
	dis = 0
	dis = math.sqrt((x2-x1)**2+(y2-y1)**2)
	return dis
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
dis = distance(x1, y1, x2, y2)
print(dis)
#----------------------------
#task2-----------------------
"""
Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
"""
def power(a, n):
	res = 1
	for i in range(abs(n)):
		res *= a
	if n >= 0:
		return res
	else:
		return 1/res
a = float(input())
n = int(input())
print(power(a, n))
#----------------------------
#task3-----------------------
"""
Дано действительное положительное число a и целое неотрицательное число n.
 Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(),
 а используя рекуррентное соотношение an=a?an-1.
"""
def power(a, n):
	if n == 0:
		return 1
	else:
		return a * power(a, n - 1)
a = float(input())
n = int(input())
print(power(a, n))
#----------------------------

#task4-----------------------
"""
Напишите функцию fib(n),
 которая по данному целому неотрицательному
 n возвращает n-e число Фибоначчи.
"""
def fib(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)
n = int(input())
print(fib(n))
