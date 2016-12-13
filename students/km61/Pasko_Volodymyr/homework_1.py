#task1------------------------------------------------------------
"""
Напишіть програму, яка отримує три числа і друкує їх суму. Кожне число користувач вводить у окремому рядку.
"""

# program printing the sum of three entered numbers
print()
print()
print("Enter the first number: ")
number_1 = int(input())
print("Enter the second number: ")
number_2 = int(input())
print("Enter the third number: ")
number_3 = int(input())

sum = number_1 + number_2 + number_3;

print("The sum is ", sum)

#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
Напишіть програму, яка отримує довжини двох катетів прямокутного трикутника та виводить його площу. Користувач вводить довжини катетів у окремих рядках.
"""

#The program which calcutates the area of right angled triangle using the value of its two sides

print("Define the two sides of righ tangled triangle: ")
print("Side 1: ")
side_1 = int(input())
print("Side 2: ")
side_2 = int(input())
area = (side_1 * side_2) / 2
print("The area of your triangle is ", area)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?
"""
#program dividing the apples beween the students
print()
print("Enter the quantity of students: ")
quantity_of_students = int(input())
print("Enter the quantity of apples: ")
quantity_of_apples = int(input())
apple_for_student = quantity_of_apples // quantity_of_students
apple_in_bag = quantity_of_apples % quantity_of_students
print("Each student will get the", apple_for_student, "apples")
print(apple_in_bag, " apples will stay in the bag")


#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
Нехай число N - кількість хвилин, відрахованих після півночі. Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?
"""
# Program transforming the number into hours and minutes 
import math
number_to_transform = int(input("Enter the number for transforming into hours and minutes: "))
Hours = number_to_transform // 60
Minutes = number_to_transform % 60
print(Hours, " Hours ", Minutes, " Minutes")

#-----------------------------------------------------------------

#task5------------------------------------------------------------
"""
Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”
"""
# program greeting the user 
users_name = input("Enter your name: ")
print("Hello," , users_name + "!") 

#-----------------------------------------------------------------

#task6------------------------------------------------------------

"""
Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:
"""
#program which, according to the number, prints the next and previous number
origin_number = int(input("Enter the number: "))
print()
print ("The next number for the number", origin_number, " is", origin_number + 1)
print()
print ("The previos number for the number", origin_number, "is", origin_number - 1)

#-----------------------------------------------------------------

#task7------------------------------------------------------------
"""
Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів. Яку мінімальну кількість столів необхідно придбати?
"""
# program counting the minimal amount of tables for students of three groups
print("Enter the quantity of the first group: ")
group_1 = int(input())
print("Enter the quantity of the second group: ")
group_2 = int(input())
print("Enter the quantity of the third group: ")
group_3 = int(input())

tables = ((group_1 + group_2 + group_3) // 2) + 1
print ("You need to buy ", tables, " tables")

#-----------------------------------------------------------------










