#task1----------------------------------------
'''Дано два цілих числа. Вивести найменше з них'''

#input
print ('Task 1: Виведення найменшого числа ')
number_1 = int(input('Enter the real  numder: '))     #int
number_2 = int(input('Enter the real  numder: '))     #int

#main
if number_1 > number_2: 
    #output
    print ('Найменше число з введених:', number_2)
else:
    #output
    print('Найменше число з введених:', number_1)
print('')
#-----------------------------------------------------


#task2--------------------------------------------------------
'''Вивести результат функції sign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0,
sign(x) = 0, if x = 0.'''

#input
print('Task 2: Результат функції sign(x)')
x = int(input('Enter the real  numder:'))     #int

#main
if x > 0:
    print("sing(x) = 1")      #значення функції при х > 0 
                              #str
elif x < 0:
    print("sing(x) = -1")     #значення функції при х < 0
                              #str
else:
    print("sing(x) = 0")      #значення функції при х = 0
                              #str
print('')
#---------------------------------------------------------------


#task3---------------------------------------------------------------
'''Дано три цілих числа. Вивести найменше з них.'''

#input
print ('Task 3: Виведення наймешного числа:')
number_1 = int(input('Enter the real number:'))          #int
number_2 = int(input('Enter the real number:'))          #int
number_3 = int(input('Enter the real number:'))          #int

#main
if (number_1 < number_2) and (number_1 < number_3):
    print('Найменше число дорівнює',number_1)      #int
elif (number_2 < number_1) and (number_1 < number_3):
    print('Найменше число дорівнює', number_2 )    #int
else:
    print('Найменше число дорівнює', number_3)    #int
print('')
#------------------------------------------------------------------------


#task4--------------------------------------------------------------------
'''Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".'''

#input
print('Task 4: Визначення високосного року')
year = int(input('Enter the year:'))    #real number

#main
if year % 4 == 0 and year % 100 != 0:
    print("LEAP")  #str
elif year % 400 == 0:
    print("LEAP")  #str
else:
    print("COMMON")  #str
print('')
#---------------------------------------------------------------------------


#task5----------------------------------------------------------------------
'''Дано три цілих числа. Визначте, скільки з них дорівнюють один одному.
Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо два з них
дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).'''

#input
print('Task 5: Визначення рівності чисел')
number_1 = int(input('Enter the integer number: '))              #int
number_2 = int(input('Enter the integer number: '))              #int
number_3 = int(input('Enter the integer number: '))              #int

#main
if number_1 == number_2 == number_3:
    print('3')       # три введені числа рівні
                     #str
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print('2')      # два будь-які введені числа рівні
                    #str
else:
    print('0')      #всі числа не рівні між собою
                    #str
print('')
#-----------------------------------------------------------------------

#task6------------------------------------------------------------------
'''Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки.
Визначити, чи може тура перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа
від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини,
останні два числа – для другої. Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.'''

#input
print('Task 6: Переміщення шахового тура ')
x1 = int(input('Enter the first coordinate of the first cell: '))    #int from 1 to 8
y1 = int(input('Enter the second coordinate of the first cell: '))    #int from 1 to 8
x2 = int(input('Enter the first coordinate of the second cell: '))    #int from 1 to 8
y2 = int(input('Enter the second coordinate of the second cell: '))    #int from 1 to 8

#main
if x1 > 8 or x1 < 0:
    print ('Entered an invalid number')
elif y1 > 8 or y1 < 0:
    print('Entered an invalid number')
elif x2 > 8 or x2 <0:
    print ('Entered an invalid number')
elif y2 >8 or y2 <0:
    print('Entered an invalid number')
    
else:
    if x1 == x2 or y1 == y2:
        print("YES")        #str      
    else:
        print("NO")         #str
print('')
#------------------------------------------------------------------


#task7--------------------------------------------------------------
'''Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.'''

#input
print('Task 7: Визначення кольору двох клітин')
x1 = int(input('Enter the first coordinate of the first cell: '))    #int from 1 to 8
y1 = int(input('Enter the second coordinate of the first cell: '))    #int from 1 to 8
x2 = int(input('Enter the first coordinate of the second cell: '))    #int from 1 to 8
y2 = int(input('Enter the second coordinate of the second cell: '))    #int from 1 to 8

#main
if x1 > 8 or x1 < 0:
    print ('Entered an invalid number')
elif y1 > 8 or y1 < 0:
    print('Entered an invalid number')
elif x2 > 8 or x2 <0:
    print ('Entered an invalid number')
elif y2 >8 or y2 <0:
    print('Entered an invalid number')

else:
    if (x1 + y1 + x2 + y2)%2 == 0:
        print("YES")       #str
    else:
        print("NO")         #str
print('')
#-----------------------------------------------------------------------------


#task8----------------------------------------------------------
'''Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку.
Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.'''

#input
print('Task 8: Переміщення шахового короля')
x1 = int(input('Enter the first coordinate of the first cell: '))    #int from 1 to 8
y1 = int(input('Enter the second coordinate of the first cell: '))    #int from 1 to 8
x2 = int(input('Enter the first coordinate of the second cell: '))    #int from 1 to 8
y2 = int(input('Enter the second coordinate of the second cell: '))    #int from 1 to 8

#main
if x1 > 8 or x1 < 0:
    print ('Entered an invalid number')
elif y1 > 8 or y1 < 0:
    print('Entered an invalid number')
elif x2 > 8 or x2 <0:
    print ('Entered an invalid number')
elif y2 >8 or y2 <0:
    print('Entered an invalid number')

else:
    if abs (x1 - x2) <= 1 and abs (y1 - y2) <= 1:
        print("YES")        #str
    else: 
        print("NO")         #str
print('')
#-----------------------------------------------------------


#task9---------------------------------------------------------------
'''Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки.
Визначити, чи може слон перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8,
кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої.
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.'''

#input
print('Task 9: Переміщення шахового слона')
x1 = int(input('Enter the first coordinate of the first cell: '))    #int from 1 to 8
y1 = int(input('Enter the second coordinate of the first cell: '))    #int from 1 to 8
x2 = int(input('Enter the first coordinate of the second cell: '))    #int from 1 to 8
y2 = int(input('Enter the second coordinate of the second cell: '))    #int from 1 to 8

#main
if x1 > 8 or x1 < 0:
    print ('Entered an invalid number')
elif y1 > 8 or y1 < 0:
    print('Entered an invalid number')
elif x2 > 8 or x2 <0:
    print ('Entered an invalid number')
elif y2 >8 or y2 <0:
    print('Entered an invalid number')

else:
    if abs (x1 - x2) == abs (y1 - y2):
        print("YES")      #str
    else:
        print("NO")       #str
print('')
#-----------------------------------------------------


#task10--------------------------------------------------------
'''Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин.
Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.'''

#input
print('Task 10: Переміщення шахової королеви')
x1 = int(input('Enter the first coordinate of the first cell: '))    #int from 1 to 8
y1 = int(input('Enter the second coordinate of the first cell: '))    #int from 1 to 8
x2 = int(input('Enter the first coordinate of the second cell: '))    #int from 1 to 8
y2 = int(input('Enter the second coordinate of the second cell: '))    #int from 1 to 8

#main
if x1 > 8 or x1 < 0:
    print ('Entered an invalid number')
elif y1 > 8 or y1 < 0:
    print('Entered an invalid number')
elif x2 > 8 or x2 <0:
    print ('Entered an invalid number')
elif y2 >8 or y2 <0:
    print('Entered an invalid number')

else:
    if (abs (x1 - x2) == abs (y1 - y2)) or ((x1 == x2) or (y1 == y2)):
        print("YES")                 #str
    else:
        print("NO")                  #str
print('')
#-------------------------------------------------------


#task11---------------------------------------------------------
'''Шаховий кінь рухається як літера L. Він може переміщатись на дві клітинки по горизонталі і
одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі.
Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.'''

#input
print('Task 11: Переміщення шахового слона')
x1 = int(input('Enter the first coordinate of the first cell: '))    #int from 1 to 8
y1 = int(input('Enter the second coordinate of the first cell: '))    #int from 1 to 8
x2 = int(input('Enter the first coordinate of the second cell: '))    #int from 1 to 8
y2 = int(input('Enter the second coordinate of the second cell: '))    #int from 1 to 8

#main
if x1 > 8 or x1 < 0:
    print ('Entered an invalid number')
elif y1 > 8 or y1 < 0:
    print('Entered an invalid number')
elif x2 > 8 or x2 <0:
    print ('Entered an invalid number')
elif y2 >8 or y2 <0:
    print('Entered an invalid number!')

else:
    if abs (x1 - x2) == 1 and abs (y1 - y2) == 2:
        print("YES")                                  #str
    elif abs (x1 - x2) == 2 and abs (y1 - y2) == 1:
        print("YES")                                  #str
    else:
        print("NO")                                    #str
print('')
#----------------------------------------------------------------------


#task12---------------------------------------------------------
'''Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад може бути розділений
на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими.
Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин.
Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.'''

#input
print('Task 12: Поділ шоколаду')
lenght_chokolate = int(input('Enter the real number: '))    # int from 0
width_chokolate = int(input('Enter the real number: '))     #int from 0
cell_number = int(input('Enter the real number: '))         #int from 0

#main
if lenght_chokolate < 0 or width_chokolate < 0 or cell_number < 0:
    print('Entered an invalid number!')
    
else:
    if cell_number < lenght_chokolate * width_chokolate and (cell_number % width_chokolate == 0 or cell_number % lenght_chokolate == 0):
        print("YES")                          #str
    else:
        print("NO")                          #str
print()
#-----------------------------------------------------------------
