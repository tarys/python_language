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
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task9------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task10------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task11------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task12------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task13------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------

#task14------------------------------------------------------------
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. 
Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару. 
"""
lis=input()
lis_razdel=lis.split()
longe=len(lis_razdel)
for i in range(longe-1):
    if (int(lis_razdel[i])>0) and (int(lis_razdel[i+1])>0) or (int(lis_razdel[i])<0) and (int(lis_razdel[i+1])<0):
        print(lis_razdel[i], lis_razdel[i+1])
        break


#-----------------------------------------------------------------