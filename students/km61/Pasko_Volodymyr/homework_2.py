#task1------------------------------------------------------------
"""
Дано два цілих числа. Вивести найменше з них.
"""

#program, which compares two entered numbers and printeng the smallest one
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
if (first_number < second_number):
    print(first_number)
else:
    print(second_number)

#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
Вивести результат функціїsign(x), що визначається наступним чином: 
"""
# program, printing the result of sign(x) function, according to the 
argument_function = int(input(("Enter x: ")))
if (argument_function > 0):
    print("sign(x) = 1")
elif (argument_function == 0):
    print("sign(x) = 0")
else:
    print("sign(x) = -1")
#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
Дано три цілих числа. Вивести найменше з них.
"""
# program comparing three numbers according to their value and printing the smallest
print("Enter the first number: ")
first_number = int(input())
print("Enter the second number: ")
second_number = int(input())
print("Enter the third number: ")
third_number = int(input())

if (first_number < second_number < third_number) or (first_number < third_number < second_number) :
    print(first_number)
elif (second_number < first_number < third_number) or (second_number < third_number < first_number):
    print(second_number)
elif (third_number < second_number < first_number) or (third_number < first_number < second_number):
    print(third_number)
#-----------------------------------------------------------------

#task4------------------------------------------------------------

"""
Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".
"""
# program, which shows if the year leap or common
year = int(input("Enter the year: "))
if (year % 4 == 0) or (year % 400 == 0):
    print("LEAP")

else:
    print("COMMON")
#-----------------------------------------------------------------

#task5------------------------------------------------------------
"""
Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).
"""
# program, which shows the quantity of equal numbers

print()
print("Enter the first number: ")
first_number = int(input())
print("Enter the second number: ")
second_number = int(input())
print("Enter the third number: ")
third_number = int(input())
if (first_number == second_number == third_number):
    print(3)
elif (first_number == second_number) or (first_number == third_number): 
    print(2)
elif (first_number == second_number) or (second_number == third_number):
    print(2)
elif (first_number == third_number) or (second_number == third_number):
    print(2)
else:
    print(0)
#-----------------------------------------------------------------

#task6------------------------------------------------------------

"""
Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки. Визначити, чи може тура перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.
"""

# Program showing the possibility of chess rook moving
print("Define the cordinate of the column: ")
cordinate_column = int(input())
print("Define the cordinate of the row: ")
cordinate_row = int(input())
print("Define the cordinate of the column, where you want to make a move: ")
wish_cordinate_column = int(input())
print("Define the cordinate of the row, where you want to make a move: ")
wish_cordinate_row = int(input())

if (cordinate_column == wish_cordinate_column) or (cordinate_row == wish_cordinate_row):
    print("YES")
else:
    print("NO")
#-----------------------------------------------------------------

#task7------------------------------------------------------------

"""
Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.
"""
 program showing the color of cell on chess board
print("Define the cordinate of the column of the first cellule: ")
cordinate_column = int(input())
print("Define the cordinate of the row of the first cellule: ")
cordinate_row = int(input())

if ((cordinate_column % 2 == 0) and (cordinate_row % 2 == 0)) or ((cordinate_column % 2 != 0) and (cordinate_row % 2 != 0)):
    color_cell_black = 1  # black cell
elif ((cordinate_column % 2 != 0) and (cordinate_row % 2 == 0)) or ((cordinate_column % 2 ==  0) and (cordinate_row % 2 != 0)):
    color_cell_black = 0 # not black cell

print("Define the cordinate of the column of the second cellule : ")
wish_cordinate_column = int(input())
print("Define the cordinate of the row of the second cellule: ")
wish_cordinate_row = int(input())

if ((wish_cordinate_column % 2 != 0) and (wish_cordinate_row % 2 == 0)) or ((wish_cordinate_column % 2 == 0) and (wish_cordinate_row % 2 != 0)):
    color_cell_white = 1 # white cell
elif ((wish_cordinate_column % 2 == 0) and (wish_cordinate_row % 2 == 0)) or ((wish_cordinate_column % 2 != 0) and (wish_cordinate_row % 2 != 0)):
    color_cell_white = 0 # not white cell

    
if(color_cell_black != color_cell_white):
    print('Yes')
else:
    print('No')
#-----------------------------------------------------------------

#task8------------------------------------------------------------

"""
Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку. Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""

# program which shows the posibility of king's moves
print("Define the coordinates of the king: ")
king_row_cordinate = int(input())
king_column_cordinate = int(input())
print("Define the cellule you wish the king to move: ")
wish_king_row = int(input())
wish_king_cordinate = int(input())
if ((wish_king_row == king_row_cordinate) or (wish_king_row == king_row_cordinate - 1) or (wish_king_row == king_row_cordinate + 1)) and ((wish_king_cordinate == king_column_cordinate) or (wish_king_cordinate == king_column_cordinate - 1) or (wish_king_cordinate == king_column_cordinate + 1)):
    print("YES")
else:
    print("NO")
#-----------------------------------------------------------------

#task9------------------------------------------------------------

"""
Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може слон перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""
# Program, defining the possibility of bishop moves
print("Define the coordinates of the bishop: ")
bishop_row_cordinate = int(input())
bishop_column_cordinate = int(input())
print("Define the cellule you wish: ")
wish_bishop_row_cordinate = int(input())
wish_bishop_column_cordinate = int(input())

if ((bishop_row_cordinate + bishop_column_cordinate == wish_bishop_row_cordinate + wish_bishop_column_cordinate) or (bishop_row_cordinate - bishop_column_cordinate == wish_bishop_row_cordinate - wish_bishop_column_cordinate)):
    print("YES")
else:
    print('No')

#-----------------------------------------------------------------

#task10-----------------------------------------------------------
"""
Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""
# Program showing the possibility of queen's moves
print("Define the coordinates of the queen: ")
queen_row_cordinate = int(input())
queen_column_cordinate = int(input())
print("Define the cellule you wish: ")
wish_queen_row_cordinate = int(input())
wish_queen_column_cordinate = int(input())


if (queen_column_cordinate == wish_queen_column_cordinate) or (queen_row_cordinate == wish_queen_row_cordinate):
    print("YES")
elif ((queen_row_cordinate + queen_column_cordinate == wish_queen_row_cordinate + wish_queen_column_cordinate) or (queen_row_cordinate - queen_column_cordinate == wish_queen_row_cordinate - wish_queen_column_cordinate)):
    print("YES")
else:
    print('No')
#-----------------------------------------------------------------

#task11-----------------------------------------------------------
"""
Шаховий кінь рухається як літера L. Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі. Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
"""
# Program showing the possibility of knight's move
print('Enter the cordinates of the knight: ')
knight_row_cordinate = int(input()) 
knight_column_cordinate = int(input())
print('Define the cellule, you wish: ')
wish_knight_row_cordinate = int(input())
wish_knight_column_cordinate = int(input())

if (((knight_row_cordinate + 2 == wish_knight_row_cordinate) or (knight_row_cordinate - 2 == wish_knight_row_cordinate)) and ((knight_column_cordinate +1 == wish_knight_column_cordinate) or (knight_column_cordinate - 1 == wish_knight_column_cordinate))):
    print('Yes')
elif((knight_row_cordinate + 1 == wish_knight_row_cordinate or knight_row_cordinate -1 == wish_knight_row_cordinate) and (knight_column_cordinate + 2 == wish_knight_column_cordinate or knight_column_cordinate - 2 == wish_knight_column_cordinate)):
    print('Yes')
else:
    print('No')
#-----------------------------------------------------------------

#task12-----------------------------------------------------------
"""
Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими. Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин. Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.
"""
# program showing the possibility of splitting the chocolate bar 

print('Define the size of the chocolate: ')
chocolate_rows = int(input())
chocolate_cols = int(input())
print('Define the amount of chocolate you want to leave after one splitting: ')
chocolate_to_leave = int(input())

if ((chocolate_to_leave % chocolate_rows == 0) or (chocolate_to_leave % chocolate_cols == 0)) and (chocolate_to_leave <= chocolate_rows * chocolate_cols):
    print('Yes')
else:
    print('No')
#-----------------------------------------------------------------



















