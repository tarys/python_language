#task1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Даны два целых числа. Выведите значение наименьшего из них.
"""
first_usr_numb=int(input('Введите первое число'))
second_usr_numb=int(input('Введите второе число'))

if first_usr_numb<second_usr_numb:
    print('Наименьшее: ',first_usr_numb)
elif first_usr_numb>second_usr_numb:
    print('Наименьшее: ',second_usr_numb)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
В математике функция sign(x) (знак числа) определена так:
sign(x) = 1, если x > 0,
sign(x) = -1, если x < 0,
sign(x) = 0, если x = 0.
Для данного числа x выведите значение sign(x).
Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.
"""
user_numb=int(input('Введите ваше число'))

if user_numb>0:
     print(1)#ЕСЛИ ЧИСЛО ПОЛОЖИТЕЛЬНОЕ
elif user_numb<0:
     print(-1)#ЕСЛИ ЧИСЛО ОТРИЦАТЕЛЬНОЕ
else :
     print(0)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Заданы две клетки шахматной доски.
Если они покрашены в один цвет, то выведите слово YES,
а если в разные цвета — то NO.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки.
"""
import sys
first_data_of_chess_x=int(input('Введите первую координату для Х: (от 1 до 8)'))
first_data_of_chess_y=int(input('Введите первую координату для Y: (от 1 до 8)'))
second_data_of_chess_x=int(input('Введите вторую координату для Х: (от 1 до 8)'))
second_data_of_chess_y=int(input('Введите вторую координату для Y: (от 1 до 8)'))

if (first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y >8 )or(first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y <0 ):
    sys.exit('Input ERR')

if (first_data_of_chess_y+first_data_of_chess_x+second_data_of_chess_y+second_data_of_chess_x)%2==0:
    print('YES')
else:
    print('NO')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Дано натуральное число.
Требуется определить, является ли год с данным номером високосным.
Если год является високосным, то выведите YES, иначе выведите NO.
Напомним, что в соответствии с григорианским календарем, год является високосным,
если его номер кратен 4, но не кратен 100, а также если он кратен 400.
"""
user_year=int(input('Введите год'))

if (user_year%400==0)or(user_year%4==0 and user_year%100!=0):
    print('Высокосный')
else:
    print('Не высоосный')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Даны три целых числа. Выведите значение наименьшего из них.
"""
fst_usr_numb=int(input('Введите первое число'))
scd_usr_numb=int(input('Введите второе число'))
thd_usr_numb=int(input('Введите третье число'))

if fst_usr_numb < scd_usr_numb and fst_usr_numb<thd_usr_numb :
    print('Наименьшее: ', fst_usr_numb)
elif scd_usr_numb<fst_usr_numb and scd_usr_numb<thd_usr_numb :
    print('Наименьшее: ', scd_usr_numb)
else:
    print('Наименьшее: ', thd_usr_numb)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Даны три целых числа.
Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают),
2 (если два совпадает) или 0 (если все числа различны).
"""
fst_usr_numb=int(input('Введите первое число'))
scd_usr_numb=int(input('Введите второе число'))
thd_usr_numb=int(input('Введите третье число'))

if fst_usr_numb == scd_usr_numb and fst_usr_numb==thd_usr_numb :
    print('3 - Все совпадают')
elif scd_usr_numb==fst_usr_numb or scd_usr_numb==thd_usr_numb :
    print('2 - Два совпадают')
else:
    print('0 - Все разные')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Шахматная ладья ходит по горизонтали или вертикали.
Даны две различные клетки шахматной доски, определите,
может ли ладья попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки. Программа должна вывести YES,
если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.
"""
import sys
first_data_of_chess_x=int(input('Введите первую координату для Х: (от 1 до 8)'))
first_data_of_chess_y=int(input('Введите первую координату для Y: (от 1 до 8)'))
second_data_of_chess_x=int(input('Введите вторую координату для Х: (от 1 до 8)'))
second_data_of_chess_y=int(input('Введите вторую координату для Y: (от 1 до 8)'))

if (first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y >8 )or(first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y <0 ):
    sys.exit('Input ERR')

if first_data_of_chess_x==second_data_of_chess_x or first_data_of_chess_y==second_data_of_chess_y :
    print('YES')
else:
    print('NO')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task8~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Шахматный слон ходит по диагонали.
Даны две различные клетки шахматной доски, определите,
может ли слон попасть с первой клетки на вторую одним ходом.
"""
import sys
first_data_of_chess_x=int(input('Введите первую координату для Х: (от 1 до 8)'))
first_data_of_chess_y=int(input('Введите первую координату для Y: (от 1 до 8)'))
second_data_of_chess_x=int(input('Введите вторую координату для Х: (от 1 до 8)'))
second_data_of_chess_y=int(input('Введите вторую координату для Y: (от 1 до 8)'))

if (first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y >8 )or(first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y <0 ):
    sys.exit('Input ERR')

if abs(first_data_of_chess_x==second_data_of_chess_x)==abs(first_data_of_chess_y==second_data_of_chess_y):
    print('YES')
else:
    print('NO')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task9~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Шахматный король ходит по горизонтали, вертикали и диагонали,
но только на 1 клетку. Даны две различные клетки шахматной доски,
определите, может ли король попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки. Программа должна вывести YES,
если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.
"""
import sys
first_data_of_chess_x=int(input('Введите первую координату для Х: (от 1 до 8)'))
first_data_of_chess_y=int(input('Введите первую координату для Y: (от 1 до 8)'))
second_data_of_chess_x=int(input('Введите вторую координату для Х: (от 1 до 8)'))
second_data_of_chess_y=int(input('Введите вторую координату для Y: (от 1 до 8)'))

if (first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y >8 )or(first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y <0 ):
    sys.exit('Input ERR')

if 1<=((first_data_of_chess_x-second_data_of_chess_x)**2 + (first_data_of_chess_y-second_data_of_chess_y)**2)<=2:
    print('YES')
else:
    print('NO')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task10~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
Даны две различные клетки шахматной доски, определите,
может ли ферзь попасть с первой клетки на вторую одним ходом.
"""
import sys
first_data_of_chess_x=int(input('Введите первую координату для Х: (от 1 до 8)'))
first_data_of_chess_y=int(input('Введите первую координату для Y: (от 1 до 8)'))
second_data_of_chess_x=int(input('Введите вторую координату для Х: (от 1 до 8)'))
second_data_of_chess_y=int(input('Введите вторую координату для Y: (от 1 до 8)'))

if (first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y >8 )or(first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y <0 ):
    sys.exit('Input ERR')

if (first_data_of_chess_x==second_data_of_chess_x) or (first_data_of_chess_y==second_data_of_chess_y) or (abs(first_data_of_chess_x==second_data_of_chess_x)==abs(first_data_of_chess_y==second_data_of_chess_y)):
    print('YES')
else:
    print('NO')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task11~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
Шоколадку можно один раз разломить по прямой на две части. Определите,
можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек.
Программа получает на вход три числа: n, m, k и должна вывести YES или NO.
"""
border_long=int(input('Введите длину: '))
border_width=int(input('Введите ширину: '))
user_count=int(input('Введите количество отломаных долек: '))

if ((border_long*border_width)/2)<user_count:
    print('YES')
else:
    print('NO')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#task12~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Шахматный конь ходит буквой “Г” —
на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
или наоборот.
Даны две различные клетки шахматной доски, определите,
может ли конь попасть с первой клетки на вторую одним ходом.
"""
import sys
first_data_of_chess_x=int(input('Введите первую координату для Х: (от 1 до 8)'))
first_data_of_chess_y=int(input('Введите первую координату для Y: (от 1 до 8)'))
second_data_of_chess_x=int(input('Введите вторую координату для Х: (от 1 до 8)'))
second_data_of_chess_y=int(input('Введите вторую координату для Y: (от 1 до 8)'))

if (first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y >8 )or(first_data_of_chess_x or first_data_of_chess_y or second_data_of_chess_x or second_data_of_chess_y <0 ):
    sys.exit('Input ERR')

if (abs(first_data_of_chess_x-second_data_of_chess_x)==1 and abs(first_data_of_chess_y-second_data_of_chess_y)==2 )or(abs(first_data_of_chess_x-second_data_of_chess_x)==2 and abs(first_data_of_chess_y-second_data_of_chess_y)==1):
    print('YES')
else:
    print('NO')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
