#task1--------------------------------------------
"""
Display all items in the list with even indices (ie, A [0], A [2], A [4], ...).
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
Print a list of all the even-numbered elements. In this case, use a for loop to iterate over the list, not their indices!
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
Given a list of numbers. Print a list of all the elements that are larger than the previous element.
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
Given a list of numbers. If it contains two adjacent elements of one sign, display these numbers.
If adjacent elements of one sign not - do not output anything. If there are several pairs of neighbors - print the first pair.
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
Given a list of numbers. Determine how much of this list of items that are more than two of their neighbors, and bring the number of such elements.
The last elements of the list is never taken into account, since they lack the neighbors.
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
Given a list of numbers. Print the value of the largest element in the list, and then the index of the item in the list.
If the largest element, output index of the first of them.
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
Peter moved to another school. In gym class he needed to define its place in the ranks. Help him to do it.
The program receives the input of a non-increasing sequence of natural numbers, meaning the growth of each person in the ranks.
After this number is entered X - Petit growth. All numbers in the input natural and not exceed 200.
Display the number with which Peter has to get up in the system. If there are people in the ranks of the same stature, the same as at Petit, it must stand up after them.
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
Given a list, ordered by non-decreasing order of elements in it.
Determine how much various elements therein.
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
Move the neighboring cells list (A [0] c A [1], A [2] c A [3], and so on. D.).
If an odd number of elements, the last element is in its place.
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
In all the different elements of the list.
Swap the minimum and maximum element of this list.
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
Given a list of numbers, and the index k in the list.
Remove from the list item with the k index, sliding to the left all the elements, standing to the right of the element with index k.
The program receives the list of input, then number k.
The program moves all the elements, and then removes the last element of the list using the pop () method with no parameters.
The program must implement a shift directly into the list, instead of doing so in the derivation of the elements.
You also can not use the additional list. Also, do not use the method pop (k) with a parameter ..
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
Given a list of integers, the integer k and the value C.
Must be inserted into the list at position index k element
equal to C, moving all the elements had no less than the index k, the right.
Since the number of elements in this list increases,
after reading the list to the end you will need to add a new element,
using the append method. 
The insert should be implemented already in the read list
Doing this in the derivation and without creating an additional list.
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
Given a list of numbers. Count how many pairs of elements in it that are equal to each other.
It is believed that any two elements are equal to each other to form a pair that you want to count.
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
Dan list. Bring those elements that appear in the list only once.
The elements you want to display in the order in which they appear in the list.
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
N pins put in one number, numbered from left to right with numbers from 1 to N.
Then, on the number of balls thrown K, while the i-th ball knocked down all the pins with the numbers to li ri inclusive.
Determine which pins are left standing on the spot.
The program receives the input of the number of pins N and the number of shots K.
Next comes the K pairs of numbers li, ri, while 1≤ li≤ ri≤ N. 
The program should print a sequence of N characters, where the j-th symbol is "I",
if the j-I pin remained standing, or ".", if the j-pin I was hit.
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
It is known that on a board of 8 × 8 can arrange 8 queens so that they do not hit each other.
You are given a balance of 8 queens on the board, determine whether there is among them a pair of beating each other.
The program takes an eight pairs of numbers, each number from 1 to 8 - 8 queens coordinates.
If the queen did not hit each other, output word of NO, otherwise print YES.
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
