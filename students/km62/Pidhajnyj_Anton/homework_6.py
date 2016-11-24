#task1------------------------------------------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
"""



def convert_string_to_list(string,sep=' '):
    list_of_numbers=[]
    j=0
    string+=sep
    for i in range(len(string)):
        if string[i]==sep:
            list_of_numbers.append(int(string[j:i]))
            j=i
    return list_of_numbers
def list_pair_indexs(list):
    list_save=list
    for i in range(len(list)):
        if i%2!=0:
            list_save[i]=''
    return list_save
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
        
print_list(list_pair_indexs(convert_string_to_list(input())))


#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!

"""



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
def list_of_pair_elements(list):
    list_return=[]
    for element in list:
        if element%2==0:
            list_return.append(element)
    return list_return

print_list(list_of_pair_elements(convert_string_to_list()))


#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

"""



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
def list_of_elements_bigger_pervious(list):
    list_return=[]
    for i in range(1,len(list)):
        if list[i]>list[i-1]:
            list_return.append(list[i])
    return list_return
    
print_list(list_of_elements_bigger_pervious(convert_string_to_list()))


#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
"""



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
def sign(x):
    if x<0:
        return -1
    elif x!=0:
        return 1
    else:
        return 0
def pair_with_similar_sign(list):
    list_return=[]
    for i in range(1,len(list)):
        if sign(list[i-1])==sign(list[i]):
            list_return.append(list[i-1])
            list_return.append(list[i])
            break
    return list_return

print_list(pair_with_similar_sign(convert_string_to_list()))


#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def list_of_elements_bigger_pervious_and_next(list):
    list_return=[]
    for i in range(1,len(list)-1):
        if (list[i]>list[i-1]) and (list[i]>list[i+1]):
            list_return.append(list[i])
    return list_return
    
print(len(list_of_elements_bigger_pervious_and_next(convert_string_to_list())))


#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
"""



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
def max_in_list(list):
    out=[]
    out.append(max(list))
    out.append(list.index(max(list)))
    return out
    
print_list(max_in_list(convert_string_to_list()))


#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю.
После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
"""



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
def put_number_in_sorted_list(num,list):
    out_list=list
    out_list.append(num)
    for i in range(len(out_list)-1,0,-1):
        if out_list[i]>out_list[i-1]:
            out_list[i],out_list[i-1]=out_list[i-1],out_list[i]
        else:
            break
    return out_list
def index_last(element,list):
    out_list=list
    out_list.reverse()
    return len(out_list)-out_list.index(element)-1
        
li=convert_string_to_list()
n=int(input())
li=put_number_in_sorted_list(n,li)
print(index_last(n,li)+1)


#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
"""



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def types_of_element_sorted_list(list):
    count=1
    for i in range(1,len(list)):
        if list[i]!=list[i-1]:
            count+=1
    return count

print(types_of_element_sorted_list(convert_string_to_list()))


#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте.
"""



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
def replace_elements(index1,index2,list):
    out_list=list
    out_list[index1],out_list[index2]=out_list[index2],out_list[index1]
    return out_list

li=convert_string_to_list()
for i in range(0,len(li)-1,2):
    li=replace_elements(i,i+1,li)
print_list(li)


#-----------------------------------------------------------------


#task10-----------------------------------------------------------
"""
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
"""



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
def max_in_list(list):
    out=[]
    out.append(max(list))
    out.append(list.index(max(list)))
    return out
def min_in_list(list):
    out=[]
    out.append(min(list))
    out.append(list.index(min(list)))
    return out
def replace_elements(index1,index2,list):
    out_list=list
    out_list[index1],out_list[index2]=out_list[index2],out_list[index1]
    return out_list

li=convert_string_to_list()    
print_list(replace_elements(max_in_list(li)[1],min_in_list(li)[1],li))


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



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
def delete_element(List,index):
    for i in range(index,len(List)-1):
        List[i],List[i+1]=List[i+1],List[i]
    List.pop()
    

li=convert_string_to_list()
k=int(input())
delete_element(li,k)
print_list(li)

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



def convert_string_to_list(sep=' '):
    out_list=[int(s) for s in input().split(sep)]
    return out_list
def print_list(list,sep=' '):
    for element in list:
        print(element,end=sep)
def paste_element(index,element,List):
    List.append(element)
    for i in range(len(List)-1,index,-1):
        List[i],List[i-1]=List[i-1],List[i]

li=convert_string_to_list()       
k_c=convert_string_to_list()
k=k_c[0]
c=k_c[1]
paste_element(k,c,li)
print_list(li)


#-----------------------------------------------------------------


#task13-----------------------------------------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""



result = 0

list_ = input().split()
for i in range (len(list_)):#фиксируем елемент
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



def form_list_(size):#this function create a new 2-D list sizeXsize (this function created by Pochta Ivan)
    list_ = (size * '0 ').split()
    for i in range(len(list_)):
        list_[i] = []
        list_[i] = (size * '0 ').split()
    return list_


def horizontal_vertical_test(list_):#this function make a test. If ion horizontal and vertical we have only 1 queen function retur 1, else 0.(created by Pochta Ivan)
    for i in range(len(list_)):
        sum_of_horizontal = 0
        sum_of_vertical = 0
        for j in range(len(list_)):
            sum_of_horizontal += int(list_[i][j])
            sum_of_vertical += int(list_[j][i])
        if sum_of_horizontal > 1 or sum_of_vertical > 1:
            return 0
    return 1


def diagonal_test(list):#this function for diagonal test(created by Anton Pidgayniy)
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

for i in range(8):# This is part of code where we read a coordinat's of Queen on the chess board(created by Pochta Ivan)
    i, j = input().split()
    list_[int(i) - 1][int(j) - 1] = 1

if diagonal_test(list_) == 1 and horizontal_vertical_test(list_) == 1:#It's a part of code, where we print a result(create by Anton Pidgayniy)
    print("NO")
else:
    print("YES")

#-----------------------------------------------------------------




