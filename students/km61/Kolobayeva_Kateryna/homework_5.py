#Длина отрезка_1
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
"""
#Program calculates length of line:
from math import sqrt
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
#print(distance(x1, x2, y1, y2))
print(distance(x1, x2, y1, y2))
#Отрицательная степень_2
"""
Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
"""
#Program calculates power of number:
def power(a,n):
    original_number=a
    if n<0:
        for i in range(1,n,-1):
            a/=original_number
    elif n>0:
        for i in range(1,n):
             a*=original_number
    else:
         a=1
    return a
a=float(input())
n=int(input())
#print(power(a,n))
print(power(a,n))

#Большие буквы_3
"""
Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же, меняя первую букву на большую.
Например, print(capitalize('word')) должно печатать слово Word.
На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских букв. Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы. При этом используйте вашу функцию capitalize().
Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII, и функция chr(), которая по коду символа возвращает сам символ. Например, ord('a') == 97, chr(97) == 'a'.
"""
#Print function, which takes the word of small letters and returns the same, changing the first letter of the great:
a = input()
def capitalize(str):
    str = str.title()
    return str
print( capitalize(a) )
#Возведение в степень_4
"""
Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.
Решение оформите в виде функции power(a, n).
"""
#Program calculates power of number with recursion:
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
#print(power(float(input()), int(input())))
print(power(float(input()), int(input())))

#Числа Фибоначчи_5
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче нельзя использовать циклы — используйте рекурсию.
"""
#Program calculates Fibonachi number with recursion:
def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
#print(fib(n))
print(fib(n))
