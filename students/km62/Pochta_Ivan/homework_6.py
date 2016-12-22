#task1------------------------------------------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""



input_str = input()
list_ = input_str.split(' ')
for i in range( len(list_) ):
    if i % 2 == 0:
        print(list_[i] , end = ' ')

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!

"""



list_ = input().split()
for element in list_:
    if int ( element ) % 2 == 0:
        print ( element , end=' ')

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

"""



list_= input(). split()
for i in range ( 1 , len(list_) ):
    if int(list_[i]) > int(list_[i-1]) :
        print ( list_[i] , end = ' ' )

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
"""



list_ = input().split()
for i in range ( 1, len( list_ ) ):
    if int( list_[i] ) * int( list_[i-1] ) > 0 :
        print( list_[i-1] , list_[i] )
        break

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""



count = 0
list_= input() . split ()
for i in range( 1 , len(list_)-1 ):
    if ( int(list_[i]) > int(list_[i-1]) ) and ( int(list_[i]) > int(list_[i+1]) ):
        count += 1
print(count)

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
"""



list_ = input() . split()
index = 0
max_ = int(list_[0])
for i in range( 1, len(list_) ):
    if int(list_[i]) > max_:
        max_ = int(list_[i])
        index = i
print( max_ , index)

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю.
После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""



def sorting(list_):
    for i in range(len(list_)-1):
        for j in range(i, len(list_)):
            if int(list_[i]) < int(list_[j]):
                var = int(list_[i])
                list_[i] = int(list_[j])
                list_[j] = var
    return list_
    
    
list_ = input().split() 
petrik_heigth = int(input())
list_.append(petrik_heigth)
sorting(list_)
for i in range(len(list_), 0 ,-1):
    if int(list_[i-1]) == petrik_heigth:
        print(i)
        break

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
"""



count = 0

list_ = input().split()
for i in range(len(list_)-1):
    if int(list_[i]) < int(list_[i+1]):
        count +=1
print(count+1)

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте.
"""



var=0
list_ = input().split()
for i in range(len(list_)//2):
    var = list_[i*2]
    list_[i*2] = list_[i*2+1]
    list_[i*2+1] = var
for element in list_:
    print(element, end = ' ')

#-----------------------------------------------------------------


#task10-----------------------------------------------------------
"""
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""



def max_( list_ ):
    max_element = int( list_[0] )
    for element in list_:
        if int( element ) > max_element:
            max_element =  int( element )
    return max_element
def min_( list_ ):
    min_element = int( list_[0] )
    for element in list_:
        if int( element ) < min_element:
            min_element =  int( element )
    return min_element
    

list_= input().split()
min_element = (min_(list_))
max_element = (max_(list_))
for i in range(len(list_)):
    if list_[i] == str(min_element):
        list_[i] = max_element
    elif list_[i] == str(max_element):
        list_[i] = min_element
for element in list_ :
    print( element , end = ' ' )

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Дан список из чисел и индекс элемента в списке k.
Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k.
Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.
"""



list_ = input().split()
number_of_element = int(input())
for i in range ( number_of_element, len(list_)-1):
    list_[ i ] = list_[ i + 1 ]
list_.pop()
for element in list_:
    print(element, end = ' ')

#-----------------------------------------------------------------


#task12-----------------------------------------------------------
"""
Дан список целых чисел, число k и значение C.
Необходимо вставить в список на позицию с индексом k элемент,
равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается,
после считывания списка в его конец нужно будет добавить новый элемент,
используя метод append.

Вставку необходимо осуществлять уже в считанном списке,
не делая этого при выводе и не создавая дополнительного списка.
"""



#This task can be realized more simply. I think that it's better=).
list_ = input().split()
index_of_new_element , new_element = input().split()

list_.insert(int(index_of_new_element), new_element)

for element in list_:
    print(element, end = ' ')

#-----------------------------------------------------------------


#task13-----------------------------------------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""



result = 0

list_ = input().split()
for i in range (len(list_)):#фиксируем элемент
    for j in range (i+1 , len(list_)):#перебираем все следующие элементу элементы в списке
        if list_[i] == list_[j]:#сравниваем их
            result += 1
print( result )

#-----------------------------------------------------------------


#task14-----------------------------------------------------------
"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""



counter = 0
list_of_lonely_elements=[]

list_ = input() . split()

for i in range(len(list_)):#фиксируем элемент
    counter = 0 # ставим значение счетчика по умолчанию
    for j in range(len(list_)): #перебираем элементы списка
        if (list_[i] == list_[j]) and i!=j: # если элемент равен другому и это не один и тот же элемент, то:
            counter = 1
    if counter == 0:
        list_of_lonely_elements.append(list_[i])


for element in list_of_lonely_elements:
    print(element, end = ' ')

#-----------------------------------------------------------------


#task15-----------------------------------------------------------
"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N.
Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно.
Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K.
Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N.

Программа должна вывести последовательность из N символов, где j-й символ есть “I”,
если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""



def form_of_list_(number): # Function which make a list
    list_ = []
    list_ = ['I' for i in range(number)]
    return(list_)


number, count_of_shots = input().split()

list_ = form_of_list_(int(number))

for i in range (int(count_of_shots)):
    start_pos, final_pos = input().split()
    for j in range( int(start_pos)-1 , int(final_pos) ):
        list_[j] = '.'

for element in list_:
    print(element, end = '')

#-----------------------------------------------------------------


#task16------------------------------------------------------------
"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей.
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""



def form_list_(size):#this function create a new 2-D list sizeXsize (this function created by me)
    list_ = (size * '0 ').split()
    for i in range(len(list_)):
        list_[i] = []
        list_[i] = (size * '0 ').split()
    return list_


def horizontal_vertical_test(list_):#this function make a test. If ion horizontal and vertical we have only 1 queen function retur 1, else 0.(created by me)
    for i in range(len(list_)):
        sum_of_horizontal = 0
        sum_of_vertical = 0
        for j in range(len(list_)):
            sum_of_horizontal += int(list_[i][j])
            sum_of_vertical += int(list_[j][i])
        if sum_of_horizontal > 1 or sum_of_vertical > 1:
            return 0
    return 1


def diagonal_test(list):#this function for horizontal test(created by Anton Pidgayniy)
    for i in range(len(list)):
        sum1, sum2, sum3, sum4 = 0, 0, 0, 0
        for j in range(len(list)):
            if -1 < j - i < len(list):
                sum1 += int(list[j - i][j])
                sum2 += int(list[j][j - i])
                sum3 += int(list[j - i][len(list) - j - 1])
                sum4 += int(list[len(list) - j - 1][j - i])
        if sum1 > 1 or sum2 > 1 or sum3 > 1 or sum4 > 1:
            return 0
    return 1


list_ = form_list_(8)

for i in range(8):# This is part of code where we read a coordinat's of Queen on the chess board(created by me)
    i, j = input().split()
    list_[int(i) - 1][int(j) - 1] = 1

if diagonal_test(list_) == 1 and horizontal_vertical_test(list_) == 1:#It's a part of code, where we print a result(create by Anton Pidgayniy)
    print("NO")
else:
    print("YES")

#-----------------------------------------------------------------




