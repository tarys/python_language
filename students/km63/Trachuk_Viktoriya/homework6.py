#task1--------------------------------------------
"""
Выведите все элементы списка с четными индексами
"""
s=input()
list=s.split( )
i=0
for element in list:
    print(list[i])
    i+=2 
#-------------------------------------------------
#task2--------------------------------------------
"""
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
"""
s=input()
list=s.split()
i = 0
for element in list:
    q = i % 2
    if q==0:
        print(element)
    i+=1
#-------------------------------------------------
#task3--------------------------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
s=input()
list=s.split( )
i=0
for element in list:
    if len(list)==1:
        list=[]
        print(list)
    elif list[i+1]>list[i]:
        print(list[i+1])
    i+=1
#-------------------------------------------------
#task4--------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
"""
def input_data():
    data = input().split()
    return data
    
def operation_data(elements):
    data = []
    for i in range(0, len(elements)):
            if i < len(elements)-1:
                if int(elements[i]) * int(elements[i + 1]) > 0:
                    data = [elements[i]]
                    data.append(elements[i + 1])
                    break
    return data

def print_data(output_data):
    for i in output_data:
        print (i, end=' ')
print_data(operation_data(input_data()))
#-------------------------------------------------
#task5--------------------------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
list_new=[]
s=input()
list=s.split( )
if len(list)==1:
    print(list_new)
i=1
for element in list:
    if i!=(len(list)-1):
        if (list[i]>list[i-1]) and (list[i]>list[i+1]):
            list_new.append(list[i])
        i+=1    
        
print(list_new)   
#-------------------------------------------------
#task6--------------------------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
"""
s=input()
list=s.split( )
i=0
g1=0
max=list[0]
for element in list:
    if i!=(len(list)-1):
        if list[i+1]>max:
            max=list[i+1]
            g1=i+1
        i+=1
    else: 
        if list[i]>max:
            max=list[i]
            g1=i
print(max)
print(g1)
#-------------------------------------------------
#task7--------------------------------------------
"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200. Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""
s=input()
list=s.split( )
x=input()
list_new=[]
i=0
j=0
for element in list:
    if list[i]==x:
        if i!=(len(list)-1):
            j=i+1
        else:
            j=len(list)
    else:
        while list[i]>x:
            if i!=(len(list)-1):
                i+=1
                j=i
            else:
                j=len(list)
print(j)
#-------------------------------------------------
#task8--------------------------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
"""
s=input()
list=s.split( )
i=0
j=len(list)
for element in list:
    if i!=(len(list)-1):
        if list[i]==list[i+1]:
            j-=1
        i+=1
print(j)
#-------------------------------------------------
#task9--------------------------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте.
"""
s=input()
list=s.split( )
i=0
if len(list)%2 == 1:
    for element in list:
        if i!=(len(list)-1):
            k=list[i]
            list[i]=list[i+1]
            list[i+1]=k
            i+=2
    print(list)
else:
    for element in list:
        if i!=(len(list)):
            k=list[i]
            list[i]=list[i+1]
            list[i+1]=k
            i+=2
    print(list)
#-------------------------------------------------
#task10--------------------------------------------
"""
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""
def input_data():
    data = input().split()
    return data

def operation_data(elements):
    max = elements[0]
    min = elements[0]
    ind_min = 0
    ind_max = 0
    for i in range(0, len(elements)):
        if  int(min) > int(elements[i]):
            min = elements[i]
            ind_min = i
        if  int(max) < int(elements[i]):
            max = elements[i]
            ind_max = i
    elements[ind_min], elements[ind_max] = elements[ind_max], elements[ind_min]    
    return elements

def print_data(output_data):
    for i in output_data:
        print (i, end=' ')

print_data(operation_data(input_data()))
#-------------------------------------------------
#task11--------------------------------------------
"""
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.
Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список. Также не следует использовать методpop(k) с параметром.
"""
s=input()
list=s.split( )
k=int(input())
len=len(list)
while k<len-1:
    list[k]=list[k+1]
    k+=1
list.pop()
print(list)
#-------------------------------------------------
#task12--------------------------------------------
"""
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.
Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
"""
def input_data():

    data = input().split()

    return data

def operation_data(elements):

    data = input().split()

    elements.append(data[1])

    for i in range(len(elements) - 1, int(data[0]), -1):

        elements[i] = elements[i - 1]

    elements[int(data[0])] = int(data[1])

    return elements

def print_data(output_data):
   for i in output_data:

        print (i, end=' ')
  
print_data(operation_data(input_data()))
#-------------------------------------------------
#task13--------------------------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""
s=input()
list=s.split( )
len=len(list)
amount=0
i=0
while i<len:
    j=0
    while j<i:
        if list[i]==list[j]:
            amount+=1
        j+=1
    i+=1
print(amount)
#-------------------------------------------------
#task14--------------------------------------------
"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
s=input()
list=s.split( )
len=len(list)
i=0
while i<len:
    j=0
    while j<len:
        if list[i]==list[j] and j!=i:
            break
        elif j==len-1:
            print(list[i])
        j+=1
    i+=1
#-------------------------------------------------
#task15--------------------------------------------
"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.
Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1? li? ri? N.
Программа должна вывести последовательность из N символов, где j-й символ есть “I”, если j-я кегля осталась стоять, или “.”, если j-я кегля была сбита.
"""
Def form_of_list(number):
	List=[]
	List=[‘I’ for I in range(number)]
	Return(list)
Number,count_of_shots=input().split()
List=form_of_list(int(number))
For I in range (int(count_of_shots)):
	Start_pos,final_pos=input().splint()
	For j in range(int(start_pos)-1, int(final_pos)):
		List_[j]=’.’
For element in list:
	Print(element, end=’ ‘)
#-------------------------------------------------
#task16--------------------------------------------
"""
Известно, что на доске 8?8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

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
 
 if diagonal_test(list_) == 1 and horizontal_vertical_test(list_) == 1:
	 print("NO")
 else:
     print("YES")
#-------------------------------------------------
