﻿#task1------------------------------------------------------------
"""
Напишіть програму, яка отримує три числа і друкує їх суму. Кожне число користувач вводить у окремому рядку.
"""



a = int(input())
b = int(input())
c = int(input())
print(a + b + c)


#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Напишіть програму, яка отримує довжини двох катетів прямокутного трикутника та виводить його площу. Користувач вводить довжини катетів у окремих рядках.
"""



a=int(input())
b = int(input())
print((a*b)/2)


#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?
"""



n=int(input())
k=int(input())
print(k// n)
print(k% n)



#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Нехай число N - кількість хвилин, відрахованих після півночі. Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?
"""



n=int(input())

n=n%1440

print(n//60,n%60)


#-----------------------------------------------------------------

    
#task5------------------------------------------------------------
"""
Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”
"""


a = str(input())

print("Hello,"+" " +a+"!")



#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

 	
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
"""



a = int(input())

print('The next number for the number ',a,' is ',a+1)

print('The previous number for the number ',a,' is ',a-1)


#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів. Яку мінімальну кількість столів необхідно придбати?
"""

a = int(input())

b = int(input())

c = int(input())

d=(a // 2 + b // 2 + c // 2)

e=(a%2+b%2+c%2)

print (d+e)

#-----------------------------------------------------------------
