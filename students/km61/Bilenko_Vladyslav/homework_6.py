#task1
"""
Условие
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""
#Четные индексы#
list = [int(i) for i in input().split()]

def rec_elements (list):
    if len(list) == 0:
        return
    print(list[0])
    rec_elements(list[2::])
rec_elements(list)

#task2
"""
Условие
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""
#Четные элементы#
list = [int(i) for i in input().split()]
def rec_elements (list):
    if len(list) == 0:
        return
    if list[0]%2 == 0:
        print(list[0])
    rec_elements(list[1::])
rec_elements(list)

#task3
"""
Условие
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
#Больше предыдущего#
list = [int(i) for i in input().split()]
def bigger_elements (list):
    if len(list) == 1:
        return
    if list[0]<list[1]:
        print(list[1])
    bigger_elements(list[1::])
bigger_elements (list)

#task4
"""
Условие
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
"""
#Соседи одного знака#
list = [int(i) for i in input().split()]
def same_sign (list):
    if len(list) == 1:
        return
    if list[0] * list[1]>0:
        print(list[0], list[1])
        return
    same_sign(list[1::])
same_sign(list)

#task5
"""
Условие
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
#Больше своих соседей#
def neighbour (amount, list):
    if len(list) < 3:
        return amount
    if list[0] < list[1] > list[2]:
        amount += 1
    return neighbour (amount, list[1::])
list = [int(i) for i in input().split()]
amount = 0
print(neighbour(amount, list))

#task6
"""
Условие
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько,
выведите индекс первого из них.
"""
#Наибольший элемент#
list = [int(i) for i in input().split()]    
counter = 0
max = 0
def max_element_index (list, i, max):
    if i == len(list):
        return max
    if list[i] > list[max]:
        return max_element_index(list, i+1, i)
    else:
        return max_element_index(list, i+1, max)
index = max_element_index(list, max, counter)
print(list[index], index)

#task7
"""
Условие
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. 
После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""
#Шеренга#
def row (i, count):
    if i == len(list):
        return count
    if peters_height > int(list[i]):
        return count
    return row (i+1, count+1)
list = [int(i) for i in input().split()]
peters_height = int(input())
print(row(0,1))

#task8
"""
Условие
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
"""
#Количество различных элементов#
def new_list (i, count):
    if i == len(list):
        return count
    if list[i]!=list[i-1]:
        return new_list (i+1, count+1)
    return new_list (i+1, count)
list = [int(i) for i in input().split()]
print(new_list(1,1))

#task9
"""
Условие
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент 
остается на своем месте.
"""
#Переставить соседние#
def change(list): 
    if len(list)<2: 
        print(' '.join(list)) 
        return 
    list[0],list[1]=list[1],list[0] 
    print(' '.join(list[:2:]),end=' ') 
    change(list[2::]) 
list = input().split()
change(list)

#task10
"""
Условие
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""
#Переставить min и max#
def change_min_and_max (max, min, i):
    if i == len(list):
        list[max],list[min]=list[min],list[max]
        return
    if list[max]<list[i]:
        return change_min_and_max(i, min, i+1)
    if list[min]>list[i]:
        return change_min_and_max(max, i, i+1)
    return change_min_and_max(max, min, i+1)
list = [int(s) for s in input().split()]
change_min_and_max(0,0,0)
print(' '.join([str(i) for i in list]))

#task11
"""
Условие
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, 
стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент 
списка при помощи метода pop() без параметров.
"""
#Удалить элемент#
def delete (index, i):
    if i == len(list):
        list.pop()
        return list
    list[index],list[i]=list[i],list[index]
    return delete(index+1, i+1)
list = input().split()
index = int(input())
print(' '.join(delete(index, index+1)))

#task12
"""
Условие
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, 
сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить 
новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
"""
#Вставить элемент#
def add_element(i,index,need_index):
    if i==int(need_index)-1:
        return list
    list[i],list[index]=list[index],list[i]
    return add_element(i-1,index-1,need_index)
list=input().split()
index_number=input().split()
list.append(index_number[1])
print(' '.join( add_element(len(list)-2,len(list)-1,index_number[0]) ))

#task13
"""
Условие
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, 
равные друг другу образуют одну пару, которую необходимо посчитать.
"""
#Количество совпадающих пар#
def pares(list, pares_count):
    if list == []:
        return pares_count
    pares_count += list.count(list[0]) - 1
    return pares(list[1::], pares_count)
list = input().split()
print(pares(list, 0))

#task14
"""
Условие
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, 
в котором они встречаются в списке.
"""
#Уникальные элементы#
def unique_elements(list, index):
    if index == len(list):
        return
    if list.count(list[index]) == 1:
        print(list[index], end=' ')
    unique_elements(list, index + 1)
list = input().split()
unique_elements(list, 0)