# -*- coding: utf-8 -*-

"""
    Домашня робота №2
    Тема: "Умовні конструкції"
    Студент: Козирєв Антон Юрійович
    Група: КМ - 62
"""

import math

#Task_1----------------------------------------------------#

"""
    Умова: Дано два цілих числа. Вивести найменше з них.
"""

#print("Task #1");
Number_1 = int(input()) #"Enter first integer number:"
Number_2 = int(input()) #"Enter second integer number:"
if (Number_1<Number_2):
    print(Number_1)
elif (Number_2<Number_1):
    print(Number_2)
else:
    print(Number_1)
#print("First task complited!");

#---------------------------------------------------------#



#Task_2---------------------------------------------------#

"""
    Умова: Вивести результат функціїsign(x), що визначається наступним чином: 
        sign(x) = 1, if x > 0, 
        sign(x) = -1, if x < 0, 
        sign(x) = 0, if x = 0..
"""

#print("Task #2");
Number = int(input()) #"Enter integer number: "
if Number>0:
    print(1) #"sign(x) = 1"
elif (Number<0):
    print(-1) #"sign(x) = -1"
else:
    print(0) #"sign(x) = 0"
#print("Second task complited!");

#---------------------------------------------------------#



#Task_3---------------------------------------------------#

"""
    Умова: Дано три цілих числа. Вивести найменше з них.
"""

#print("Task #3");
Number_1 = int(input()) #"Enter first integer number: "
Number_2 = int(input()) #"Enter second integer number: "
Number_3 = int(input()) #"Enter third integer number: "
if (Number_1<Number_2) and (Number_1<Number_3):
    print(Number_1)
elif (Number_2<Number_1) and (Number_2<Number_3):
    print(Number_2)
elif (Number_3<Number_1) and (Number_3<Number_2):
    print(Number_3)
else:
    print("Some of them are equal!")
#print("Third task complited!");

#---------------------------------------------------------#



#Task_4---------------------------------------------------#

"""
Умова: Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".

Рік високосний, якщо виконується хоча б одна з умов:

рік завжди високосним, якщо його номер ділиться на 4 без остачі і не ділиться без остачі на 100
рік завжди високосним, якщо його номер ділиться на 400 без остачі
"""

#print("Task #4");
Year = int(input()) #"I'm livin' in year: "
if ((Year % 4 == 0) and (Year % 100 != 0)) or Year % 400 == 0:
    print("LEAP")
else:
    print("COMMON")
#print("Fourth task complited!");

#---------------------------------------------------------#



#Task_5---------------------------------------------------#

"""
    Умова: Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).
"""

#print("Task #5");
Number_1 = int(input()) #"Enter first integer number:"
Number_2 = int(input()) #"Enter second integer number:"
Number_3 = int(input()) #"Enter third integer number:"
if (Number_1 != Number_2) and (Number_2 != Number_3) and (Number_3 != Number_1):
    print(0)
elif (Number_1 == Number_2) and (Number_2 == Number_3) and (Number_3 == Number_1):
    print(3)
elif (Number_1 == Number_2) or (Number_2 == Number_3) or (Number_3 == Number_1):
    print(2)
#print("Fifth task complited!");

#---------------------------------------------------------#



#Task_6---------------------------------------------------#

"""
Умова: Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки.
        Визначити, чи може тура перейти з першої клітини у другу за один хід. 
        Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. 
        Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.
"""

#print("Task #6");
SRow = int(input()) #"Start row (1-8):"
SColumn = int(input()) #"Start column (1-8):"
ERow = int(input()) #"End row (1-8):" 
EColumn = int(input()) #"End column (1-8):"
if ((SRow > 8 or SRow < 1) or (SColumn > 8 or SColumn < 1)) or ((ERow > 8 or ERow < 1) or (EColumn > 8 or EColumn < 1)):
    print("Invalid position!")
else:
    if (SRow == ERow or SColumn == EColumn):
        print("YES")
    else:
        print("NO")   
#print("Sixth task complited!");

#---------------------------------------------------------#



#Task_7---------------------------------------------------#

"""
    Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору.
    Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
    Перші два числа - для першої клітини, останні два числа – для другої.
    Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.
"""

#print("Task #7");
SRow = int(input()) #"Start row (1-8):"
SColumn = int(input()) #"Start column (1-8):"
ERow = int(input()) #"End row (1-8):"
EColumn = int(input()) #"End column (1-8):"
if ((SRow > 8 or SRow < 1) or (SColumn > 8 or SColumn < 1)) or ((ERow > 8 or ERow < 1) or (EColumn > 8 or EColumn < 1)):
    print("Invalid position!")
else:
    if ((SRow + SColumn) % 2 == 0): # Start position (1,1) - black, next (2,1) and (1,2) - white;
        SColor = "Black" #Start color
    else:
        SColor = "White"
            
    if ((ERow + EColumn) % 2 == 0):
        EColor = "Black" #End color                      
    else:
        EColor = "White"                       
        
    if (SColor == EColor):
        print("YES")
    else:
        print("NO")

#print("Seventh task complited!");


#---------------------------------------------------------#



#Task_8---------------------------------------------------#

"""
    Умова: Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку.
    Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід.
    Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
    Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

#print("Task #8");
SRow = int(input()) #"Start row (1-8):"
SColumn = int(input()) #"Start column (1-8):"
ERow = int(input()) #"End row (1-8):"
EColumn = int(input()) #"End column (1-8):"
if ((SRow > 8 or SRow < 1) or (SColumn > 8 or SColumn < 1)) or ((ERow > 8 or ERow < 1) or (EColumn > 8 or EColumn < 1)):
    print("Invalid position!")
else:
    if ((ERow > SRow + 1 or ERow < SRow - 1) or (EColumn > SColumn + 1 or EColumn < SColumn - 1)):
        print("NO")
    else:
        print("YES")
#print("Eighth task complited!");

#---------------------------------------------------------#



#Task_9---------------------------------------------------#

"""
Умова: Шаховий слон рухається по діагоналі на будь-яку кількість клітин.
       Дано координати двох клітин шахової дошки.
       Визначити, чи може слон перейти з першої клітини у другу за один хід.
       Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
       Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

#print("Task #9");
SRow = int(input()) #"Start row (1-8):"
SColumn = int(input()) #"Start column (1-8):"
ERow = int(input()) #"End row (1-8):"
EColumn = int(input()) #"End column (1-8):"
if ((SRow > 8 or SRow < 1) or (SColumn > 8 or SColumn < 1)) or ((ERow > 8 or ERow < 1) or (EColumn > 8 or EColumn < 1)):
    print("Invalid position!")
else:
    difRow = math.fabs(ERow - SRow)    # Row difference:  dif = |x2 - x1|
    difColumn = math.fabs(EColumn - SColumn)   # Column difference:  dif = |y1 - y2|
    if (difRow != difColumn):
        print("NO")
    else:
        print("YES")
#print("Nineth task complited!");

#---------------------------------------------------------#


#Task_10--------------------------------------------------#

"""
Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин.
       Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід.
       Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
       Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

# Queen positions = Officer positions + Castle Positions
#print("Task #10");
SRow = int(input()) #"Start row (1-8):"
SColumn = int(input()) #"Start column (1-8):"
ERow = int(input()) #"End row (1-8):"
EColumn = int(input()) #"End column (1-8):"
if ((SRow > 8 or SRow < 1) or (SColumn > 8 or SColumn < 1)) or ((ERow > 8 or ERow < 1) or (EColumn > 8 or EColumn < 1)):
    print("Invalid position!")
else:
    #Officer positions condition
    difRow = math.fabs(ERow - SRow)    # Row difference:  dif = |x2 - x1|
    difColumn = math.fabs(EColumn - SColumn)   # Column difference:  dif = |y1 - y2|
    #
    if ((difRow == difColumn) or (SRow == ERow or SColumn == EColumn)):
        print("YES")
    else:
        print("NO")
#print("Tenth task complited!");

#---------------------------------------------------------#


#Task_11--------------------------------------------------#

"""
    Умова: Шаховий кінь рухається як літера L.
    Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі.
    Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід.
    Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
    Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

#print("Task #11");
Result = "NO"
SRow = int(input()) #"Start row (1-8):"
SColumn = int(input()) #"Start column (1-8):"
ERow = int(input()) #"End row (1-8):"
EColumn = int(input()) #"End column (1-8):"
if ((SRow > 8 or SRow < 1) or (SColumn > 8 or SColumn < 1)) or ((ERow > 8 or ERow < 1) or (EColumn > 8 or EColumn < 1)):
    print("Invalid position!")
else:
    Delta_Row = math.fabs(SRow - ERow) #Difference in row values
    Delta_Column = math.fabs(SColumn - EColumn) #Difference in column values
    if (Delta_Row == 0 or Delta_Row == 2) and (Delta_Column == 2):
        Result = "YES"
    elif (Delta_Row == 0 and Delta_Column == 2) or (Delta_Column == 0):
        Result = "YES"
    print(Result)
#print("Eleventh task complited!")

#---------------------------------------------------------#



#Task_12--------------------------------------------------#

"""
    Умова: Шоколад має форму прямокутника, розділеного на n×m клітин.
    Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими.
    Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин.
    Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.
"""

#print("Task #12");
Rows = int(input()) #"Chocolate bar rows: "
Columns = int(input()) #"Chocolate bar columns: "
Pieces = int(input()) #"Pieces of chocolate you want: "
if ((Rows * Columns) <= Pieces):
    print("NO")
else:
    if (Pieces % Rows == 0 or Pieces % Columns == 0):
        print("YES")
    else:
        print("NO")
#print("Twelveth task complited!");

#---------------------------------------------------------#
