#Задача №1 -------------------------------------------------------------
"""

Умова: Дано два цілих числа. Вивести найменше з них.

Вхідні дані: користувач вводить ціле число

Вихідні дані: вивести ціле число
"""


#input------------------------------------------------------------------
integer1 = int(input())
integer2 = int(input())
#output-----------------------------------------------------------------
if(integer1 > integer2):
	print(integer2)
else:
	print(integer1)

#-----------------------------------------------------------------------


#Задача №2--------------------------------------------------------------
"""
Умова: Вивести результат функціїsign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..

Вхідні дані: користувач вводить дійсне число.

Вихідні дані: вивести результат sign.
"""


#main-------------------------------------------------------------------
def sign(x):
	if(x > 0):
		print(1)
	elif(x < 0):
		print(-1)
	else:
		print(0)
#input------------------------------------------------------------------
a = int(input())
sign(a)

#-----------------------------------------------------------------------


#Задача №3--------------------------------------------------------------
"""
Умова: Дано три цілих числа. Вивести найменше з них.

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""


#input------------------------------------------------------------------
a = int(input())
b = int(input())
c = int(input())
#main-------------------------------------------------------------------
if(a <= b):
	minimum = a
elif(b < a):
	minimum = b
if(minimum > c):    
	minimum = c
print(minimum)

#-----------------------------------------------------------------------


#Задача №4--------------------------------------------------------------
"""
Умова: Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".

Рік високосний, якщо виконується хоча б одна з умов:

рік завжди високосним, якщо його номер ділиться на 4 без остачі і не ділиться без остачі на 100
рік завжди високосним, якщо його номер ділиться на 400 без остачі
Вхідні дані: ціле число, що вводить користувач

Вихідні дані: вивести текстовий рядок.
"""


#input------------------------------------------------------------------
a = int(input())
#main-------------------------------------------------------------------
if(a%100 == 0):
	a = a/100
if(a%4 == 0):
#output-----------------------------------------------------------------
	print("LEAP")
else:    
	print("COMMON")


#--------------------------------------------------------------------------------------------------


#Задача №5-----------------------------------------------------------------------------------------
"""
Умова: Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""


#input------------------------------------------------------------------
a = int(input())
b = int(input())
c = int(input())
#main-------------------------------------------------------------------
if(a == b and b == c and a == c):
	answer=3
elif(a == b or b==c or a == c):
	answer=2
else:
	answer=0
#output-----------------------------------------------------------------
print (answer)

#-----------------------------------------------------------------------

#Задача №6--------------------------------------------------------------
"""
Умова: Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки. Визначити, чи може тура перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""


#input------------------------------------------------------------------
column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())
#output-----------------------------------------------------------------
if(column1 == column2 or row1==row2):
	print("YES");
else:    
	print("NO");

#-----------------------------------------------------------------------


#Задача №7--------------------------------------------------------------
"""
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""


#input------------------------------------------------------------------
column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())
#main-------------------------------------------------------------------
if(column1 % 2 != 0):
	if(row1 % 2 == 0):
		firstCell = "Black"
	elif(row1 % 2 != 0):
		firstCell = "White"
elif(column1 % 2 == 0):
	if(row1 % 2 != 0):
		firstCell = "Black"
	elif(row1 % 2 == 0):
		firstCell = "White"
if(column2 % 2 != 0):
	if(row2 % 2 == 0):
		secondCell = "Black"
	elif(row2 % 2 != 0):
		secondCell = "White"
elif(column2 % 2 == 0):
	if(row2 % 2 != 0):
		secondCell = "Black"
	elif(row2 % 2 == 0):        
		secondCell = "White"
if(firstCell == secondCell):
#output-----------------------------------------------------------------    
	print('YES')
else:
	print('NO')

#-----------------------------------------------------------------------


#Задача №8--------------------------------------------------------------
"""
Умова: Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку. Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести текстовий рядок.
"""


#input------------------------------------------------------------------
column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())
#main-------------------------------------------------------------------
if(column1 - column2 == 1 or column1 - column2 == 0 or column1 - column2 == -1):
	if(row1-row2==1 or row1-row2 ==0 or row1-row2 == -1):
		print("YES")
	else:
		print("NO")
else:    
	print("NO")

#--------------------------------------------------------------------------------------------------


#Задача №9-----------------------------------------------------------------------------------------
"""
Умова: Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може слон перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""


#input------------------------------------------------------------------
column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())
#main-------------------------------------------------------------------
if(abs(column2-column1) == abs(row2-row1)):
	print("YES")
else:    
	print("NO")

#-----------------------------------------------------------------------

#Задача №10-------------------------------------------------------------
"""
Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""


#input------------------------------------------------------------------
column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())
#main-------------------------------------------------------------------
if(abs(column2-column1) == abs(row2-row1)):
	print("YES")
elif(column1 == column2 or row1 == row2):
	print("YES")
else:
	print("NO")
#--------------------------------------------------------------------------------------------------

#Задача №11-----------------------------------------------------------------------------------------
"""
Умова: Шаховий кінь рухається як літера L. Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі. Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""


#input------------------------------------------------------------------
column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())
#main-------------------------------------------------------------------
if(abs(column1-column2) == 1 and abs(row1-row2) == 2 or abs(column1-column2) == 2 and abs(row1-row2) == 1):
	print("YES")
else:
	print("NO")


#--------------------------------------------------------------------------------------------------

#Задача №12-------------------------------------------------------------
"""
Умова: Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими. Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин. Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.

Вхідні дані: 3 цілих числа: n,m, k. Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""


#input------------------------------------------------------------------
width = int(input())
height = int(input())
piece = int(input())
#main-------------------------------------------------------------------
if((width*height - piece) >= 0 and (width*height - piece)%width == 0 or (width*height - piece) >= 0 and (width*height - piece)%height == 0):
	print("YES")
else:
	print("NO")

#-----------------------------------------------------------------------
