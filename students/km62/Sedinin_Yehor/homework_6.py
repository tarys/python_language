#task1------------------------------------------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter number to add it to array, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')

i = 0
while i < len(array):
	print(i, ' element of list is ', array[i])
	i += 2

#task2------------------------------------------------------------
"""
Выведите все четные элементы списка. 
При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter number to add it to array, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')

print('Even elements:')
for element in array:
	if int(element) % 2 == 0:
		print(element, end = ' ')


#task3------------------------------------------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter number to add it to array, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')
print('Elements, bigger then privious:')
i = 0
while i < len(array):
	if int(array[i]) > int(array[i - 1]):
		print(array[i], end = ' ')
	i += 1	


#task4------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. 
Если таких пар соседей несколько — выведите первую пару.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter number to add it to array, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')
print('Pair whith the same sign:')
i = 0
while i < len(array):
	if (int(array[i]) > 0 and  int(array[i - 1]) > 0) or (int(array[i]) < 0 and  int(array[i - 1]) < 0):
		print(array[i - 1], 'and', array[i])
		exit()	
	i += 1

#task5------------------------------------------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter number to add it to array, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')
print('Elements, bigger then neighboring:')
i = 1
while i < len(array) - 1:
	if int(array[i]) > int(array[i - 1]) + int(array[i + 1]):
		print(array[i], end = ' ')
	i += 1	

#task6------------------------------------------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. 
Если наибольших элементов несколько, выведите индекс первого из них.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter number to add it to array, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')

i = 0
max_element = 0
while i < len(array):
	if int(array[i]) > max_element:
		max_element = int(array[i])
	i += 1	
print('Max element = ', max_element)

#task7------------------------------------------------------------
"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. 
После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""

array = []
a = None
n = int(input('Enter number of students in group'))

for i in range(n):
	a = int(input('Enter height of student'))
	if int(a) > 200 or int(a) < 0:
		print('Invalid height, try again')
	else:	 
		array.append(a)

h = int(input('Enter Petya`s height'))
array.append(h)

print('-------------------------------------------------------')

array.sort()
print(array)
print(n  - array.index(h) + 1)

#task8------------------------------------------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем. 
Определите, сколько в нем различных элементов.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter number, which not less then previous, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')

i = 0
n = len(array)
while i < len(array) - 1:
	if array[i] == array[i + 1]:
		n -= 1
	i += 1			
			
print('Number of unique elements = ', n)

#task9------------------------------------------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). 
Если элементов нечетное число, то последний элемент остается на своем месте.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter element, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')

i = 0
print(array)
while i < len(array) - 1:
	array[i], array[i + 1] = array[i + 1], array[i]
	i += 2	
print(array)			

#task10------------------------------------------------------------
"""
В списке все элементы различны. 
Поменяйте местами минимальный и максимальный элемент этого списка.
"""

array = []
a = None
n = int(input('Enter number of elments'))

for i in range(n):
	a = int(input('Enter element'))
	array.append(a)

i_min = array.index(min(array))
i_max = array.index(max(array))

array[i_min], array[i_max] = array[i_max], array[i_min]

#task11------------------------------------------------------------
"""
Дан список из чисел и индекс элемента в списке k. 
Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. 
Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. 
Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter element, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')
print(array)

k = int(input('Enter removable element index'))

for i in range(k, len(array) - 1):
	array[i] = array[i + 1]

array.pop()

print(array)	

#task12------------------------------------------------------------
"""
Дан список целых чисел, число k и значение C. 
Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter element, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')
print(array)

c = input('Enter extra element')
k = int(input('Enter extra element index'))

array.append(None)
for i in range(len(array) - 1, k, -1):
	array[i] = array[i - 1]

array[k] = c

print(array)

#task13------------------------------------------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter element, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')
print(array)

for i in range(len(array) - 1):
	for j in range(len(array) - 1):
		if array[j] == array[i] and i != j:
			print('Elments number', i, ' and ', j, 'are the same (', array[i], ')' )

#task14------------------------------------------------------------
"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

array = []
a = None

while a != 'End' and a != 'end':
	a = input('Enter element, to end input enter ''End''\n') 
	array.append(a)

array.pop()
print('-------------------------------------------------------')
print(array)

for i in range(len(array)):
	for j in range(len(array)):
		if array[j] == array[i] and i != j:
			break	
	else:
		print('Element number ', i,'(', array[i], ') is unique')

#task15------------------------------------------------------------
"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. 
Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. 
Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""

n = int(input('Enter number of bowls'))
k = int(input('Enter number of throws'))

throws = []
downed = []
for i in range(k):
	print('Enter downed bowls by ', i + 1, '`st throw in format "Number1 Nuber2"')
	str = input()
	throw = [int(throw) for throw in str.split(' ')]
	if len(throw) != 2 or throw[0] < 0 or throw[1] < 0 or throw[0] > n or throw[1] > n:
		print('invalid')
		exit(0)
	throws.append(throw)

for element in throws:
	for i in range(element[0], element[1] + 1):
		downed.append(i)	

for i in range(n):
	if i + 1 in downed:
		print('.', end = ' ')
	else:
		print('I', end = ' ')

#task16------------------------------------------------------------
"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""

figures = []
res = False

for i in range(8):
	print('Enter coordinates for ', i, '`st figure in format "x y"')
	xy = input()
	coords = [int(coords) for coords in xy.split(' ')]
	if len(coords) != 2 or coords[0] < 0 or coords[1] < 0 or coords[0] > 8 or coords[1] > 8:
		print('invalid')
		exit(0)
	figures.append(coords)


def check(pair1, pair2):
	if pair1[0] == pair2[0] or pair1[1] == pair2[1]:
		print("Invalid values, try again")
	else:
		if (abs(pair2[0] - pair1[0]) == abs (pair2[1] - pair1[1])) or ((pair1[0] == pair2[0]) and (pair1[1] != pair2[1])) or ((pair1[1] == pair2[1]) and (pair1[0] != pair2[0])):
			return True
		else:
			return False

for i in range(7):
	if check(figures[i], figures[i + 1]):
		res = True
	else:
		res = False
		break

if res:
	print('YES')
else:
	print('NO')