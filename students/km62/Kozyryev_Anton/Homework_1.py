# -*- coding: utf-8 -*-

"""
    Домашня робота №1
    Тема: "Введення та вивід інформації. Прості операції"
    Студент: Козирєв Антон Юрійович
    Група: КМ - 62
"""


#Task_1----------------------------------------------------#

"""
    Умова: Напишіть програму, яка отримує три числа і друкує їх суму. Кожне число користувач вводить у окремому рядку.
"""

#print("Task #1");
Number_1 = input() #"Enter the first number: "
Number_2 = input() #"Enter the second number: "
Number_3 = input() #"Enter the third number: "
Sum = int(Number_1) + int(Number_2) + int(Number_3) # A + B + C
print(Sum) #"Sum: "
#print("First task complited!")

#---------------------------------------------------------#



#Task_2---------------------------------------------------#

"""
    Умова: Напишіть програму, яка отримує довжини двох катетів прямокутного трикутника та виводить його площу. Користувач вводить довжини катетів у окремих рядках.
"""

#print("Task #2");
Side_1 = input() #"Enter the first side: "
Side_2 = input() #"Enter the second side: "
Square = (int(Side_1) * int(Side_2)) / 2
print(Square) #"Square of tringle: "
#print("Second task complited!");

#---------------------------------------------------------#



#Task_3---------------------------------------------------#

"""
    Умова: N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?
"""

#print("Task #3");
students = input() #"Students: "
apples = input() #"Apples: "
per_student = int(apples) / int(students) #per = per student
extra = int(apples) % int(students) #ext = extra
print(int(per_student)) #"Apples per student: "
print(int(extra)) #"Extra apples: "
#print("Third task complited!");

#---------------------------------------------------------#



#Task_4---------------------------------------------------#

"""
Умова: Нехай число N - кількість хвилин, відрахованих після півночі. Скільки годин і хвилин буде показувати цифровий годинник, якщо за відлік взяти 00:00?

Програма повинна виводити два числа: кількість годин (від 0 до 23) і кількість хвилин (від 0 до 59). Візьміть до уваги, що починаючи з півночі може пройти декілька днів, тому число N може бути достатньо великим.
"""

#print("Task #4");
Time = input() #"Time: "
Min = int(Time) % 60
Hour = (int(Time) // 60) % 24
print(Hour, Min) #"Hours {}, minutes {}"
#print("Fourth task complited!");

#---------------------------------------------------------#



#Task_5---------------------------------------------------#

"""
    Умова: Напишіть програму, яка вітає користувача, друкуючи слово "Hello", ім'я користувача і знак оклику після нього. Наприклад “Hello, Mike!”
"""

#print("Task #5");
name = input() #"Tell me plz your marvelous name: "
print("Hello,", name + "!")
#print("Fifth task complited!");

#---------------------------------------------------------#



#Task_6---------------------------------------------------#

"""
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

The next number for the number 179 is 180.
The previous number for the number 179 is 178.
"""

#print("Task #6")
Current_Number = input() #"Enter your current number: "
Next_Number = int(Current_Number) + 1 #Next number
Previos_Number = int(Current_Number) - 1 #Previous number
print("The next number for the number", Current_Number,"is" , Next_Number) 
print("The previous number for the number", Current_Number,"is" , Previos_Number) 
#print("Sixth task complited!")

#---------------------------------------------------------#



#Task_7---------------------------------------------------#

"""
Умова: Школа вирішила сформувати три нові групи учнів та надати їм окремі класи. У кожному класі необхідно встановити столи для учнів, у розрахунку, що за одним столом може сидіти не більше двох учнів. Яку мінімальну кількість столів необхідно придбати?
"""

#print("Task #7");
Amount_of_students1 = input();#"Enter the amount of students from first group: "
Amount_of_students2 = input();#"Enter the amount of students from second group: "
Amount_of_students3 = input();#"Enter the amount of students from third group: "

Extra = int(Amount_of_students1) % 2; # Extra desk for student (if student / mod = 1)
Desks_for_group1 = int(Amount_of_students1) // 2 + Extra;

Extra = int(Amount_of_students2) % 2; # Extra desk for student (if student / mod = 1)
Desks_for_group2 = int(Amount_of_students2) // 2 + Extra;

Extra = int(Amount_of_students3) % 2; # Extra desk for student (if student / mod = 1)
Desks_for_group3 = int(Amount_of_students3) // 2 + Extra;

print(Desks_for_group1 + Desks_for_group2 + Desks_for_group3);
#print("Seventh task complited!")

#---------------------------------------------------------#
