# task1------------------------------------------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""


# четные индексы
def list_def(n):
    if n >= len(list_numbers):
        return
    print(list_numbers[n])
    list_def(n + 2)


list_numbers = input().split()
list_def(0)

# -----------------------------------------------------------------


# task2------------------------------------------------------------
"""
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""


# четные элементы
def list_def(n):
    if n == len(list_numbers):
        return
    if list_numbers[n] % 2 == 0:
        print(list_numbers[n])
    list_def(n + 1)


list_numbers = [int(element) for element in input().split()]
list_def(0)
# -----------------------------------------------------------------


# task3------------------------------------------------------------
"""
	Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""

'''
 Больше предыдущего
'''


def list_def(n):
    if n == len(list_numbers):
        return
    if int(list_numbers[n]) > int(list_numbers[n - 1]):
        print(list_numbers[n])
    list_def(n + 1)


list_numbers = input().split()
list_def(1)
# -----------------------------------------------------------------


# task4------------------------------------------------------------
'''
	Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
'''


# Соседи одного знака
def list_def(n):
    if n == len(list_numbers):
        return
    if (int(list_numbers[n]) < 0 and int(list_numbers[n - 1]) < 0) or (
            int(list_numbers[n]) > 0 and int(list_numbers[n - 1]) > 0):
        print(list_numbers[n - 1], list_numbers[n])
        return
    list_def(n + 1)


list_numbers = input().split()
list_def(1)
# -----------------------------------------------------------------


# task5------------------------------------------------------------
'''
	Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
'''


# Больше своих соседей
def list_def(n, count):
    if n == len(list_numbers) - 1:
        return count
    if int(list_numbers[n]) > int(list_numbers[n - 1]) and int(list_numbers[n]) > int(list_numbers[n + 1]):
        count += 1
    count = list_def(n + 1, count)
    return count


list_numbers = input().split()
count = 0
if len(list_numbers) > 1:
    print(list_def(1, count))
else:
    print(0)
# -----------------------------------------------------------------



# task6------------------------------------------------------------
'''
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
'''


# Наибольший элемент
def maximum(max_index, i):
    if i == len(list_numbers):
        return max_index
    if list_numbers[max_index] < list_numbers[i]:
        return maximum(i, i + 1)
    else:
        return maximum(max_index, i + 1)


list_numbers = [int(i) for i in input().split()]
index = maximum(0, 0)
print(list_numbers[index], index)
# -----------------------------------------------------------------



# task7------------------------------------------------------------
'''
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
'''


# Шеренга
def sherenga(i, counter):
    if i == len(list_numbers):
        return counter
    if height_Petia > int(list_numbers[i]):
        return counter
    return sherenga(i + 1, counter + 1)


list_numbers = input().split()
height_Petia = int(input())
print(sherenga(0, 1))
# -----------------------------------------------------------------


# task8------------------------------------------------------------
'''
	Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
'''


# Количество различных элементов
def others(i, counter):
    if i == len(list_numbers):
        return counter
    if list_numbers[i] != list_numbers[i - 1]:
        return others(i + 1, counter + 1)
    return others(i + 1, counter)


list_numbers = input().split()
print(others(1, 1))
# -----------------------------------------------------------------


# task9------------------------------------------------------------
'''
	Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте.
'''


# Переставить соседние
def change(list_numbers):
    if len(list_numbers) < 2:
        print(' '.join(list_numbers))
        return
    list_numbers[0], list_numbers[1] = list_numbers[1], list_numbers[0]
    print(' '.join(list_numbers[:2:]), end=' ')
    change(list_numbers[2::])


list_numbers = input().split()
change(list_numbers)

# -----------------------------------------------------------------


# task10------------------------------------------------------------
'''
	 В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
'''


# Переставить min и max
def change(max_index, min_index, i):
    if i == len(list_numbers):
        list_numbers[max_index], list_numbers[min_index] = list_numbers[min_index], list_numbers[max_index]
        return
    if list_numbers[max_index] < list_numbers[i]:
        return change(i, min_index, i + 1)
    if list_numbers[min_index] > list_numbers[i]:
        return change(max_index, i, i + 1)
    return change(max_index, min_index, i + 1)


list_numbers = [int(s) for s in input().split()]
change(0, 0, 0)
print(' '.join([str(i) for i in list_numbers]))
# -----------------------------------------------------------------


# task11------------------------------------------------------------
'''
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.
'''


# Удалить элемент
def delet(index, i):
    if i == len(list_numbers):
        list_numbers.pop()
        return list_numbers
    list_numbers[index], list_numbers[i] = list_numbers[i], list_numbers[index]
    return delet(index + 1, i + 1)


list_numbers = input().split()
index = int(input())
print(' '.join(delet(index, index + 1)))
# -----------------------------------------------------------------


# task12------------------------------------------------------------
'''
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
'''


# Вставить элемент
def append(i, index, need_index):
    if i == int(need_index) - 1:
        return list_numbers
    list_numbers[i], list_numbers[index] = list_numbers[index], list_numbers[i]
    return append(i - 1, index - 1, need_index)


list_numbers = input().split()
index_number = input().split()
list_numbers.append(index_number[1])
print(' '.join(append(len(list_numbers) - 2, len(list_numbers) - 1, index_number[0])))

# -----------------------------------------------------------------

# task13------------------------------------------------------------
"""
	Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""


# Количество совпадающих пар
def double(index, i, pairs):
    if index == len(list_numbers):
        return pairs
    if i == len(list_numbers):
        return double(index + 1, index + 2, pairs)
    if list_numbers[i] == list_numbers[index]:
        return double(index, i + 1, pairs + 1)
    return double(index, i + 1, pairs)


list_numbers = input().split()
print(double(0, 1, 0))
# -----------------------------------------------------------------


# task14------------------------------------------------------------
"""
	Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


# Уникальные элементы
def all_numbers(i, index):
    if i == len(list_numbers):
        return 1
    if list_numbers[index] == list_numbers[i] and index != i:
        return
    return all_numbers(i + 1, index)


def unique(index, count):
    if index == len(list_numbers):
        return
    if all_numbers(0, index) == 1:
        print(list_numbers[index], end=' ')
        return unique(index + 1, count + 1)
    else:
        return unique(index + 1, count)


list_numbers = input().split()
unique(0, 0)
# -----------------------------------------------------------------


# task15------------------------------------------------------------
"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""


def change(index, index_2):
    if index > index_2:
        return
    res[index] = '.'
    change(index + 1, index_2)


def game(i):
    if i == int(N_and_K[1]):
        return
    n = [int(element) - 1 for element in input().split()]
    change(n[0], n[1])
    game(i + 1)


N_and_K = input().split()
res = ['I'] * int(N_and_K[0])
game(0)
print(''.join(res))
# -----------------------------------------------------------------

# task16------------------------------------------------------------
"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""


# Ферзи
def create(i):
    if i == 8:
        return
    x_y = []
    x_y = [int(i) for i in input().split()]
    list_numbers.append(x_y)
    create(i + 1)


list_numbers = []
create(0)


def yes_no(index, i):
    x1_y1 = list_numbers[index]
    x2_y2 = list_numbers[i]
    if (x1_y1[0] + x1_y1[1] == x2_y2[0] + x2_y2[1]) or (x1_y1[0] - x1_y1[1] == x2_y2[0] - x2_y2[1]):
        return 'YES'
    if (x1_y1[0] == x2_y2[0] and x1_y1[1] != x2_y2[1]) or (x1_y1[1] == x2_y2[1] and x1_y1[0] != x2_y2[0]):
        return 'YES'
    if i == 7 and index == 6:
        return 'NO'
    if i == 7:
        return yes_no(index + 1, index + 2)
    return yes_no(index, i + 1)


print(yes_no(0, 1))