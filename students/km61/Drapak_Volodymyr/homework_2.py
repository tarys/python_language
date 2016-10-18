#task1------------------------------------------------------------
"""
Умова: Дано два цілих числа. Вивести найменше з них.

Вхідні дані: користувач вводить два цілих числа

Вихідні дані: вивести ціле число
"""



#write your answer here...
"""
# Program reads two integers and outputs lesser of them
# first_number, second_number - integers
# Result is lesser of read numbers (integer)

# input
first_number = int(input())
second_number = int(input())

# body
if first_number <= second_number:
    print(first_number)
else:
    print(second_number)
"""

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Умова: Вивести результат функції sign(x), що визначається наступним чином:
sign(x) = 1, if x > 0,
sign(x) = -1, if x < 0,
sign(x) = 0, if x = 0..

Вхідні дані: користувач вводить дійсне число.

Вихідні дані: вивести результат sign.
"""



#write your answer here...
"""
# Program reads integer x and outputs sign(x)
# x - integer
# Result is sign(x) (integer)

# input
x = int(input())

# body
if x < 0:
    print(-1)
elif x > 0:
    print(1)
else:
    print(0)
"""

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Умова: Дано три цілих числа. Вивести найменше з них.

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""



#write your answer here...
"""
# Program reads three numbers and outputs lesser of them
# first_number, second_number, third_number - integers
# Result is least of read numbers (integer)

# input
first_number = int(input())
second_number = int(input())
third_number = int(input())

# body
if(first_number <= second_number and first_number <= third_number):
    print(first_number)
elif(second_number <= first_number and second_number <= third_number):
    print(second_number)
else:
    print(third_number)
"""

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Умова: Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним.
Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".

Рік високосний, якщо виконується хоча б одна з умов:

рік завжди високосний, якщо його номер ділиться на 4 без остачі і не ділиться без остачі на 100
рік завжди високосний, якщо його номер ділиться на 400 без остачі
Вхідні дані: ціле число, що вводить користувач

Вихідні дані: вивести текстовий рядок.
"""



#write your answer here...
"""
# Program reads year and determines whether a leap year
# year - integer
# Result is string where is written "LEAP" or "COMMON"

# input
year = int(input())

# body
if year % 400 == 0 or (year%4 == 0 and year%100 != 0):
    print("LEAP")
else:
    print("COMMON")
"""

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Умова: Дано три цілих числа. Визначте, скільки з них дорівнюють один одному.
Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові),
2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""



#write your answer here...
"""
# Program reads three numbers and determines how much of them are equal each other
# first_number, second_number, third_number - integers
# Result is number of equal each other numbers (integer)

# input
first_number = int(input())
second_number = int(input())
third_number = int(input())

# body
if(first_number == second_number and second_number == third_number):
    print(3)
elif(first_number == second_number or first_number == third_number or second_number == third_number)
    print(2)
else:
    print(0)
"""

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Умова: Шахова тура переміщається по горизонталі або по вертикалі.
Дано координати двох клітин шахової дошки. Визначити, чи може тура перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#write your answer here...
"""
# Program reads coordinates of two cells of chessboard and determines can rook on first cell move to second cell for one move
# x1, y1, x2, y2 - respective coordinates of two cells (integers)
# Result is string where is written "YES" or "NO"

# input
y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())

# body
if(x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2):
    print("YES")
else:
    print("NO")
"""

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#write your answer here...
"""
# Program reads coordinates of two cells of chessboard and determines are they painted in one color or no
# y1, x1, y2, x2 - respective coordinates of two cells of chessboard
# Result is string where written "YES" or "NO"

# input
y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())

# body
if((abs(y1 - y2) + abs(x1 - x2)) % 2 == 0):
    print("YES")
else:
    print("NO")
"""

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Умова: Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку.
 Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід.
  Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
  Перші два числа - для першої клітини, останні два числа – для другої.
  Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#write your answer here...
"""
# Program reads coordinates of two cells of chessboard and determines can king move from first cell to second for one move
# y1, x1, y2, x2 - respective coordinates of two cells of chessboard
# Result is string where written "YES" or "NO"

# input
y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())

# body
if(abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1):
    print("YES")
else:
    print("NO")
"""

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Умова: Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки.
Визначити, чи може слон перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#write your answer here...
"""
# Program reads coordinates of two cells of chessboard and determines can bishop move from first cell to second for one move
# y1, x1, y2, x2 - respective coordinates of two cells of chessboard
# Result is string where written "YES" or "NO"

# input
y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())

# body
if(abs(x1 - x2) == abs(y1 - y2)):
    print("YES")
else:
    print("NO")
"""

#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин.
Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#write your answer here...
"""
# Program reads coordinates of two cells of chessboard and determines can queen move from first cell to second for one move
# y1, x1, y2, x2 - respective coordinates of two cells of chessboard
# Result is string where written "YES" or "NO"

# input
y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())

# body
can_move_as_bishop = abs(x1 - x2) == abs(y1 - y2)
can_move_as_rook = (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2)
if(can_move_as_rook or can_move_as_bishop):
    print("YES")
else:
    print("NO")
"""

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Умова: Шаховий кінь рухається як літера L.
Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі.
Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#write your answer here...
"""
# Program reads coordinates of two cells of chessboard and determines can knight move from first cell to second for one move
# y1, x1, y2, x2 - respective coordinates of two cells of chessboard
# Result is string where written "YES" or "NO"

# input
y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())

# body
if(abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
    print("YES")
else:
    print("NO")
"""

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Умова: Шоколад має форму прямокутника, розділеного на n×m клітин.
Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими.
Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин.
Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.

Вхідні дані: 3 цілих числа: n,m, k. Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""



#write your answer here...

"""
# Program reads three numbers - dimensions of chocolate bar and number of cells and determines can chocolate bar be divided
# length, width - dimensions of chocolate bar
# cell_number - number of cells
# Result is string where is written answer for question

# input
length = int(input())
width = int(input())
cell_number = int(input())

# body
if((cell_number % length == 0 or cell_number % width == 0) and cell_number < length*width):
    print("YES")
else:
    print("NO")
"""

#-----------------------------------------------------------------