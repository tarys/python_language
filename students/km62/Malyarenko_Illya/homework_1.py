#task1------------------------------------------------------------
"""
Умова: Напишіть програму, яка отримує три числа і друкує їх суму. Кожне число користувач вводить у окремому рядку.

Вхідні дані: 3 дійсних числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести суму трьох чисел на екран.
"""

a = int(input())
b = int(input())
c = int(input())
print(a+b+c)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Умова: Напишіть програму, яка отримує довжини двох катетів прямокутного трикутника та виводить його площу. Користувач вводить довжини катетів у окремих рядках.

Вхідні дані: 2 дійсних числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести площу трикутника на екран.
"""

h = int(input())
b = int(input())
print(1/2*b*h)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Умова: N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?

Програма отримує числа N і K. Вона повинна вивести два числа: відповіді на поставлені вище питання.

Вхідні дані: 2 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести два числа. Перше - кількість яблук у студента, друге - кількість яблук, що лишилось у кошику.
"""

n = int(input())
k = int(input())
print(k//n)
print(k-(k//n)*n)

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Умова: Нехай число N - кількість хвилин, відрахованих після півночі. Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?

Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59). Візьміть до уваги, що починаючи з півночі може пройти декілька днів, тому число N може бути достатньо великим.

Вхідні дані: 1 ціле число, що вводить користувач

Вихідні дані: вивести два числа. Перше - години, друге - хвилини.
"""

n=int(input())
print((n//60)-24*(n//(24*60)))
print(n-60*(n//60))

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Умова: Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”

Вхідні дані: ім'я користувача

Вихідні дані: вивести рядок привітання
"""

n=str(input())
print("Hello, "+n+"!")

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

 	
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
Вхідні дані: ціле число

Вихідні дані: два рядки за наведеним у завдання форматом.
"""

n=int(input())
print("The next number for the number "+str(n)+" is "+str(n+1))
print("The previous number for the number "+str(n)+" is "+str(n-1))

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Умова: Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів. Яку мінімальну кількість столів необхідно придбати?

Вхідні дані: 3 цілих числа - кількість учнів у кожній групі.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: число - кількість столів
"""

g1=int(input())
g2=int(input())
g3=int(input())
dg1=(g1//2)+(g1-2*(g1//2))
dg2=(g2//2)+(g2-2*(g2//2))
dg3=(g3//2)+(g3-2*(g3//2))
print(dg1+dg2+dg3)

#-----------------------------------------------------------------


