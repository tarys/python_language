#task1------------------------------------------------------------
"""
Задача №1 
Умова: Напишіть програму, яка отримує три числа і друкує їх суму. Кожне число користувач вводить у окремому рядку.
Вхідні дані: 3 дійсних числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести суму трьох чисел на екран.
"""
a = float(input())
b = float(input())
c = float(input())
z = a+b+c
print(z)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Задача №2
Умова: Напишіть програму, яка отримує довжини двох катетів прямокутного трикутника та виводить його площу. Користувач вводить довжини катетів у окремих рядках.
Вхідні дані: 2 дійсних числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести площу трикутника на екран.
"""

a=float(input())
b=float(input())

print(a*b*0.5)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Задача №3 
Умова: N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?
Програма отримує числа N і K. Вона повинна вивести два числа: відповіді на поставлені вище питання.
Вхідні дані: 2 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести два числа. Перше - кількість яблук у студента, друге - кількість яблук, що лишилось у кошику.
"""

N=int(input())
K=int(input())
print(K//N)	
print(K-(K//N)*N)


#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Задача №4 
Умова: Нехай число N - кількість хвилин, відрахованих після півночі. Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?
Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59). Візьміть до уваги, що починаючи з півночі може пройти декілька днів, тому число N може бути достатньо великим.
Вхідні дані: 1 ціле число, що вводить користувач
Вихідні дані: вивести два числа. Перше - години, друге - хвилини.
"""
a=int(input())
b= int(a//60)
c= int(b//24)
print(b-(c*24))
print(a-(b*60))
 
#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Задача №5 
Умова: Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”
Вхідні дані: ім'я користувача
Вихідні дані: вивести рядок привітання
"""

n=str(input(“Enter your name “))
print(“Hello”+” “+n+”!”)
 

#-----------------------------------------------------------------



#task6------------------------------------------------------------
"""
Задача №6 
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:
 The next number for the number 179 is 180.
The previous number for the number 179 is 178.Вхідні дані: ціле число
Вихідні дані: два рядки за наведеним у завдання форматом.
"""
a=int(input())
b= str(a+1)
c= str(a-1)
q=str(a)
print(“The next number for the number ”+q+” is “ + b)
print(“The previos number for the number ”+q+” is “ + c)
 
	
#-----------------------------------------------------------------



#task7------------------------------------------------------------
"""
Задача №7
Умова: Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів. Яку мінімальну кількість столів необхідно придбати?
Вхідні дані: 3 цілих числа - кількість учнів у кожній групі.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: число - кількість столів
"""
a=int(input())
b=int(input())
c=int(input())
q=float(a//2)
w=float(b//2)
e=float(c//2)
print(a%2+b%2+c%2+q+w+e)
 

#-----------------------------------------------------------------
