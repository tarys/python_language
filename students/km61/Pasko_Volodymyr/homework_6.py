# task 1 ----------------------------------------------------------
'''
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
'''
# program printing the elements with the even index in the list
list = [int(i) for i in input('Enter the element: ').split()]


def rec_even_elements(list):
    # recursion end
    if len(list) == 0:
        return
    # body
    print(list[0])
    # recursion
    rec_even_elements(list[2::])


rec_even_elements(list)
# ----------------------------------------------------------------------------------
# task 2 ----------------------------------------------------------
'''
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
'''
# program printing the even elements from the list
new_list = [int(i) for i in input('Enter the element: ').split()]


def even_elements_recursion(list):
    # rec. stop
    if len(list) == 0:
        return
    # body
    if list[0] % 2 == 0:
        print(list[0])
    # recursion
    even_elements_recursion(list[1::])


even_elements_recursion(new_list)
# ----------------------------------------------------------------------------------
# task 3 ----------------------------------------------------------
'''
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
'''
# program printing the elements which are bigger then the previous one
list = [int(i) for i in input('Enter the element: ').split()]


def bigger_than_previous_recursion(list):
    # rec.stop
    if len(list) == 1:
        return
        # body
    if list[1] > list[0]:
        print(list[1])
    # recursion
    bigger_than_previous_recursion(list[1::])


bigger_than_previous_recursion(list)
# ----------------------------------------------------------------------------------
# task 4 ----------------------------------------------------------
'''
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько —
выведите первую пару.
'''
# program printing the elements in the list with the same sign

input_list = [int(i) for i in input('Enter the element: ').split()]


def same_sign_recursion(input_list):
    # rec.stop
    if len(input_list) == 1:
        return
    # body
    if input_list[0] * input_list[1] > 0:
        print(input_list[0], input_list[1])
    # recursion
    same_sign_recursion(input_list[1::])


same_sign_recursion(input_list)
# ----------------------------------------------------------------------------------
# task 5 ----------------------------------------------------------
'''
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество
таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
'''
# program printing the elements which are bigger than neighbour elements
new_list = [int(i) for i in input('Enter the element: ').split()]


def bigger_than_neighbours_recursion(list):
    # rec. stop
    if len(list) == 2:
        return
    # body
    if list[1] > list[0] and list[1] > list[2]:
        print(list[1])
    # recursion
    bigger_than_neighbours_recursion(list[1::])


bigger_than_neighbours_recursion(new_list)
# ----------------------------------------------------------------------------------
# task 6 ----------------------------------------------------------
'''
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
'''
# program printing the maximum element and it's index from the list
new_list = [int(i) for i in input('Enter the element: ').split()]
counter = 0
max_counter = 0


def max_element_recursion(list, i, max_counter):
    if i == len(list):
        return max_counter
    if list[i] > list[max_counter]:
        return max_element_recursion(list, i + 1, i)
    else:
        return max_element_recursion(list, i + 1, max_counter)


index = max_element_recursion(new_list, counter, max_counter)
print(new_list[index], index)
# ----------------------------------------------------------------------------------
# task 7 ----------------------------------------------------------
'''
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это
сделать. Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого
человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у
Пети, то он должен встать после них.
'''
# program printing the Peter's place in the que according to his height
new_list = [int(i) for i in input('Enter the height of class: ').split()]
peters_place = 0
que_place = 0
peters_height = int(input('Enter Peter\'s height: '))


def peters_height_recursion(list, height, place, need_to_stay_place):
    # rec.stop
    if height >= list[0]:
        return print(1)
    if need_to_stay_place > 0:
        return print(need_to_stay_place + 1)
    # body and recursion
    if height > list[place]:
        peters_height_recursion(list, height, place, place)
    else:
        peters_height_recursion(list, height, place + 1, need_to_stay_place)


peters_height_recursion(new_list, peters_height, que_place, peters_place)
# ----------------------------------------------------------------------------------
# task 8 ----------------------------------------------------------
'''
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
'''

# program printing the quantity of different elements
new_list = [int(i) for i in input('Enter the elements: ').split()]
different_element_counter = 1
elements = 0
previous_element = new_list[0]


def different_elem_recursion(list, element, previous_element, different_elements):
    # rec. stop
    if element == len(list):
        return print(different_elements)
    # body and recursion
    if list[element] != previous_element:
        different_elem_recursion(list, element + 1, list[element], different_elements + 1)
    else:
        different_elem_recursion(list, element + 1, list[element], different_elements)


different_elem_recursion(new_list, elements, previous_element, different_element_counter)
# ----------------------------------------------------------------------------------
# task 9 ----------------------------------------------------------
'''
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то
последний элемент остается на своем месте.
'''
# program swapping the neighbour elements in the sequence
new_list = [int(i) for i in input('Enter the elements: ').split()]
element = 0
next_element = 1


def swap_elem_recursion(list, element, next_element):
    # rec. stop
    if next_element > len(list) - 1:
        return print(list)
    # body and recursion
    list[element], list[next_element] = list[next_element], list[element]
    swap_elem_recursion(list, element + 2, next_element + 2)


swap_elem_recursion(new_list, element, next_element)
# ----------------------------------------------------------------------------------
# task 10 ----------------------------------------------------------
'''
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
'''
# program swapping the minimum and maximum element in the list
new_list = [int(i) for i in input('Enter the elements: ').split()]
max_index = 0
min_index = 0
i = 0


def find_min_index_recursion(list, i, min_index):
    # rec. stop
    if i == len(list):
        return min_index
    # body and recursion
    if list[min_index] > list[i]:
        return find_min_index_recursion(list, i + 1, i)
    else:
        return find_min_index_recursion(list, i + 1, min_index)


def find_max_index_recursion(list, i, max_index):
    # rec. stop
    if i == len(list):
        return max_index
    # body and recursion
    if list[max_index] < list[i]:
        return find_max_index_recursion(list, i + 1, i)
    else:
        return find_max_index_recursion(list, i + 1, max_index)


new_max_index = find_max_index_recursion(new_list, i, max_index)
new_min_index = find_min_index_recursion(new_list, i, min_index)
new_list[new_min_index], new_list[new_max_index] = new_list[new_max_index], new_list[new_min_index]
print(new_list)
# ----------------------------------------------------------------------------------
# task 11 ----------------------------------------------------------
'''
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы,
стоящие правее элемента с индексом k. Программа получает на вход список, затем число k. Программа сдвигает все элементы,
а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.
'''

# program deleting the index in the list and moving the element
new_list = [int(i) for i in input('Enter the elements: ').split()]
remove_index = int(input('Enter the index of the element to remove: '))


def remove_index_recursion(list, i):
    if i >= len(list):
        list.pop()
        return print(list)
    list[i], list[i - 1] = list[i - 1], list[i]
    remove_index_recursion(list, i + 1)


remove_index_recursion(new_list, remove_index + 1)
# ----------------------------------------------------------------------------------
# task 12 ----------------------------------------------------------
'''
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C,
сдвинув все элементы, имевшие индекс не менее k, вправо. Посколько при этом количество элементов в списке увеличивается,
 после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
'''
# program adding the element according to its index
new_list = [int(i) for i in input("Enter the element: ").split()]
index_paste_element = int(input('Enter the index of the element to paste: '))
element_to_paste = int(input('Enter the element to paste: '))
i = len(new_list) - 1


def add_element_recursion(list, add_element, index_add_element, i):
    if i == len(list) - 1:
        list.append(add_element)
        i += 1
    # rec. stop
    if i == index_add_element:
        return print(list)
    # body
    list[i], list[i - 1] = list[i - 1], list[i]
    return add_element_recursion(list, add_element, index_add_element, i - 1)


add_element_recursion(new_list, element_to_paste, index_paste_element, i)
# ----------------------------------------------------------------------------------
# task 13 ----------------------------------------------------------
'''
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные
друг другу образуют одну пару, которую необходимо посчитать.
'''
# program counting the similar pairs in the list
new_list = [int(i) for i in input('Enter the element: ').split()]
element_i = 0
i = 0
same_element_counter = 0


def count_pair_recursion(list, i, element_checker, same_elements):
    # rec. stop
    if i == len(list) - 1:
        return print(same_elements)
    # body and recursion
    if element_checker >= len(list) - 1:
        element_checker = i + 1
        return count_pair_recursion(list, i + 1, element_checker, same_elements)
    if list[i] == list[element_checker + 1]:
        return count_pair_recursion(list, i, element_checker + 1, same_elements + 1)
    else:
        return count_pair_recursion(list, i, element_checker + 1, same_elements)


count_pair_recursion(new_list, i, element_i, same_element_counter)
# ----------------------------------------------------------------------------------
# task 14 ----------------------------------------------------------
'''
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том
порядке, в котором они встречаются в списке.
'''

# program printing the non repeated elements in the list
new_list = [int(i) for i in input('Enter the element: ').split()]
i = 0


def unique_elem_recursion(list, i):
    # rec. stop
    if i == len(list):
        return
    # body
    if list.count(list[i]) == 1:
        print(list[i])
        unique_elem_recursion(list, i + 1)
    else:
        return unique_elem_recursion(list, i + 1)


unique_elem_recursion(new_list, i)
# ----------------------------------------------------------------------------------
# task 15 ----------------------------------------------------------
'''
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров,
при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом
1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять,
или “.”, если j-я кегля была сбита.
'''
# ----------------------------------------------------------------------------------
# task 16 ----------------------------------------------------------
'''
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
'''
# ----------------------------------------------------------------------------------
