#task1------------------------------------------------------------
"""
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...). 
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    even_element=[]
    longe = len (element)
    for i in range(0, longe+1, 2):
        even_element.append(element[i])
    return even_element
    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements())) 
#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы! 
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    even_element=[]
    longe = len (element)
    for i in range(0, longe):
        if int(element[i])%2==0:
            even_element.append(element[i])
    return even_element
    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements())) 
#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента. 
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    even_element=[]
    longe = len (element)
    for i in range(0, longe-1):
        if int(element[i])<int(element[i+1]):
            even_element.append(element[i+1])
    return even_element
    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements())) 
#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару. 
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    even_element=[]
    longe = len (element)
    for i in range(0, longe-1):
        if int(element[i])*int(element[i+1])>0:
            even_element.append(element[i])
            even_element.append(element[i+1])
            if len (even_element)>1:
                break
    return even_element
    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements()))
#-----------------------------------------------------------------

#task5------------------------------------------------------------------------------------------------------------------------
"""
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. 
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.  
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    count=0
    even_element=[]
    longe = len (element)
    for i in range(1, longe-1):
        if int(element[i])>int(element[i-1]) and int(element[i])>int(element[i+1]):
            count+=1
    return count
    
def print_elements(output_element):
    print (output_element)
        
print_elements(even_elements(input_elements()))
#-----------------------------------------------------------------

#task6------------------------------------------------------------
"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. 
Если наибольших элементов несколько, выведите индекс первого из них.  
"""
def input_elements():
    element=input().split()
    return element
    
def even_elements(element):
    maximum=element[0]
    counter=0
    even_element=[]
    longe = len (element)
    for i in range(1, longe):
        if int(element[i])>int(maximum):
            maximum=element[i]
    while element[counter]!=maximum:
        counter+=1

    return maximum, counter

    
def print_elements(output_element):
    for i in output_element:
        print (i, end=' ')
        
print_elements(even_elements(input_elements()))
#-----------------------------------------------------------------

#task7------------------------------------------------------------
"""
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.

Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. 
После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, 
таким же, как у Пети, то он должен встать после них. 
"""
def inputе():
    variable=input().split()
    return variable
    
def even_elements():
    height=inputе()
    height_Petya=inputе()
    count=1
    longe=len (height)
    for i in range (0, longe):
        if int(height_Petya[0])<=int(height[i]):
            count+=1
    printe(count)
    return

    
def printe(output_element):
    print (output_element)
        
even_elements()
#-----------------------------------------------------------------

#task8------------------------------------------------------------
"""
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов. 
"""
def inputе():
    liste = input().split()
    return liste
		
def main(liste):
    end_list=[liste[0]]
    count=0
    longe = len (liste)
    for i in range(longe):
        for j in range(len(end_list)):
            if liste[i]==end_list[j]:
                count+=1
        if count==0:        
            end_list.append(liste[i])
        count=0
    result=len(end_list)
    return result
    
def printe(result):
    print (result)
    
printe(main(inputе()))
#-----------------------------------------------------------------

#task9------------------------------------------------------------
"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте. 
"""
def inputе():
    liste = input().split()
    return liste
    
def main(liste):
    longe = len (liste)
    if longe%2==1:
        longe-=1
    for i in range(0, longe, 2):
        buf=liste[i]
        liste[i]=liste[i+1]
        liste[i+1]=buf
    return liste
    
def printe(liste):
    for i in liste:
        print (i, end=' ')
    
printe(main(inputе()))
#-----------------------------------------------------------------

#task10------------------------------------------------------------
"""
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка. 
"""
def inputе():
    liste = input().split()
    return liste
    
def main(liste):
    longe = len(liste)
    if longe<2:
        return liste
        
    if int(liste[0])>=int(liste[1]):
        maxe=liste[0]
        nom_max=0
        mine=liste[1]
        nom_min=1
    else:
        maxe=liste[1]
        nom_max=1
        mine=liste[0]
        nom_min=0
    for i in range(2, longe):
        if int(liste[i])>int(maxe):
            maxe=liste[i]
            nom_max=i
        elif int(liste[i])<int(mine):
            mine=liste[i]
            nom_min=i
    buf=liste[nom_max]
    liste[nom_max]=liste[nom_min]
    liste[nom_min]=buf
    return liste
    
def printe(liste):
    for i in liste:
        print (i, end=' ')
    
printe(main(inputе()))
#-----------------------------------------------------------------

#task11------------------------------------------------------------
"""
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, 
сдвинув влево все элементы, стоящие правее элемента с индексом k.

Программа получает на вход список, затем число k. Программа сдвигает все элементы, 
а после этого удаляет последний элемент списка при помощи метода pop() без параметров.

Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список. 
Также не следует использовать метод pop(k) с параметром. 
"""
def inputе():
    liste = input().split()

    return liste
    
def main(liste):
    namber = int(input())
    liste=liste[:namber]+liste[namber+1:]
    return liste
    
def printe(liste):
    for i in liste:
        print (i, end=' ')
    
printe(main(inputе()))
#-----------------------------------------------------------------

#task12------------------------------------------------------------
"""
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, 
сдвинув все элементы, имевшие индекс не менее k, вправо.

Посколько при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка. 
"""
def inputе():
    liste = input().split()
    return liste
    
def main(liste):
    enter=input().split()
    namber = int(enter[0])
    change_namber = int(enter[1])
    for i in range(namber, len(liste)):
        liste[i], change_namber = change_namber, liste[i]
    liste.append(change_namber)
    
    return liste
    
def printe(liste):
    for i in liste:
        print (i, end=' ')
    
printe(main(inputе()))
#-----------------------------------------------------------------

#task13------------------------------------------------------------
"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
"""
def inputе():
    liste = input().split()
    return liste
    
def main(liste):
    count=0
    longe = len(liste)
    for i in range(longe):
        for j in range(i + 1, longe):
            if liste[i] == liste[j]:
                count += 1
    return count
    
def printe(liste):
    print (liste)
    
printe(main(inputе()))
#-----------------------------------------------------------------

#task14------------------------------------------------------------
"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, в котором они встречаются в списке. 
"""
def inputе():
    liste = input().split()
    return liste
    
def main(liste):
    new_list=[]
    count=0
    longe = len (liste)
    for i in liste:
        for j in liste:
            if int(i)==int(j):
                count+=1
        if count==1:
            new_list.append(i)
        count=0
    return new_list
    
def printe (liste):
    for i in liste:
        print (i, end=' ')
    
printe(main(inputе()))
#-----------------------------------------------------------------
#task15------------------------------------------------------------
"""
N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N. Затем по этому ряду бросили K шаров, 
при этом i-й шар сбил все кегли с номерами от li до ri включительно. Определите, какие кегли остались стоять на месте.

Программа получает на вход количество кеглей N и количество бросков K. Далее идет K пар чисел li, ri, при этом 1≤ li≤ ri≤ N. 
"""
def liste(q):
    liste=[]
    count=0
    for k in range(q): 
        a=input().split()
        for i in range(int(a[0]), int(a[1])+1):
            for g in liste:
                if i == g:
                    count+=1
            if count==0:
                liste.append(i)
            count=0
    return liste
    
q=input().split()
a=['I']*int(q[0])
liste=liste(int(q[1]))
for i in liste:
    a[i-1]='.'
for i in a:
        print (i, end='')
#-----------------------------------------------------------------
#task16------------------------------------------------------------
"""
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, 
определите, есть ли среди них пара бьющих друг друга.

Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. 
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES. 
"""
liste=[]
for i in range(8):
    liste.append([int(i) for i in input().split()])
count=0
result='NO'
for j in range(8):
    for k in range(8):
        if abs(liste[j][0] == liste[k][0]) or abs(liste[j][1] == liste[k][1]) or (abs(liste[j][0]-liste[k][0]) == abs(liste[j][1]-liste[k][1])):
            count+=1
    if count > 1:
        result='YES'
        break
    count=0
print(result)
#-----------------------------------------------------------------
