#task1-------------------------------------------------------------------------------------------------------
"""

Даны два целых числа. Выведите значение наименьшего из них.

"""
#Програма для виведення мінімуму із двох чисел
first_number = int(input())#Введення першого числа
second_number = int(input())#Введення другого числа
if first_number > second_number: #Якщо х більше у то:
   print(second_number)#вивести у
else:#інакше: 
    print(first_number)#вивести х

#task2-------------------------------------------------------------------------------------------------------
"""

В математике функция sign(x) (знак числа) определена так: 
sign(x) = 1, если x > 0, 
sign(x) = -1, если x < 0, 
sign(x) = 0, если x = 0.
Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.

"""
#Програма для вирішення функції sign(x)
x  = int(input())#Введення змінної х
if x > 0:#Якщо виконується умова х>0:
    print ("1")#виведеться 1
elif x < 0:#Якщо виконується умова х<0:
    print("-1")#виведеться -1
else:#інакше
    print("0")#виведеться 0

#task3-------------------------------------------------------------------------------------------------------
"""

Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO. 
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

"""
#Програма для визначення кольору клітинок
first_coordinate_x_=int(input())#Введення першої х координати
first_coordinate_y_=int(input())#Введення першої у координати
second_coordinate_x_=int(input())#Введення другої х координати
second_coordinate_y_=int(input())#Введення другої y координати
if (first_coordinate_x_+first_coordinate_y_)%2==(second_coordinate_x_+second_coordinate_y_)%2:#Якщо виконується умова, що остача від ділення на 2 перших і других координат рівна(умова одинаковості клітинок)
    print("YES")#Виведеться Так
else:#інакше
    print("NO")#Виведеться Ні

#task4-------------------------------------------------------------------------------------------------------
"""

Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, 
то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, 
год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

"""
#Програма для визначення кольору клітинок
first_coordinate_x_=int(input())#Введення першої х координати
first_coordinate_y_=int(input())#Введення першої у координати
second_coordinate_x_=int(input())#Введення другої х координати
second_coordinate_y_=int(input())#Введення другої y координати
if (first_coordinate_x_+first_coordinate_y_)%2==(second_coordinate_x_+second_coordinate_y_)%2:#Якщо виконується умова, що остача від ділення на 2 перших і других координат рівна(умова одинаковості клітинок)
    print("YES")#Виведеться Так
else:#інакше


#task5-------------------------------------------------------------------------------------------------------
"""

Даны три целых числа. Выведите значение наименьшего из них.

"""
#Програма для обчислення мінімуму двох чисел
first_number = int(input())#Введення перше число
second_number = int(input())#Введення друге число
third_number = int(input())#Введення третє число
if first_number > second_number and third_number > second_number:
   print(second_number)#Виведення першого числа
elif second_number > first_number and third_number > first_number:
    print(first_number)#Виведення другого числа
elif second_number > third_number and first_number > third_number:
    print(third_number)#Виведення третього числа
else:#інакше
    print(first_number)#Виведення першого числа

#task6-------------------------------------------------------------------------------------------------------
"""

Даны три целых числа. Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

"""
first_number  = int(input())
second_number = int(input())
third_number = int(input())
if first_number == second_number == third_number :
    print(3)
elif first_number == second_number or first_number == third_number or third_number == second_number:
    print(2)
else:
    print(0)

#task7-------------------------------------------------------------------------------------------------------
"""

Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом. 
Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.

"""
#Програма для визначення того, чи може ходити тура
first_coordinate_x_ = int(input())#Введення першої х координати
first_coordinate_y_  = int(input())#Введення першої у координати
second_coordinate_x_  = int(input())#Введення другої х координати
second_coordinate_y_   = int(input())#Введення другої у координати
if first_coordinate_x_ == second_coordinate_x_   or first_coordinate_y_  == second_coordinate_y_:#Умова ходу тури
    print("YES")#Виведення "Так"
else:#інакше
    print("NO")#Виведення "Ні"

#task8-------------------------------------------------------------------------------------------------------
"""

Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку. Даны две различные клетки шахматной доски, 
определите, может ли король попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.

"""
#Програма для визначення того, чи може ходити король
first_coordinate_x_ = int(input())#Введення першої х координати
first_coordinate_y_  = int(input())#Введення першої у координати
second_coordinate_x_  = int(input())#Введення другої х координати
second_coordinate_y_   = int(input())#Введення другої у координати
if abs(first_coordinate_x_-second_coordinate_x_)<2 and abs(first_coordinate_y_-second_coordinate_y_)<2:#Умова ходу короля
    print("YES")#Виведення "Так"
else:#інакше
    print("NO")#Виведення "Ні"

#task9------------------------------------------------------------------------------------------------------
"""

Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.

"""
#Програма для визначення того, чи може ходити слон
first_coordinate_x_ = int(input())#Введення першої х координати
first_coordinate_y_  = int(input())#Введення першої у координати
second_coordinate_x_  = int(input())#Введення другої х координати
second_coordinate_y_   = int(input())#Введення другої у координати
if abs(first_coordinate_x_-second_coordinate_x_)==abs(first_coordinate_y_-second_coordinate_y_):#Умова ходу слона
    print("YES")#Виведення "Так"
else:#інакще
    print("NO")#Виведення "Ні"

#task10-------------------------------------------------------------------------------------------------------
"""

Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две 
различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.

"""
#Програма для визначення того, чи може ходити ферзь
first_coordinate_x_ = int(input())#Введення першої х координати
first_coordinate_y_  = int(input())#Введення першої у координати
second_coordinate_x_  = int(input())#Введення другої х координати
second_coordinate_y_   = int(input())#Введення другої у координати
if (abs(first_coordinate_x_-second_coordinate_x_)==abs(first_coordinate_y_-second_coordinate_y_)) or ((first_coordinate_x_==second_coordinate_x_) or (first_coordinate_y_==second_coordinate_y_)):#Умова ходу ферзя
    print("YES")#Виведення "Так"
else:#інакше
    print("NO")#Виведення "Ні"

#task11-------------------------------------------------------------------------------------------------------
"""

Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали, или наоборот. 
Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую одним ходом.

"""
#Програма для визначення того, чи може ходити кінь
first_coordinate_x_ = int(input())#Введення першої х координати
first_coordinate_y_  = int(input())#Введення першої у координати
second_coordinate_x_  = int(input())#Введення другої х координати
second_coordinate_y_   = int(input())#Введення другої у координати
if (abs(first_coordinate_x_-second_coordinate_x_)==2 and abs(first_coordinate_y_-second_coordinate_y_)==1) or (abs(first_coordinate_x_-second_coordinate_x_)==1 and abs(first_coordinate_y_-second_coordinate_y_)==2):#Умова ходу коня
    print("YES")#Виведення "Так"
else:#інакше
    print("NO")#Виведення "Ні"

#task12-------------------------------------------------------------------------------------------------------
"""

Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по прямой на две части. Определите, 
можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек. 
Программа получает на вход три числа: n, m, k и должна вывести YES или NO.

"""
#Програма для визначення чи можна відламати від шоколадки частина, що складається рівно з k часточок.
cols = int(input())#Введення кількості рядків
raws = int(input())#Введення кількості стовбчиків
number_of_deviding = int(input())#Введення кількості поділів
if (number_of_deviding%cols==0 or number_of_deviding%raws==0) and (number_of_deviding<=cols*raws):#Умова поділу шоколадки
    print("YES")#Виведення "Так"
else:#інакше
    print("NO")#Виведення "Ні"
