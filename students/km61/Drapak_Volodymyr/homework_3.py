#task1------------------------------------------------------------
"""
Факторіалом числа n називається добуток 1 × 2 × ... × n. Позначення: n!.
По даному натуральному n обисліть значення n!. Користуватися математичною бібліотекою math в цій задачі забороняється.
"""



#write your answer here...
"""
# Program calculates factorial from n
# n - integer
# Result is factorial of n (integer)

# input
n = int(input())

# body
for i in range(1, n):
    n = n*i
print(n)
"""

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
По даному натуральному n обчисліть суму 1!+2!+3!+...+n!.
При розв'язанні цієї задачі можна використати лише один цикл. Користуватися математичною бібліотекою math в цій задачі забороняється.
"""



#write your answer here...
"""
# Program calculates sum of factorials from 1! to n!
# n - integer
# Result is sum of factorials (integer)

# default
factorial_from_n = 1
sum_of_factorials = 0

# input
n = int(input())

# body
for i in range(n):
    factorial_from_n = factorial_from_n*(i + 1)
    sum_of_factorials += factorial_from_n
print(sum_of_factorials)
"""

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано N чисел: спочатку вводиться число N, потім вводиться рівно N цілих чисел.
Підрахуйте кількість нулів серед введених чисел і виведіть цю кількість.
Вам потрібно порахувати кількість чисел, рівних нулю, а не кількість цифр.
"""



#write your answer here...
"""
# Program count number of zeros among N numbers
# Every number is integer
# Result is count of zeros (integer)

# default
zeros_counter = 0

# input
N = int(input())

# body
for i in range(N):
    zeros_counter += (int(input()) == 0)
print(zeros_counter)
"""

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
По даному натуральному n ≤ 9 виведіть сходинки з n сходинок, i-а сходинка складається з чисел від 1 до i без пробілів.
"""



#write your answer here...
"""
# Program outputs stairs of numbers
# n - stair number
# Result is n strings-stairs

# input
n = int(input())

# body
for i in range(n):
    s = ""
    for j in range(i + 1):
        s += str(j + 1)
    print(s)
"""

#-----------------------------------------------------------------