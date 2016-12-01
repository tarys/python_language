﻿#task1------------------------------------------------------------

"""

Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).

"""

#

a=input("list")

for i in range(0,len(a),2):

	print(a[i],end=" ")

#-----------------------------------------------------------------

#task2------------------------------------------------------------

"""
Выведите все четные элементы списка.

"""

#

from random import randrange

n=int(input("n:"))

for element in [randrange(1,100) for i in range(n)]:

	if element%2==0:

		print(element)

#-----------------------------------------------------------------


#task3------------------------------------------------------------

"""

Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""

#

from random import randrange

n=int(input("n:"))

list=[randrange(1,100) for i in range(n)]

print(list)

for i in range(n-1):

	if (list[i]<list[i+1]):

		print(list[i+1],end=" ")

#-----------------------------------------------------------------

#task4------------------------------------------------------------

"""

Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.

"""

#

n=int(input("length:"))

a=[]

for i in range(n):
	
	x=int(input("element:"))

	a.append(x)
print(a)
for i in range((n-1)):

	if (a[i] > 0 and a[i+1] > 0) or (a[i] < 0 and a[i+1] < 0):

		print(a[i],a[i+1])

		break

#-----------------------------------------------------------------

#task5------------------------------------------------------------

"""

Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.

"""

#

n=int(input("length:"))

a=[]

for i in range(n):

	x=int(input("element:"))

	a.append(x)

print(a)

k=0

for i in range(1,n-1):

	if (a[i] > a[i-1]) and (a[i]>a[i+1]):

		k+=1

print(k)

#-----------------------------------------------------------------

#task6------------------------------------------------------------

"""

Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.

"""

#

n=int(input("length:"))

a=[]

for i in range(n):

  x=int(input("element:"))

  a.append(x)

print(a)

max=a[0]

for i in range(n):

  if max<a[i]:

    max=a[i]

print(max)

print(a.index(max))

#-----------------------------------------------------------------

#task7------------------------------------------------------------


"""


Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.


"""


#

n=int(input("length:"))

a=[]

for i in range(n):

	x=int(input("element:"))

	if x>200:

		print("no more than 200")

		break

	a.append(x)

petja=int(input("Petya:"))

a.sort()

a.reverse()

print(a)

for i in range(n):

	if a[n-1]>=petja:

		print(n+1)

		break

	elif a[i]<petja:

		print(i+1)

		break

#-----------------------------------------------------------------

#task8------------------------------------------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем.
 Определите, сколько в нем различных элементов.
"""
#
n=int(input("length:"))
a=[]
for i in range(n):
  x=int(input("element:"))
  a.append(x)
a.sort()
print(a)
counter=0
value=0
for element in a:
  if element!=value:
    value=element
    counter+=1
print(counter)
#-----------------------------------------------------------------

#task9------------------------------------------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
Если элементов нечетное число,
то последний элемент остается на своем месте.
"""
#
n=int(input("length:"))
a=[]
for i in range(n):
  x=int(input("element:"))
  a.append(x)
for i in range(1,n,2):
  b=str(a[i-1])
  b1=str(a[i])
  print(b,end=" ")
  print(b1,end="\n")
if n%2!=0:
  print(a[n-1])
#-----------------------------------------------------------------

#task10------------------------------------------------------------
"""
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""
#
n=int(input("length:"))
a=[]
for i in range(n):
  x=int(input("element:"))
  a.append(x)
ma=max(a)
mi=min(a)
mai=a.index(ma)
mii=a.index(mi)
a[mai]=mi
a[mii]=ma
print(a)
#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.
"""
#
k=int(input("number:"))
n=int(input("length:"))
a=[]
for i in range(n):
  x=int(input("element:"))
  a.append(x)
for i in range (k+1,n):
  a[i-1]=a[i]
a.pop()
print(a)
#-----------------------------------------------------------------

#task12------------------------------------------------------------
"""
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
"""
#
k=int(input("number:"))
c=input("element:")
n=int(input("length:"))
a=[]
for i in range(n):
  x=int(input("element:"))
  a.append(x)
a.insert(k,c)
print(a)
#-----------------------------------------------------------------

#task13------------------------------------------------------------
"""
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
"""
#
n=int(input("length:"))
a=[]
for i in range(n):
  x=int(input("element:"))
  a.append(x)
counter=0
a.sort()
for i in range(1,n):
  if a[i-1]==a[i]:
    counter+=1
print(counter)
#-----------------------------------------------------------------

#task14------------------------------------------------------------
"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
#
n=int(input("length:"))
a=[]
for i in range(n):
  x=int(input("element:"))
  a.append(x)
counter=0
for element in a:
  if a.count(element)==1:
    print(element)
#-----------------------------------------------------------------

