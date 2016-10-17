#task1------------------------------------------------------------
"""
Напишіть програму, яка отримує три числа і друкує їх суму. Кожне 
число користувач вводить у окремому рядку.
"""
print('Program that takes three numbers and prints their sum')
num_1 = int(input('Value №1:'))
num_2 = int(input('Value №2:'))
num_3 = int(input('Value №3:'))
print(num_1 + num_2 + num_3)
#---------------------------------------------------------------

#task2------------------------------------------------------------
"""
Напишіть програму, яка отримує довжини двох катетів прямокутного 
трикутника та виводить його площу. Користувач вводить довжини 
катетів у окремих рядках.
"""
print('Program that reads the two lengths of the base and the height in the\
right triangle and prints its area')
height = int(input('Cathetus 1:'))
base = int(input('Cathetus 2:'))
print(0.5 * height * base)
#---------------------------------------------------------------

#task3------------------------------------------------------------
"""
N студентів отримали K яблук і розподілити їх між собою порівну. 
Неподілені яблука залишились у кошику. Скільки яблук отримає кожен
студент? Скільки яблук залишиться в кошику?
"""
print("Program gets the numbers N and K. It should print the two numbers: an\
swers for the questions above.")
students = int(input("Students:"))
apples = int(input("Apples:"))
print(apples // students, apples % students)
#---------------------------------------------------------------

#task4------------------------------------------------------------
"""
Нехай число N - кількість хвилин, відрахованих після півночі. 
Скільки годин і хвилин буде показувати цифровий годинник, 
якщо за відлік взяти 00:00?
"""
print("Digital Clock")
minutes = int(input("Enter a number of minutes:"))
hours = minutes // 60
hours = hours % 24
minutes = minutes - hours * 60
#---------------------------------------------------------------

#task5------------------------------------------------------------
"""
Напишіть програму, яка вітає користувача, друкуючи слово "Hello", 
ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”
"""
name = input("What is your name?")
print('Hello,%s!' %(name))
#---------------------------------------------------------------

#task6------------------------------------------------------------
"""
Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:
	The next number for the number 179 is 180.
	The previous number for the number 179 is 178.
"""
num = int(input("Enter a number"))
print('The next number for the number %s is %s' % (num, num+1))
print('The previous number for the number %s is %s' % (num, num-1))
#---------------------------------------------------------------

#task7------------------------------------------------------------
"""
Школа вирішила сформувати три нові групи учнів та надати їм окремі 
класи. У кожному класі необхідно встановити столи для учнів, у 
розрахунку, що за одним столом може сидіти не більше двох учнів. 
Яку мінімальну кількість столів необхідно придбати?
"""
tables = 0
students = int(input("First class"))
tables += students // 2 + students % 2
students = int(input("Second class"))
tables += students // 2 + students % 2
students = int(input("Third class"))
tables += students // 2 + students % 2
print(tables)
#---------------------------------------------------------------
