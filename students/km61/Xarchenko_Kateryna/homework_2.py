#task1-------------------------------------------------------------------------
"""

Умова: Дано два цілих числа. Вивести найменше з них.

Вхідні дані: користувач вводить ціле число

Вихідні дані: вивести ціле число
"""
#Програма для виводу меншого числа
#a,b - цілі числа для порівняня 
a = int(input())
b = int(input())
#Порівняня чисел 
if a<b:
    print(a)
else:
    print(b)
#------------------------------------------------------------------------------


#task2-------------------------------------------------------------------------
"""

Умова: Вивести результат функції sign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0..

Вхідні дані: користувач вводить дійсне число.

Вихідні дані: вивести результат sign.
"""
#Програма для визначення мат. функції sign
#sign - число для перевірки
sign = int(input())
#перевірка на число додатнє 
if sign>0:
    print(1)
#перевірка на чило відємне
elif sign<0:
    print(-1)
#перевірка чи дорівнює 0
else:
    print(0)
#------------------------------------------------------------------------------


#task3-------------------------------------------------------------------------
"""

Умова: Дано три цілих числа. Вивести найменше з них.

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""
#Програма для знаходження меншого числа
#number1,number2,number3 - цілі числа 
number1 = int(input())
number2 = int(input())
number3 = int(input())
# перевірка
if (number1<number2) and (number2<number3):
    print(number1)
elif (number1<number3) and (number3<number2):
    print(number1)
elif (number2<number1) and (number1<number3):
    print(number2)
elif (number2<number3) and (number3<number1):
    print(number2)
elif (number3<number1) and (number1<number2):
    print(number3)
elif (number3<number2) and (number2<number1):
    print(number3)
elif (number1==number2) and (number1<number3):
    print(number1)
elif (number1==number3) and (number1<number2):
    print(number1)
elif (number3==number2) and (number3<number1):
    print(number2)
else:
    print(number1)

#------------------------------------------------------------------------------


#task4-------------------------------------------------------------------------
"""

Задача №4 

Умова: Дано ціле число, що визначає рік. Визначити, чи є вказаний рік 
високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – 
"СOMMON".

Рік високосний, якщо виконується хоча б одна з умов:

рік завжди високосним, якщо його номер ділиться на 4 без остачі і не ділиться 
без остачі на 100
рік завжди високосним, якщо його номер ділиться на 400 без остачі

Вхідні дані: ціле число, що вводить користувач

Вихідні дані: вивести текстовий рядок.
"""
#Програма для визначення чи високосний рік
#year - заданий рік
year = int(input())
#перевірка на високосність
if year%400==0:
    print("LEAP")
elif (year%4==0) and (year%100!=0):
    print("LEAP")
else:
    print("COMMON")

#------------------------------------------------------------------------------


#task5-------------------------------------------------------------------------
"""

Умова: Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. 
Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо 
два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа 
різні).

Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести ціле число
"""
#прогрма для визначеня кількості однакових чисел
#number1,number2,nember3 - цілі числа
number1 = int(input())
number2 = int(input())
number3 = int(input())
#визначеня кількості однакових чисел 
if (number1==number2) and (number2==number3):
    print(3)
elif (number1==number2) or (number2==number3) or (number1==number3):
    print(2)
else:
    print(0)

#------------------------------------------------------------------------------


#task6-------------------------------------------------------------------------
"""

Умова: Шахова тура переміщається по горизонталі або по вертикалі. Дано координа 
ти двох клітин шахової дошки. Визначити, чи може тура перейти з першої клітини 
у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з 
яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої 
клітини, останні два числа – для другої. Програма має вивести "YES", якщо тура 
може виконати переміщення, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""
#Програма для визначеня можливости ходу тури
#Ввід координат початкової точки
x1 = int(input())
y1 = int(input())
#Ввід координат кінцевої точки
x2 = int(input())
y2 = int(input())
#Перевірка на можливість ходу
if (x1==x2) or (y1==y2):
    print("YES")
else:
    print("NO")
#------------------------------------------------------------------------------


#task7-------------------------------------------------------------------------
"""
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони
кольору. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких 
визначає номер рядку та стовпчика клітини. Перші два числа - для першої 
клітини, останні два числа – для другої. Програма має вивести "YES", якщо 
колір однаковий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""
#Програма для визначення однаковості  кольору клітинок
#Запис перших координат
x1 = int(input())
y1 = int(input())
#Запис других координат
x2 = int(input())
y2 = int(input())
#Якщо остача від ділення однакова то клітинки одного кольору
if ((x1-x2)%2==(y1-y2)%2):
    print("YES")
else:
    print("NO")
#------------------------------------------------------------------------------


#task8-------------------------------------------------------------------------
"""

Умова: Шаховий король переміщується по горизонталі, по вертикалі або по 
діагоналі на будь-яку сусідню клітинку. Дано координати двох клітин шахової 
дошки. Визначити, чи може король перейти з першої клітини у другу за один хід. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер 
рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два 
числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в 
іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""
#Програма на можливість ходу короля
#координата початку 
x1 = int(input())
y1 = int(input())
#Координата закінчення
x2 = int(input())
y2 = int(input())
#Перевірка можливості 
if (x1==x2+1) and ((y1==y2+1) or (y1==y2-1) or (y1==y2)):
    print("YES")
elif (x1==x2-1) and ( (y1==y2-1) or (y1==y2+1) or (y1==y2)):
    print("YES")
elif (x1==x2) and ((y1==y2-1) or (y1==y2+1)):
    print("YES")
else:
    print("NO")

#------------------------------------------------------------------------------


#task9-------------------------------------------------------------------------
"""
Умова: Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано 
координати двох клітин шахової дошки. Визначити, чи може слон перейти з першої 
клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, 
кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для 
першої клітини, останні два числа – для другої. Програма має вивести "YES", 
якщо хід можливий, або "NO" в іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""
#Програма для перевірки можливості можливості ходу слона
#Координати почадку ходу
x1 = int(input())
y1 = int(input())
#Координати закінчення ходу
x2 = int(input())
y2 = int(input())
#Перевірка можливості 
if abs(x2-x1)==abs(y2-y1):
    print("YES")
else:
    print("NO")

#------------------------------------------------------------------------------


#task10------------------------------------------------------------------------
"""

Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі 
на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. 
Визначити, чи може королева перейти з першої клітини у другу за один хід. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер 
рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два 
числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в 
іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""
x1 = int(input())

y1 = int(input())

x2 = int(input())

y2 = int(input())

if x2-x1==y2-y1:

    print("YES")

elif x2-x1==y1-y2:

    print("YES")

elif (x1==x2) or (y1==y2):

    print("YES")

else:

    print("NO")

#------------------------------------------------------------------------------


#task11------------------------------------------------------------------------
"""

Умова: Шаховий кінь рухається як літера L. Він може переміщатись на дві 
клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по 
вертикалі і одну по горизонталі. Дано координати двох клітин шахової дошки. 
Визначити, чи може кінь перейти з першої клітини у другу за один хід. 
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер 
рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два 
числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в 
іншому випадку.

Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.

Вихідні дані: вивести текстовий рядок.
"""
#Програма для перевірки можливості ходу коня
#Координати початку ходу
x1 = int(input())
y1 = int(input())
#Координати початку ходу
x2 = int(input())
y2 = int(input())
#Перевірка ходу
if ((x1==x2+2) or (x1==x2-2)) and ((y1==y2+1) or (y1==y2-1)):
    print("YES")
elif ((x1==x2+1) or (x1==x2-1)) and ((y1==y2+2) or (y1==y2-2)):
    print("YES")
else:
    print("NO")

#------------------------------------------------------------------------------


#task12------------------------------------------------------------------------
"""

Умова: Шоколад має форму прямокутника, розділеного на n?m клітин. Шоколад може 
бути розділений на дві частини тільки по горизонталі або по вертикалі, при 
цьому клітини мають бути цілими. Визначити, чи можна розділити шоколад за один 
крок таким чином, щоб одна з частин матиме точно k клітин. Програма має 
вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.

Вхідні дані: 3 цілих числа: n,m, k. Кожне число користувач вводить в окремому 
рядку.

Вихідні дані: вивести текстовий рядок.
"""
#Програма на можливість поділу шоколадки на 2 частини
#Шоколадка розміром n на m
n = int(input())
m = int(input())
#Площу неохыдної частини
k = int(input())
#Перевірка 
if (k%n==0) and (k<n*m):
    print("YES")
elif (k%m==0) and (k<n*m):
    print("YES")
else:
    print("NO")

#------------------------------------------------------------------------------