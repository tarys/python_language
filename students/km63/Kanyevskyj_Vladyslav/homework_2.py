#task1------------------------------------------------------------
"""
Задача №1 
Умова: Дано два цілих числа. Вивести найменше з них.
Вхідні дані: користувач вводить ціле число
Вихідні дані: вивести ціле число
"""



#
a=int(input())
b=int(input())
if a<b:
    print(a)
else :
    print(b)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""

Задача №2
Умова: Вивести результат функції sign(x), що визначається наступним чином: 
sign(x)=1,ifx>0, 
sign(x)=-1,ifx<0, 
sign(x) = 0, if x = 0..
Вхідні дані: користувач вводить дійсне число.
Вихідні дані: вивести результат sign.
"""



#
x = float(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Задача №3 
Умова: Дано три цілих числа. Вивести найменше з них.
Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести ціле число
"""



#
 x=int(input))
y=int(input))
z=int(input))
if x<y<z :
    print(x)
elif x<z<y :
    print(x)
elif y<x<z :
    print(y)
elif y<z<x :
    print(y)
else :	
    print(z)


#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""

Задача №4 
Умова: Дано ціле число, що визначає рік. Визначити, чи є вказаний рік високосним. Якщо так, то вивести користувачу "LEAP", в іншому випадку – "СOMMON".
Рік високосний, якщо виконується хоча б одна з умов:
	рік завжди високосним, якщо його номер ділиться на 4 без остачі і не ділиться без остачі на 100
	рік завжди високосним, якщо його номер ділиться на 400 без остачі
Вхідні дані: ціле число, що вводить користувач
Вихідні дані: вивести текстовий рядок.
"""



#
x = int(input())
if x%4==0 and x%100!=0:    
    print("LEAP")
elif x%400==0:
    print("LEAP")
else:
    print("COMMON")
 
#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""

Задача №5 
Умова: Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. Програма повинна виводити одне з чисел: 3 (якщо всі числа однакові), 2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).
Вхідні дані: 3 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести ціле число
"""



#
x = int(input())
y = int(input())
z = int(input())
if x == y == z:
    print(3)
elif y==x and x!=z:
    print(2)
elif y==z and x!=y:
    print(2)
elif x==z and y!=x:
    print(2)
elif x!=y!=z:	
    print(0)
 

#-----------------------------------------------------------------



#task6------------------------------------------------------------
"""

Задача №6 
Умова: Шахова тура переміщається по горизонталі або по вертикалі. Дано координати двох клітин шахової дошки. Визначити, чи може тура перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо тура може виконати переміщення, або "NO" в іншому випадку.
Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести текстовий рядок.
"""



#
# х,у - координати першої клітинки
# a,b - координати другої клітинки
x = int(input())
y = int(input())
a = int(input())
b = int(input())
if x == a or y==b:
    print("YES")
else :
    print("NO")	
#-----------------------------------------------------------------



#task7------------------------------------------------------------
"""

Задача №7
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.
Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести текстовий рядок.
"""



#
# х,у - координати першої клітинки
# a,b - координати другої клітинки
x = int(input())
y = int(input())
a = int(input())
b = int(input())
if (x+y)%2==0 and (a+b)%2==0 :
    print("YES")
elif (x+y)%2!=0 and (a+b)%2!=0 :
    print("YES")
else :
    print("NO") 

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""

Задача №8
Умова: Шаховий король переміщується по горизонталі, по вертикалі або по діагоналі на будь-яку сусідню клітинку. Дано координати двох клітин шахової дошки. Визначити, чи може король перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести текстовий рядок.
"""



#
# х,у - координати першої клітинки
# a,b - координати другої клітинки
x = int(input())
y = int(input())
a = int(input())
b = int(input())
if -1<=(x-a)<=1 and -1<=(y-b)<=1:
    print("YES")
else:
    print("NO")
 

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""

Задача №9
Умова: Шаховий слон рухається по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може слон перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести текстовий рядок.
"""



#
# х,у - координати першої клітинки
# a,b - координати другої клітинки
x = int(input())
y = int(input())
a = int(input())
b = int(input())
if abs(x - a) == abs(y - b):
    print("YES")
else:
    print("NO")
 

#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""

Задача №10
Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин. Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести текстовий рядок.
"""



#
# х,у - координати першої клітинки
# a,b - координати другої клітинки
x = int(input())
y = int(input())
a = int(input())
b = int(input())
if abs(x - a) == abs(y - b):
    print("YES")
elif x == a or y==b:
    print("YES")
else :	
    print("NO")
 
	
#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""

Задача №11
Умова: Шаховий кінь рухається як літера L. Він може переміщатись на дві клітинки по горизонталі і одну клітинку по вертикалі або на дві клітинки по вертикалі і одну по горизонталі. Дано координати двох клітин шахової дошки. Визначити, чи може кінь перейти з першої клітини у другу за один хід. Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
Вхідні дані: 4 цілих числа.  Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести текстовий рядок.
тувач вводить в окремому рядку.
Вихідні дані: вивести текстовий рядок.
"""



#
# х,у - координати першої клітинки
# a,b - координати другої клітинки
x=int(input())
y = int(input())
a = int(input())
b = int(input())
if abs(x-a)==2 and abs(y-b)==1:
    print("YES")
elif abs(x-a)==1 and abs(y-b)==2:
    print("YES")
else:	
    print("NO") 

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""

Задача №12
Умова: Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад може бути розділений на дві частини тільки по горизонталі або по вертикалі, при цьому клітини мають бути цілими. Визначити, чи можна розділити шоколад за один крок таким чином, щоб одна з частин матиме точно k клітин. Програма має вивести "YES", якщо шоколад можна поділити, або "NO" в іншому випадку.
Вхідні дані: 3 цілих числа: n,m, k. Кожне число користувач вводить в окремому рядку.
Вихідні дані: вивести текстовий рядок.
"""



#
n = int(input())
m = int(input())
k = int(input())
if n*m-k==n or n*m-k==m and n*m>k and k!=1:
    print("YES")
elif (n*m-k)%2==0 and n*m>k and k!=1:
     print("YES")
else:	
    print("NO")
 

#-----------------------------------------------------------------
