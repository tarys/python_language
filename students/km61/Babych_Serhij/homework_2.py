#task1------------------------------------------------------------
"""
Умова: Дано два цілих числа. Вивести найменше з них.
"""
#програма виводить найбільше з 2 числ
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
if first_number > second_number:
    print('Minimum of two numbers is'second_number)
elif eliffirst_number = second_number:
    print('The numbers are same',first_number)
else:
    print('Minimum of two numbers is',first_number)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Умова: Вивести результат функції sign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..
"""
#Програма порівнює дійне число з нулем за прикладом
#виводить результат 1,-1 або 0
number = float(input('Enter number: '))
if number  > 0:
    print('sign(x) = 1')
elif number == 0:
    print('sign(x) = 0')
else:
    print('sign(x) = -1')



#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Умова: Дано три цілих числа. Вивести найменше з них.
"""
#Програма виводить найменше з 3 цылих числ
number_one = int(input('Enter number one: '))
number_two = int(input('Enter number two: '))
number_three = int(input('Enter number three: '))
if number_one > z and number_two > number_three:
    print('Minimum of three numbers is',number_three)
elif number_three > number_two and number_one > number_two:
    print('Minimum of three numbers is',number_two)
else:
    print('Minimum of three numbers is',number_one)



#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Умова: Дано ціле число, що визначає рік.
Визначити, чи є вказаний рік високосним.
Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".
"""
#Програма вираховує чи є введений рік високосним
#Рік високосний, якщо виконується хоча б одна з умов:
#    рік завжди високосним, якщо його номер ділиться на 4 без остачі і не ділиться без остачі на 100
#    рік завжди високосним, якщо його номер ділиться на 400 без остачі
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("LEAP")
else:
    print("COMMON")



#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Умова: Дано три цілих числа. Визначте, скільки з них дорівнюють один одному.
"""
#Програма повинна виводити одне з чисел:
#3 (якщо всі числа однакові),
#2 (якщо два з них дорівнюють один одному, а третє відрізняється)
#або 0 (якщо всі числа різні).
number_one = int(input('Enter number one: '))
number_two = int(input('Enter number two: '))
number_three = int(input('Enter number three: '))
if number_one == number_two == number_three:
    print(3)
elif number_one != number_two != number_three and number_one != number_three:
    print(0)
else:
    print(2)



#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Умова: Шахова тура переміщається по горизонталі або по вертикалі.
Дано координати двох клітин шахової дошки. Визначити, чи може тура перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.
"""
#Програма здійснює перевірку чи може Шахова Тура за 1 хід преміститися з однієї клітинки в іншу:
#користувач вводить кординати(від 1 до 8) двох клітинок
cordinate_x1 = int(input('Enter cordinate x1:'))
cordinate_y1 = int(input('Enter cordinate y1:'))
cordinate_x2 = int(input('Enter cordinate x2:'))
cordinate_y2 = int(input('Enter cordinate y2:'))
if cordinate_x1 == cordinate_x2 or cordinate_y1 == cordinate_y2:
    print("YES")
else:
    print("NO")



#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.
"""
#Програма здійснює перевірку чи 2 випадково вибраних клітинки є одного кольору :
#користувач вводить кординати(від 1 до 8) двох клітинок
cordinate_x1 = int(input('Enter cordinate x1:'))
cordinate_y1 = int(input('Enter cordinate y1:'))
cordinate_x2 = int(input('Enter cordinate x2:'))
cordinate_y2 = int(input('Enter cordinate y2:'))
if (cordinate_x1 + cordinate_x2 + cordinate_y1 + cordinate_y2) % 2 == 0:
    print('YES')
else:
    print("NO")



#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Умова: Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку.
Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""
#Програма здійснює перевірку чи Шаховий Король за 1 хід переміститися з однієї клітинки в іншу :
#користувач вводить кординати(від 1 до 8) двох клітинок
cordinate_x1 = int(input('Enter cordinate x1:'))
cordinate_y1 = int(input('Enter cordinate y1:'))
cordinate_x2 = int(input('Enter cordinate x2:'))
cordinate_y2 = int(input('Enter cordinate y2:'))
if 1 <=(cordinate_x1 - cordinate_x2)**2 + (cordinate_y1 - cordinate_y2)**2 <= 2:
    print('YES')
else:
    print("NO")



#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Умова: Шаховий слон рухається по діагоналі на будь-яку кількість клітин.
Дано координати двох клітин шахової дошки. Визначити, чи може слон перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""
#Програма здійснює перевірку чи Шаховий Слон за 1 хід переміститися з однієї клітинки в іншу :
#користувач вводить кординати(від 1 до 8) двох клітинок
cordinate_x1 = int(input('Enter cordinate x1:'))
cordinate_y1 = int(input('Enter cordinate y1:'))
cordinate_x2 = int(input('Enter cordinate x2:'))
cordinate_y2 = int(input('Enter cordinate y2:'))
if abs(cordinate_x1 - cordinate_x2) == abs(cordinate_y1 - cordinate_y2):
    print('YES')
else:
    print('NO')



#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин.
Дано координати двох клітин шахової дошки.Визначити, чи може королева перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""
#Програма здійснює перевірку чи Шаховиа Королева за 1 хід переміститися з однієї клітинки в іншу :
#користувач вводить кординати(від 1 до 8) двох клітинок
cordinate_x1 = int(input('Enter cordinate x1:'))
cordinate_y1 = int(input('Enter cordinate y1:'))
cordinate_x2 = int(input('Enter cordinate x2:'))
cordinate_y2 = int(input('Enter cordinate y2:'))
if abs(cordinate_x2 - cordinate_x1) == abs(cordinate_y2 - cordinate_y1) or cordinate_x1 == cordinate_x2 or cordinate_y1 == cordinate_y2  :
    print('YES')
else:
    print("NO")



#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Умова: Шаховий кінь рухається як літера L.
Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі.
Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""
#Програма здійснює перевірку чи Шаховий Кінь за 1 хід переміститися з однієї клітинки в іншу :
#користувач вводить кординати(від 1 до 8) двох клітинок
cordinate_x1 = int(input('Enter cordinate x1:'))
cordinate_y1 = int(input('Enter cordinate y1:'))
cordinate_x2 = int(input('Enter cordinate x2:'))
cordinate_y2 = int(input('Enter cordinate y2:'))
if (abs(cordinate_x2 - cordinate_x1) == 1 and abs(cordinate_y1 - cordinate_y2) == 2) or (abs(cordinate_y2 - cordinate_y1) == 1 and abs(cordinate_x2 - cordinate_x1) == 2 ):
    print('YES')
else:
    print("NO")



#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Умова: Шоколад має форму прямокутника, розділеного на n×m клітин.
Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими.
Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин.
Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.
"""
#Програма здійснює перевірку чи за один крок можна розділити шоколадку так щоб в ній було точна кількість кусочків :
#користувач вводить розміри плитки шоколаду(довжину і ширину)
long_m = int(input('Enter long chocolate bar '))
width_n = int(input('Enter width chocolate bar'))
k_squares = int(input('Enter number portions'))
if ((k_squares % long_m == 0) or (k_squares % width_n == 0)) and (long_m * width_n >= k_squares):
    print("YES")
else:
    print("NO")



#-----------------------------------------------------------------
