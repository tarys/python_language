'''
program1
Даны четыре действительных числа: x1, y1, x2, y2.
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2).
Считайте четыре действительных числа и выведите результат работы этой функции.
'''
import math
def distance(x1,y1,x2,y2):
    gipot = (x1-x2)**2 + (y1-y2)**2
    res = math.sqrt(gipot)
    return res
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print (distance(x1,y1,x2,y2))


'''
program2
Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
'''
def power(a,n) :
    res = 1
    for i in range(abs(n)) :
       res *= a
    if n < 0 :
        res = 1/res
    return res
a = float(input())
n = int(input())
print(power(a,n))



'''
program3
Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же,
меняя первую букву на большую.
Например, print(capitalize('word')) должно печатать слово Word.
На вход подаётся строка, состоящая из слов, разделённых одним пробелом.
Слова состоят из маленьких латинских букв.
Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы.
При этом используйте вашу функцию capitalize().
'''
def capitalize(word):
    chars = [c for c in word]
    if ord(chars[0]) in range(97,123):
        chars[0]= chr(ord(chars[0])-32)
    word = ''.join(chars)
    return  word

words =input().split()
for i in range(len(words)):
    words[i] = capitalize(words[i])
print(str(' ').join(words))

'''
program4
Дано действительное положительное число a и целое неотрицательное число n.
Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(),
а используя рекуррентное соотношение an=a⋅an-1.
'''
def power(a,n):
    if n == 0:
        return 1
    else :
        return a*power(a,n-1)

a =float(input())
n= int(input())
print(power(a,n))

'''
program5
Дана последовательность целых чисел, заканчивающаяся числом 0.
Выведите эту последовательность в обратном порядке.
При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных.
Рекурсия вам поможет.
'''
def printNextNumber():
    a = int(input())
    if a != 0 :
        printNextNumber()
    print(a)

printNextNumber()    

'''
program6
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
В этой задаче нельзя использовать циклы — используйте рекурсию.
'''
def fib(n):
    if n == 0 :
        return 0
    elif n == 1 or n == 2  :
        return 1
    else :
        return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))
