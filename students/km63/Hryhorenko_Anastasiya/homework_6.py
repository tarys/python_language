#task1--------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""
def input_elem():
    list = input().split()
    return list
def even_ind(elements):
	list = []
    for i in range(0, len(elements), 2):
        list.append(elements[i])
    return list
def print_elem(list):
    for i in list:
        print (i, end=' ')
print_elem(even_ind(input_elem()))

#-----------------------------------------


#task2--------------------------
"""
Выведите все четные элементы списка.
"""
def input_elem():
    list = input().split()
    return list
def even_elem(elements):
    list = []
    for i in elements:
        if int(i) % 2 == 0:
            list.append(i)
    return list
def print_elem(list):
    for i in list:
        print (i, end=' ')
print_elem(even_elem(input_elem()))


#-----------------------------------------


#task3--------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
def input_elem():
    list = input().split()
    return list
def greater_elements(elements):
    list = []
    for i in range(len(elements)):
        if i < len(elements) - 1:
            if int(elements[i]) < int(elements[i + 1]):
                list.append(elements[i +1])
    return list
def print_elem(list):
    for i in list:
        print (i, end=' ')
print_elem(greater_elements(input_elem()))


#-----------------------------------------


#task4--------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, 
выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. 
Если таких пар соседей несколько — выведите первую пару.
"""
def input_elem():
    list = input().split()
    return list
def samesign_elem(elements):
    list = []
    for i in range(0, len(elements)):
        if len(list) == 0:
            if i < len(elements)-1:
                if int(elements[i]) * int(elements[i + 1]) > 0:
                    list = [elements[i]]
                    list.append(elements[i + 1])
    return list
def print_elem(list):
    for i in list:
        print (i, end=' ')
print_elem(samesign_elem(input_elem()))


#-----------------------------------------


#task5--------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов, 
которые больше двух своих соседей, и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
def input_elem():
    list = input().split()
    return list
def greater_elements(elements):
    count_of_elem = 0
    for i in range(1, len(elements)-1):
        if int(elements[i-1]) < int(elements[i]) > int(elements[i+1]):
            count_of_elem +=1
    return count_of_elem
def print_elem(output_data):
    print (output_data)
print_elem(greater_elements(input_elem()))


#-----------------------------------------


#task6--------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке, 
а затем индекс этого элемента в списке. Если наибольших элементов несколько, 
выведите индекс первого из них.
"""
list = [int(i) for i in input().split()]
index = 0
for i in range(1, len(list)):
    if list[i] > list[index]:
        index = i
print(list[index], index)

#-----------------------------------------
#task7--------------------------
"""
Петя перешёл в другую школу. 
На уроке физкультуры ему понадобилось определить своё место в строю. 
Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, 
означающих рост каждого человека в строю. После этого вводится число X – рост Пети. 
Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. 
Если в строю есть люди с одинаковым ростом, таким же, как у Пети, 
то он должен встать после них.
"""
def input_elem():
    list = input().split()
    return list
def find_number(elements):
    hight = int(input())
    number = 0
    while number < len(elements) and int(elements[number]) >= hight:
        number += 1
    return number
def print_elem(list):
        print (list + 1)
print_elem(find_number(input_elem()))

#-----------------------------------------
#task8--------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем. 
Определите, сколько в нем различных элементов.
"""
def input_elem():
    list = input().split()
    return list
def count_of_different(elements):
    count = 0
    for i in range(0, len(elements)-1):
        if int(elements[i]) != int(elements[i + 1]):
            count +=1
    return count
def print_elem(list):
        print (list + 1)
print_elem(count_of_different(input_elem()))

#-----------------------------------------
#task9--------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). 
Если элементов нечетное число, то последний элемент остается на своем месте.
"""
def input_elem():
    list = input().split()
    return list
def replace_elem(elements):
    for i in range(0, len(elements)//2):
	    elements[i*2], elements[i*2 + 1] = elements[i*2 + 1], elements[i*2]
    return elements
def print_elem(list):
    for i in list:
        print (i, end=' ')
print_elem(replace_elem(input_elem()))


#-----------------------------------------
#task10--------------------------
"""
В списке все элементы различны. 
Поменяйте местами минимальный и максимальный элемент этого списка.
"""

list = [int(x) for x in input().split()]
index_of_min = 0
index_of_max = 0
for i in range(1, len(list)):
    if list[i] > list[index_of_max]:
        index_of_max = i
    if list[i] < list[index_of_min]:
        index_of_min = i
list[index_of_min], list[index_of_max] = list[index_of_max], list[index_of_min]
print(' '.join([str(i) for i in list]))

#-----------------------------------------
#task11--------------------------
"""
Дан список из чисел и индекс элемента в списке k. 
Удалите из списка элемент с индексом k, 
сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. 
Программа сдвигает все элементы, а после этого удаляет последний элемент 
списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, 
а не делать это при выводе элементов. Также нельзя использовать дополнительный список. 
Также не следует использовать метод pop(k) с параметром.
"""

def input_elem():
    list = input().split()
    return list
def delete_elem(elements):
    k = int(input())
    for i in range(k, len(elements) - 1):
        elements[i] = elements[i + 1]
    elements.pop()
    return elements
def print_elem(list):
    for i in list:
        print (i, end=' ')
print_elem(delete_elem(input_elem()))

#-----------------------------------------
#task12--------------------------
"""
Дан список целых чисел, число k и значение C. 
Необходимо вставить в список на позицию с индексом k элемент, 
равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, 
после считывания списка в его конец нужно будет добавить новый элемент, 
используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого 
при выводе и не создавая дополнительного списка.
"""

list = [int(s) for s in input().split()]
k, C = [int(s) for s in input().split()]
list.append(0)
for i in range(len(list) - 1, k, -1):
    list[i] = list[i - 1]
list[k] = C
print(' '.join([str(i) for i in list]))

#-----------------------------------------
#task13--------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, 
равных друг другу. Считается, что любые два элемента, 
равные друг другу образуют одну пару, которую необходимо посчитать.
"""
list = [int(x) for x in input().split()]
count = 0
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            count += 1
print(count)

#-----------------------------------------


#task14--------------------------
"""
Дан список. Выведите те его элементы, 
которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, 
в котором они встречаются в списке.
"""
list = [int(x) for x in input().split()]
for i in range(len(list)):
    for j in range(len(list)):
        if i != j and list[i] == list[j]:
            break
    else:
        print(list[i], end=' ')

#-----------------------------------------

#task15--------------------------
"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. 
Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с 
номерами от li до ri включительно. Определите, какие кегли остались 
стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. 
Далее идет K пар чисел li, ri, при этом 1? li? ri? N.

Программа должна вывести последовательность из N символов, где j-й символ 
есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""
a = [int(s) for s in input().split()]
c = ['I']*a[0]
for i in range(a[1]):
        b = [int(s) for s in input().split()]
        for k in range(b[0]-1,b[1]):
            c[k] = '.'
print(''.join(c))

#-----------------------------------------
#task16--------------------------
"""
Условие
Известно, что на доске 8?8 можно расставить 8 ферзей так, чтобы они не 
били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, 
каждое число от 1 до 8 — координаты 8 ферзей. 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""
coord_X = []
coord_Y = []
for i in range(8):
    list = input().split(' ')
    coord_X.append(int(list[0]))
    coord_Y.append(int(list[1]))
list_of_abs =[]
for k in range(8):
        list_of_abs.append(abs(int(coord_X[k])-int(coord_Y[k])))
if len(coord_X) != len(set(coord_X)) and len(coord_Y) != len(set(coord_Y)) or len(list_of_abs) != len(set(list_of_abs)):
    print('NO')
else:
    print('YES')
#-----------------------------------------

