#task1------------------------------------------------------------
"""
Умова: Напишіть програму, яка отримує три числа і друкує їх суму. Кожне число користувач вводить у окремому рядку.

Вхідні дані: 3 дійсних числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести суму трьох чисел на екран.
"""
num_one = float(input())
num_two = float(input())
num_three = float(input())
print(num_one + num_two + num_three)
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Умова: Напишіть програму, яка отримує довжини двох катетів прямокутного трикутника та виводить його площу. Користувач вводить довжини катетів у окремих рядках.

Вхідні дані: 2 дійсних числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести площу трикутника на екран.
"""
hyp = float(input())
high = float(input())
print((hyp * high) / 2)
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
print(k // n)
print(k % n)
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Умова: Нехай число N - кількість хвилин, відрахованих після півночі. Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?

Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59). Візьміть до уваги, що починаючи з півночі може пройти декілька 
днів, тому число N може бути достатньо великим.

Вхідні дані: 1 ціле число, що вводить користувач

Вихідні дані: вивести два числа. Перше - години, друге - хвилини.
"""
n = int(input())
print((n // 60) % 24, n % 60)
#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Умова: Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”

Вхідні дані: ім'я користувача

Вихідні дані: вивести рядок привітання
"""
name = input()
print("Hello,",name + "!")
#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

	The next number for the number 179 is 180.
	The previous number for the number 179 is 178.

Вхідні дані: ціле число

Вихідні дані: два рядки за наведеним у завдання форматом.
"""
number = int(input())
print("The next number for the number", number,"is", number + 1)
print("The previous number for the number", number,"is", number - 1)
#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Умова: Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом 
може сидіти не більше двох учнів. Яку мінімальну кількість столів необхідно придбати?

Вхідні дані: 3 цілих числа - кількість учнів у кожній групі.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: число - кількість столів
"""
group1 = int(input())
group2 = int(input())
group3 = int(input())
print(((group1 + group2 + group3) // 2) + ((group1 + group2 + group3) % 2))
#-----------------------------------------------------------------





