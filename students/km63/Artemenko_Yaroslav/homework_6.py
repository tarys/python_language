#task1---------------------------------------------------


"""
Задача «Четные индексы»
Условие
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    for i in range(0,len(elem),2):

        data.append(elem[i])

    return data

def print_data(output_data):

    for i in output_data:

        print (i, end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task2------------------------------------------------------


"""
Задача «Четные элементы»
Условие
Выведите все четные элементы списка.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    for i in elem:

        if int(i)%2==0:

            data.append(i)

    return data

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task3------------------------------------------------------


"""
Задача «Больше предыдущего»
Условие
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    for i in range(0,len(elem)):

        if i<len(elem)-1:

            if int(elem[i])<int(elem[i+1]):

                data.append(elem[i+1])

    return data

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task4------------------------------------------------------


"""
Задача «Соседи одного знака»
Условие
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    for i in range (0,len(elem)):

        if len(data)==0:

            if i<len(elem)-1:

                if int(elem[i])*int(elem[i+1])>0:

                    data=[elem[i]]

                    data.append(elem[i+1])

    return data

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task5------------------------------------------------------


"""
Задача «Больше своих соседей»
Условие
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
#
def input_data():
    data=input().split()
    return data
def operation_data(elem):
    count=0
    for i in range(1,len(elem)-1):
        if int(elem[i-1])<int(elem[i])>int(elem[i+1]):
            count+=1
    return count
def print_data(output_data):
    print(output_data)
print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task6------------------------------------------------------


"""
Задача «Наибольший элемент»
Условие
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. 
Если наибольших элементов несколько, выведите индекс первого из них.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=[]

    max_elem=elem[0]

    data=[max_elem]

    data.append(0)

    for i in range(1,len(elem)):

        if int(max_elem)<int(elem[i]):

            max_elem=elem[i]

            data=[max_elem]

            data.append(i)

    return data

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))

#-----------------------------------------------------------


#task7------------------------------------------------------


"""
Задача «Шеренга»
Условие
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    height=int(input())

    position=0

    while position<len(elem) and int(elem[position])>=height:

        position+=1

    return position

def print_data(output_data):

    print (output_data+1)

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task8------------------------------------------------------


"""
Задача «Количество различных элементов»
Условие
Дан список, упорядоченный по неубыванию элементов в нем.
Определите, сколько в нем различных элементов.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    count=0

    for i in range (0,len(elem)-1):

        if int(elem[i])!=int(elem[i+1]):

            count+=1

    return(count)

def print_data(output_data):

    print (output_data+1)

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task9------------------------------------------------------


"""
Задача «Переставить соседние»
Условие
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    for i in range(0,len(elem)//2):

        elem[i*2],elem[i*2+1]=elem[i*2+1],elem[i*2]

    return elem

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task10------------------------------------------------------


"""
Задача «Переставить min и max»
Условие
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    max_elem=elem[0]

    min_elem=elem[0]

    index_max=0

    index_min=0

    for i in range(0,len(elem)):

        if int(min_elem)>int(elem[i]):

            min_elem=elem[i]

            index_min=i

        if int(max_elem)<int(elem[i]):

            max_elem=elem[i]

            index_max=i

    elem[index_min],elem[index_max]=elem[index_max],elem[index_min]

    return elem

def print_data(output_data):

    for i in output_data:

        print (i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task11------------------------------------------------------


"""
Задача «Удалить элемент»
Условие
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    k=int(input())

    for i in range(k,len(elem)-1):

        elem[i]=elem[i+1]

    elem.pop()

    return elem

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task12------------------------------------------------------


"""
Задача «Вставить элемент»
Условие
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
"""
#
def input_data():

    data=input().split()

    return data

def operation_data(elem):

    data=input().split()

    elem.append(data[1])

    for i in range(len(elem)-1,int(data[0]),-1):

        elem[i]=elem[i-1]

    elem[int(data[0])]=int(data[1])

    return elem

def print_data(output_data):

    for i in output_data:

        print(i,end=" ")

print_data(operation_data(input_data()))

#-----------------------------------------------------------


#task13------------------------------------------------------


"""
Задача «Количество совпадающих пар»
Условие
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""
#
def input_data(): 
    data = input().split() 
    return data 
def operation_data(elem): 
    count=0 
    for i in elem: 
        for j in elem: 
            if i==j: 
                count+=1 
        count-=1 
    return(count // 2) 
def print_data(output_data): 
    print(output_data) 
print_data(operation_data(input_data()))
#-----------------------------------------------------------


#task14------------------------------------------------------


"""
Задача «Уникальные элементы»
Условие
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
#

#-----------------------------------------------------------


#task15------------------------------------------------------


"""
Задача «Кегельбан»
Условие
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1? li? ri? N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""
#

#-----------------------------------------------------------


#task16------------------------------------------------------


"""
Задача «Ферзи»
Условие
Известно, что на доске 8?8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""
#

#-----------------------------------------------------------



