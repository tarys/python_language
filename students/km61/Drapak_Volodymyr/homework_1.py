#task1------------------------------------------------------------
"""
Умова: Напишіть програму, яка отримує три числа і друкує їх суму. Кожне число користувач вводить у окремому рядку.

Вхідні дані: 3 дійсних числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести суму трьох чисел на екран.
"""


#write your answer here...
"""
# Program reads three real numbers and outputs their sum
# first_number, second_number, third_number - real numbers
# Result is sum of three numbers (real number)

# input
first_number = float(input())
second_number = float(input())
third_number = float(input())

# body
print(first_number + second_number + third_number)
"""

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Умова: Напишіть програму, яка отримує довжини двох катетів прямокутного трикутника та виводить його площу.
Користувач вводить довжини катетів у окремих рядках.

Вхідні дані: 2 дійсних числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести площу трикутника на екран.
"""

#write your answer here...
"""
# Program reads two cathetus of right triangle and outputs area of the triangle
# first_cathethus, second_cathethus - real numbers
# Result is area of triangle (real number)

# input
first_cathethus = float(input())
second_cathethus = float(input())

# body
print(0.5*first_cathethus*second_cathethus)
"""

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Умова: N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику.
Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?

Програма отримує числа N і K. Вона повинна вивести два числа: відповіді на поставлені вище питання.

Вхідні дані: 2 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести два числа. Перше - кількість яблук у студента, друге - кількість яблук, що лишилось у кошику.
"""



#write your answer here...
"""
# Program reads two integer numbers and outputs integer division and remainder of integer division of the first to the second
# N, K - integer numbers
# Results are integer division and remainder of integer division of the first to the second (integer numbers)

# input
N = int(input())
K = int(input())

# body
print(K//N)
print(K%N)
"""

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Умова: Нехай число N - кількість хвилин, відрахованих після півночі.
Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?

Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59).
Візьміть до уваги, що починаючи з півночі може пройти декілька днів, тому число N може бути достатньо великим.

Вхідні дані: 1 ціле число, що вводить користувач

Вихідні дані: вивести два числа. Перше - години, друге - хвилини.
"""



#write your answer here...
"""
# Program reads integer number of minutes since midnight and outputs time that clock should show
# N - number of minutes (integer)
# Result is string that consists of two integer numbers

# input
N = int(input())

# body
print(str(N%1440//60) + " " + str(N%60))
"""

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Умова: Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього.
Наприклад “Hello, Mike!”

Вхідні дані: ім'я користувача

Вихідні дані: вивести рядок привітання
"""



#write your answer here...
"""
# Program reads name of user and outputs sentence-greeting in special format: "Hello, (Name of user)!"
# Result is string

# body
print("Hello, " + input() + "!")
"""

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

The next number for the number 179 is 180.
The previous number for the number 179 is 178.

Вхідні дані: ціле число

Вихідні дані: два рядки за наведеним у завданні форматом.
"""



#write your answer here...
"""
# Program reads integer number and outputs previous and next numbers to this number
# just_number - integer number
# Results are two strings where are written previous and next numbers of read number

# input
just_number = int(input())

# body
print("The next number for the number " + str(just_number) + " is " + str(just_number + 1))
print("The previous number for the number " + str(just_number) + " is " + str(just_number - 1))
"""

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Умова: Школа вирішила сформувати три нові групи учнів та надати їм окремі класи.
У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів.
Яку мінімальну кількість столів необхідно придбати?

Вхідні дані: 3 цілих числа - кількість учнів у кожній групі.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: число - кількість столів
"""



#write your answer here...
"""
# Program outputs the number of desks needed for three classrooms where the desk is only for no more than 2 pupils
# first_number_of_students, second_number_of_students, third_number_of_students - integer numbers
# Result is number of desks (integer number)

# input
first_number_of_students = int(input())
second_number_of_students = int(input())
third_number_of_students = int(input())

# body
print(first_number_of_students//2 + first_number_of_students%2 + second_number_of_students//2 + second_number_of_students%2 +
 + third_number_of_students//2 + third_number_of_students%2)
"""

#-----------------------------------------------------------------