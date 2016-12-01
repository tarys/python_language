#task1--------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

for i in range(0, len(my_list), 2):
    print(my_list[i])



#-----------------------------------------


#task2--------------------------
"""
Выведите все четные элементы списка.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

for element in my_list:
    if element % 2 == 0:
        print element


#-----------------------------------------
#task3--------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

for i in range(1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        print my_list[i]


#-----------------------------------------


#task4--------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака,
выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

for i in range(1, len(my_list)):
    if my_list[i] ^ my_list[i-1] >= 0:
        print my_list[i-1], my_list[i]
        break


#-----------------------------------------


#task5--------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов,
которые больше двух своих соседей, и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()
counter = 0

for i in range(1, len(my_list) - 1):
    if my_list[i] > my_list[i - 1] and my_list[i] > my_list[i + 1]:
        counter += 1

print counter


#-----------------------------------------


#task6--------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке,
а затем индекс этого элемента в списке. Если наибольших элементов несколько,
выведите индекс первого из них.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

max_element, max_index = 0, 0
for index, element in enumerate(my_list):
    if element > max_element:
        max_element = element
        max_index = index

print ("Max element: {}, Max index: {}".format(max_element, max_index))


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
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()
height = int(input("Enter Petr`s height: "))

for index, element in enumerate(my_list):
    if height > element:
        print index
        break

#-----------------------------------------


#task8--------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем.
Определите, сколько в нем различных элементов.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()
unique_list = []

for element in my_list:
    if element not in unique_list:
        unique_list.append(element)

print ("Count of different elements: {}".format(len(unique_list)))

#-----------------------------------------


#task9--------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print my_list

#-----------------------------------------


#task10--------------------------
"""
В списке все элементы различны.
Поменяйте местами минимальный и максимальный элемент этого списка.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

max_element, max_element_index = 0, 0
min_element, min_element_index = my_list[0], 0

for index, element in enumerate(my_list):
    if element > max_element:
        max_element = element
        max_element_index = index
    elif element < min_element:
        min_element = element
        min_element_index = index

my_list[max_element_index], my_list[min_element_index] = my_list[min_element_index], my_list[max_element_index]

print my_list
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
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

deleted_index = int(input("Enter k: "))

for index in range(deleted_index, len(my_list) - 1):
    my_list[index] = my_list[index + 1]

my_list.pop()

print my_list

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
my_list = []
length = int(input("Enter len: "))
for i in range(length):
    my_list.append(int(input()))

my_list.append(None)

inserting_index = int(input("Enter index k: "))
inserting_value = int(input("Enter value c: "))

for index in range(length - 1, inserting_index - 1, -1):
    my_list[index + 1] = my_list[index]

my_list[inserting_index] = inserting_value

print my_list
#--------------------------------------------------------------

#task13--------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

pair_counter = 0

for i in range(0, len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j]:
            pair_counter += 1

print "Pairs counted : {}".format(pair_counter)

#-----------------------------------------


#task14--------------------------
"""
Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
"""
def create_list():
    length = int(input("Enter length: "))
    return [int(input()) for _ in range(length)]

my_list = create_list()

for i in range(0, len(my_list)):
    already_found = False
    for j in range(0, len(my_list)):
        if my_list[i] == my_list[j] and i != j:
            already_found = True
    if not already_found:
        print my_list[i]


#-----------------------------------------


#task15---------------------------------------------------------
 '''
 N кеглей выставили в один ряд, занумеровав их слева направо
 числами от 1 до N. Затем по этому ряду бросили K шаров, при
 этом i-й шар сбил все кегли с номерами от li до ri включительно.
 Определите, какие кегли остались стоять на месте.
 Программа получает на вход количество кеглей N и количество
 бросков K. Далее идет K пар чисел li, ri, при этом 1? li? ri? N.

 Программа должна вывести последовательность из N символов,
 где j-й символ есть “I”, если j-я кегля осталась стоять, или
 “.”, если j-я кегля была сбита.
 '''
my_list = []
length = int(input("Enter count N: "))
for i in range(0, length):
    my_list.append(0)

balls = int(input("Enter K: "))
list_of_balls = []
for i in range(balls * 2):
    list_of_balls.append(int(input() - 1))

for j in range(0, len(list_of_balls), 2):
    start = list_of_balls[j]
    end = list_of_balls[j+1]
    for index in range(start, end + 1):
        my_list[index] += 1

for elem in my_list:
    if elem > 0:
        print "."
    else:
        print "I"



 #---------------------------------------------------------------


 #task16---------------------------------------------------------
 '''
 Известно, что на доске 8?8 можно расставить 8 ферзей так, чтобы
 они не били друг друга. Вам дана расстановка 8 ферзей на доске,
 определите, есть ли среди них пара бьющих друг друга.
 Программа получает на вход восемь пар чисел, каждое число от 1
 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга,
 выведите слово NO, иначе выведите YES.
 '''
my_list = []
length = 6
for i in range(length):
    my_list.append(int(input()))

ok = True

# First X
for i in range(0, length, 2):
    for j in range(i + 2, length, 2):
        if my_list[i] == my_list[j]:
            ok = False

# Second Y
for i in range(1, length, 2):
    for j in range(i + 2, length, 2):
        if my_list[i] == my_list[j]:
            ok = False

for i in range(0, length, 2):
    for j in range(i + 2, length, 2):
        if my_list[i] - my_list[j] == my_list[i + 1] - my_list[j + 1]:
            ok = False


if ok:
    print "NO"
else:
    print "YES"
 #--------------------------------------------------------------