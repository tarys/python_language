#task1------------------------------------------------------------
"""
Умова: Напишіть програму, яка отримує три числа і друкує їх суму. Кожне число користувач вводить у окремому рядку.

Вхідні дані: 3 дійсних числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести суму трьох чисел на екран.
"""
#
a = float(input())

b = float(input())

c = float(input())

print(a + b + c)
#-----------------------------------------------------------------


#task2------------------------------------------------------------


"""
мова: Напишіть програму, яка отримує довжини двох катетів прямокутного трикутника та виводить його площу. Користувач вводить довжини катетів у окремих рядках.

Вхідні дані: 2 дійсних числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести площу трикутника на екран.
"""
#
b = float(input())

h = float(input())

print((b*h)/2)
#------------------------------------------------------------------


#task3-------------------------------------------------------------


"""
Умова: N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?

Програма отримує числа N і K. Вона повинна вивести два числа: відповіді на поставлені вище питання.

Вхідні дані: 2 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести два числа. Перше - кількість яблук у студента, друге - кількість яблук, що лишилось у кошику.
"""
#
n = int(input())

k = int(input())

print(k//n)

print(k%n)
#-------------------------------------------------------------------


#task4--------------------------------------------------------------


"""
Умова: Нехай число N - кількість хвилин, відрахованих після півночі. Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?

Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59). Візьміть до уваги, що починаючи з півночі може пройти декілька днів, тому число N може бути достатньо великим.

Вхідні дані: 1 ціле число, що вводить користувач

Вихідні дані: вивести два числа. Перше - години, друге - хвилини.
"""
#
n=int(input())

if n>=60:
   
  hours=n//60
    
  minutes=n%60

if hours>=24:
    
  days=n//24
    
  hours=hours%24

print(hours, minutes)
#---------------------------------------------------------------------


#task5----------------------------------------------------------------


"""
Умова: Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”

Вхідні дані: ім'я користувача

Вихідні дані: вивести рядок привітання
"""
#
name=input()
print('Hello, ' + name + '!')
#---------------------------------------------------------------------


#task6---------------------------------------------------------------


"""
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

 	
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
Вхідні дані: ціле число

Вихідні дані: два рядки за наведеним у завдання форматом.
"""
#
a=int(input())

print("The next number for the number {0} is {1}".format(a,a+1))

print("The previous number for the number {0} is {1}".format(a,a-1))

#----------------------------------------------------------------------


#task7


"""
Умова: Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів. Яку мінімальну кількість столів необхідно придбати?

Вхідні дані: 3 цілих числа - кількість учнів у кожній групі.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: число - кількість столів
"""
#
a=int(input())

b=int(input())

d=int(input())

if (a%2)==0:
    
  table=a//2

else:
    
  table=(a//2)+1
if(b%2)==0:
    
  table+=b//2 

else:
    
  table+=(b//2)+1

if(d%2)==0:
    
  table+=d//2

else:
    
  table+=(d//2+1)

print (table)
#-------------------------------------------------------------------------


