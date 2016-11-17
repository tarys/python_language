# -*- coding: utf-8 -*-

"""
    Домашня робота №6
    Тема: "list"
    Студент: Козирєв Антон Юрійович
    Група: КМ - 62
"""

import math

#Task_1----------------------------------------------------#

"""
    Условие
    Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""

List = input().split()
Even_List = []
for i in range(len(List)):
    if i % 2 == 0:
        Even_List.append(List[i])
print(' '.join(Even_List))

#----------------------------------------------------------#

#Task_2----------------------------------------------------#

"""
    Условие
    Выведите все четные элементы списка.
    При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""

List = input().split()
Even_List = []
for element in List:
    if int(element) % 2 == 0:
        Even_List.append(element)
print(' '.join(Even_List))

#----------------------------------------------------------#

#Task_3----------------------------------------------------#

"""
    Условие
    Дан список чисел.
    Выведите все элементы списка, которые больше предыдущего элемента.
"""

List = input().split()
Increase_List = []
TempNumber = int(List[0]) #Template number
for element in List:
    if TempNumber < int(element):
        TempNumber = int(element)
        Increase_List.append(element)
    TempNumber = int(element)
print(' '.join(Increase_List))

#----------------------------------------------------------#

#Task_4----------------------------------------------------#

"""
    Условие
    Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
    Если соседних элементов одного знака нет — не выводите ничего.
    Если таких пар соседей несколько — выведите первую пару.
"""

List = input().split()
Increase_List = []
for i in range(len(List) - 1):
    if int(List[i]) * int(List[i+1]) > 0: # (-a)*(-a)>0 & a*a>0 
        Increase_List.append(List[i])
        Increase_List.append(List[i + 1])
        break #Only one pair
print(' '.join(Increase_List))

#----------------------------------------------------------#

#Task_5----------------------------------------------------#

"""
    Условие
    Дан список чисел.
    Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
    Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""

List = input().split()
MoreThan_Numbers = 0
for i in range(len(List) - 2):
    if int(List[i]) < int(List[i+1]) and int(List[i+2]) < int(List[i+1]):
        MoreThan_Numbers += 1
print(MoreThan_Numbers)

#----------------------------------------------------------#

#Task_6----------------------------------------------------#

"""
    Условие
    Дан список чисел.
    Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
    Если наибольших элементов несколько, выведите индекс первого из них.
"""

List = input().split()
Maximal_element = int(List[0])
Index = 0
for i in range(len(List)):
    if Maximal_element < int(List[i]):
        Maximal_element = int(List[i])
        if int(List[i - 1]) < int(List[i]):
            Index = i #Only first element
    
print(Maximal_element, Index)

#----------------------------------------------------------#

#Task_7----------------------------------------------------#

"""
    Условие
    Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
    Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю.
    После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
    Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""

Lineup = input().split()
Hight_Petya = input()
Count = 0
for i in range(len(Lineup)):
    if int(Lineup[len(Lineup) - 1]) > int(Hight_Petya): # Hight_Petya < Last element
        Count = len(Lineup)
        break
    if int(Lineup[i]) >= int(Hight_Petya) and int(Lineup[i + 1]) < int(Hight_Petya):
        Count = i + 1
        break
print(Count + 1)

#----------------------------------------------------------#

#Task_8----------------------------------------------------#

"""
    Условие
    Дан список, упорядоченный по неубыванию элементов в нем.
    Определите, сколько в нем различных элементов.
"""

List = input().split()
Num_distinct = 1
for i in range(len(List) - 1):
    if int(List[i]) != int(List[i+1]):
        Num_distinct += 1
    
print(Num_distinct)

#----------------------------------------------------------#

#Task_9----------------------------------------------------#

"""
    Условие
    Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
    Если элементов нечетное число, то последний элемент остается на своем месте.
"""

List = input().split()
for i in range(len(List) // 2):
    Swap_Value = List [2 * i] # Template var
    List [2 * i] = List[2*i + 1]
    List[2*i + 1] = Swap_Value   
print(' '.join(List))

#----------------------------------------------------------#

#Task_10---------------------------------------------------#

"""
    Условие
    В списке все элементы различны.
    Поменяйте местами минимальный и максимальный элемент этого списка.
"""

List = input().split()
Index_Min = 0
Index_Max = 0
Maximal_element = int(List[0])
Minimal_element = int(List[0])
for i in range(len(List)):
    if Maximal_element < int(List[i]):
        Maximal_element = int(List[i])
        if int(List[i - 1]) < int(List[i]):
            Index_Max = i #Only first element
            
for i in range(len(List)):
    if Minimal_element > int(List[i]):
        Minimal_element = int(List[i])
        if int(List[i - 1]) > int(List[i]):
            Index_Min = i #Only first element


Swap_Value = List [Index_Min] # Template var
List[Index_Min] = List[Index_Max]
List[Index_Max] = Swap_Value  

print(' '.join(List))

#----------------------------------------------------------#

#Task_11---------------------------------------------------#

"""
    Условие
    Дан список из чисел и индекс элемента в списке k.
    Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
    Программа получает на вход список, затем число k.
    Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.
    Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
    Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.
"""

List = input().split()
Index_K = int(input())

Swap_Value = List[Index_K]
Prelast_Value = List[len(List) - 1]
for i in range(len(List) - 1 - Index_K):
    List[i + Index_K] = List[i + 1 + Index_K]
List[len(List) - 2] = Prelast_Value
List[len(List) - 1] = Swap_Value

List.pop()
print(' '.join(List))

#----------------------------------------------------------#

#Task_12---------------------------------------------------#

"""
    Условие
    Дан список целых чисел, число k и значение C.
    Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
    Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.
    Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
"""

List = input().split() 
List_of_Value = input().split()
Index_K = int(List_of_Value[0])
Value_to_insert_C = List_of_Value[1]

List.append(Value_to_insert_C)

for i in range(len(List) - 1 - Index_K):
    Swap_Value = List[len(List) - i - 2]
    List[len(List) - i - 2] = List[len(List) - i - 1]
    List[len(List) - i - 1] = Swap_Value

print(' '.join(List))

#----------------------------------------------------------#

#Task_13---------------------------------------------------#

"""
    Условие
    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""

List = input().split()
Pars = 0

for i in range(len(List) - 1):
    Comparing_Value = List[i]
    for j in range((len(List) - i) - 1):
        if Comparing_Value == List [j + i + 1]:
            Pars += 1
            
print(Pars)

#----------------------------------------------------------#

#Task_14---------------------------------------------------#

"""
    Условие
    Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

List = input().split()
Unique_elements = []
Equals = 0

for i in range(len(List)):
    for j in range(len(List)):
        if i != j:
            if List[i] == List [j]:
                Equals += 1
    if Equals == 0:
        Unique_elements.append(List[i])
    Equals = 0
print(' '.join(Unique_elements))

#----------------------------------------------------------#

#Task_15---------------------------------------------------#

"""
    Условие
    N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N.
    Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно.
    Определите, какие кегли остались стоять на месте. Программа получает на вход количество кеглей N и количество бросков K.
    Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N. 
    Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""

List_Value = input().split()
Skittles_N = int(List_Value[0])
Tries_K = int(List_Value[1])
Dot = "."
Skittles_List = ["I"] * Skittles_N

for i in range(Tries_K):
    Amount_Kick = input().split()
    First_Kick = int(Amount_Kick[0]) 
    Last_Kick = int(Amount_Kick[1]) 
    for i in range(Last_Kick - First_Kick + 1):
        Skittles_List[(First_Kick + i) - 1] = Dot

print(''.join(Skittles_List))

#----------------------------------------------------------#

#Task_16---------------------------------------------------#

"""
    Условие
    N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N.
    Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно.
    Определите, какие кегли остались стоять на месте. Программа получает на вход количество кеглей N и количество бросков K.
    Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N. 
    Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""

Answer = "NO"
Row = []
Column = []

for i in range(8):
    Pair = input().split()
    Row.append(Pair[0])
    Column.append(Pair[1])

for i in range(8):
    for j in range(8):
        if i != j:
            Delta_Row = math.fabs(int(Row[i]) - int(Row[j])) #Row distance between two queens
            Delta_Column = math.fabs(int(Column[i]) - int(Column[j])) #Column distance between two queens
            if (Row[i] == Row[j]) or (Column[i] == Column[j]) or (Delta_Row == Delta_Column):
                Answer = "YES"
                
print(Answer)

#----------------------------------------------------------#