# task1------------------------------------------------------------
"""
Выведите все элементы списка с четными индексами
"""


# Program recursively prints elements with even_index
def even_index(numbers_list):
    if numbers_list == []:
        return
    print(numbers_list[0], end=' ')
    even_index(numbers_list[2::1])


numbers_list = input().split()
even_index(numbers_list)
# -----------------------------------------------------------------
# task2------------------------------------------------------------
"""
Выведите все четные элементы списка.
"""


# Program recursively prints even elements
def even_elements(numbers_list):
    if numbers_list == []:
        return
    if numbers_list[0] % 2 == 0:
        print(numbers_list[0], end=' ')
    even_elements(numbers_list[1::])


numbers_list = [int(i) for i in input().split()]
even_elements(numbers_list)

# -----------------------------------------------------------------
# task3------------------------------------------------------------
"""
Выведите все элементы списка, которые больше предыдущего элемента.
"""


# Program recursively prints elements bigger then previous
def bigger_then_previous(previous, numbers_list):
    if numbers_list == []:
        return
    if previous < numbers_list[0]:
        print(numbers_list[0], end=' ')
    bigger_then_previous(numbers_list[0], numbers_list[1::])


numbers_list = [int(i) for i in input().split()]
bigger_then_previous(numbers_list[0], numbers_list[1::])
# -----------------------------------------------------------------
# task4------------------------------------------------------------
"""
Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.
"""


# Program prints first pare of two elements with equal sign(x)
def sign_neiborhoods(neibor, numbers_list):
    if numbers_list == []:
        return
    elif numbers_list[0] * neibor >= 0:
        print(neibor, numbers_list[0])
        return
    sign_neiborhoods(numbers_list[0], numbers_list[1::])


numbers_list = [int(i) for i in input().split()]
sign_neiborhoods(numbers_list[0], numbers_list[1::])
# -----------------------------------------------------------------
# task5------------------------------------------------------------
"""
Определите, сколько в списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
"""


# Program prints amount of numbers bigger then neighbors
def bigger_neibor(amount, numbers_list):
    if len(numbers_list) < 3:
        return amount
    if numbers_list[0] < numbers_list[1] > numbers_list[2]:
        amount += 1
    return bigger_neibor(amount, numbers_list[1::])


numbers_list = [int(i) for i in input().split()]
amount = 0
print(bigger_neibor(amount, numbers_list))
# -----------------------------------------------------------------
# task6------------------------------------------------------------
"""
Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
"""


# Program prints max element, and its index
def max_index(max, numbers_list):
    if numbers_list == []:
        return max
    if max < numbers_list[0]:
        max = numbers_list[0]
    return max_index(max, numbers_list[1::])


numbers_list = [int(i) for i in input().split()]
max = max_index(numbers_list[0], numbers_list[1::])
print(max, numbers_list.index(max))
# -----------------------------------------------------------------
# task7------------------------------------------------------------
"""
Выведите номер, под которым Петя должен встать в строй.
Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""


# Program prints number in line
def number_in_line(numbers_list, index, height):
    if numbers_list == []:
        return index + 1
    if numbers_list[0] < height:
        return index + 1
    return number_in_line(numbers_list[1::], index + 1, height)


numbers_list = [int(i) for i in input().split()]
height = int(input())
print(number_in_line(numbers_list, 0, height))
# -----------------------------------------------------------------
# task8------------------------------------------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем.
Определите, сколько в нем различных элементов.
"""


# Program prints amount of different elements in list
def unique_amount(unique_list, list):
    if list == []:
        return len(unique_list)
    if list[0] not in unique_list:
        unique_list.append(list[0])
    return unique_amount(unique_list, list[1::])


list = input().split()
print(unique_amount([], list))
# -----------------------------------------------------------------
# task9------------------------------------------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
"""


# Program prints two neighbor elements swapped
def swap_neighbors(list):
    if len(list) == 1:
        print(list[0])
        return
    if list == []:
        return
    print(list[1], list[0], end=' ')
    swap_neighbors(list[2::])


list = input().split()
swap_neighbors(list)
# -----------------------------------------------------------------
# task10------------------------------------------------------------
"""
В списке все элементы различны.
Поменяйте местами минимальный и максимальный элемент этого списка.
"""


# Program prints min and max swapped
def swap_min_max(min, max, numbers_list):
    if numbers_list == []:
        return
    if numbers_list[0] == min:
        print(max, end=' ')
    elif numbers_list[0] == max:
        print(min, end=' ')
    else:
        print(numbers_list[0], end=' ')
    swap_min_max(min, max, numbers_list[1::])


numbers_list = [int(i) for i in input().split()]
max = max(numbers_list)
min = min(numbers_list)
swap_min_max(min, max, numbers_list)
# -----------------------------------------------------------------
# task11------------------------------------------------------------
"""
Дан список из чисел и индекс элемента в списке k.
Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
"""


# Program deletes element with index k
def list_shift(numbers_list, i):
    if len(numbers_list) - 1 == i:
        return numbers_list
    numbers_list[i] = numbers_list[i + 1]
    return list_shift(numbers_list, i + 1)


def list_print(numbers_list):
    if numbers_list == []:
        return
    print(numbers_list[0], end=' ')
    list_print(numbers_list[1::])


numbers_list = [int(i) for i in input().split()]
k = int(input())
numbers_list = numbers_list[:k:] + list_shift(numbers_list[k::], 0)
numbers_list.pop()
list_print(numbers_list)

# -----------------------------------------------------------------
# task12------------------------------------------------------------
"""
Дан список целых чисел, число k и значение C.
Вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
"""


# Program inputs element c in position k to list
def list_print(numbers_list):
    if numbers_list == []:
        return
    print(numbers_list[0], end=' ')
    list_print(numbers_list[1::])


def add_element(element, index, numbers_list):
    if index == len(numbers_list):
        numbers_list.append(element)
        return numbers_list
    numbers_list[index], temp = element, numbers_list[index]
    return add_element(temp, index + 1, numbers_list)


numbers_list = [int(i) for i in input().split()]
index, element = [int(i) for i in input().split()]
add_element(element, index, numbers_list)
list_print(numbers_list)
# -----------------------------------------------------------------
# task13------------------------------------------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
"""


# Prodgram prints amount of pares in list
def pares(list, pares_amount):
    if list == []:
        return pares_amount
    pares_amount += list.count(list[0]) - 1
    return pares(list[1::], pares_amount)


list = input().split()
print(pares(list, 0))

# -----------------------------------------------------------------
# task14------------------------------------------------------------
"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


# Program print element if it's unique
def unique_elements(list, index):
    if index == len(list):
        return
    if list.count(list[index]) == 1:
        print(list[index], end=' ')
    unique_elements(list, index + 1)


list = input().split()
unique_elements(list, 0)
# -----------------------------------------------------------------
# task15------------------------------------------------------------
"""
Программа получает на вход количество кеглей N и количество бросков K.
Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.
Программа должна вывести последовательность из N символов, где j-й символ есть “I”,
если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""


# Program  prints list of pins after strikes, there 'I' is if pin is standing, and '.' is if it's not
def list_print(list):
    if list == []:
        return
    print(list[0], end='')
    list_print(list[1::])


def strike(pin_list, l, r):
    if l > r:
        return pin_list
    pin_list[l - 1] = '.'
    pin_list[r - 1] = '.'
    return strike(pin_list, l + 1, r - 1)


pin_amount, strikes = [int(i) for i in input().split()]
pin_list = ['I' for i in range(pin_amount)]
for i in range(strikes):
    left_pin, right_pin = [int(i) for i in input().split()]
    pin_list = strike(pin_list, left_pin, right_pin)
list_print(pin_list)
# -----------------------------------------------------------------
# task16------------------------------------------------------------
"""
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей.
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""


# Program prints 'Yes' is 8 queens can't beet each other, and yes if they can
def is_hit(queen, queens_list):
    x_difference = int(queen[0]) - int(queens_list[0][0])
    y_difference = int(queen[1]) - int(queens_list[0][1])
    if abs(x_difference) == abs(y_difference):
        return True
    elif queen[0] == queens_list[0][0]:
        return True
    elif queen[1] == queens_list[0][1]:
        return True
    elif len(queens_list) == 1:
        return False
    return is_hit(queen, queens_list[1::])


def queens(queens_list):
    if len(queens_list) == 1:
        return False
    if is_hit(queens_list[0], queens_list[1::]) == True:
        return True
    return queens(queens_list[1::])


queens_list = [input().split() for i in range(8)]
write_locations = queens(queens_list)
if write_locations == True:
    print('YES')
else:
    print('NO')
# -----------------------------------------------------------------
