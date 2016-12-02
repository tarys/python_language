#task1------------------------------------------------------------
"""
������� ������� ������� ��������� ������������� ��������. �������� ��� �����: ����� ������ � ����� �������, � ������� ����� ���������� ������� � ��������� �������. ���� ����� ��������� ���������, �� ��������� ���, � �������� ������ ����� ������, � ���� ������ ����� ����� �� ���, � �������� ������ ����� �������.
��������� �������� �� ���� ������� ������� n � m, ����� n ����� �� m ����� � ������.
"""


#default
massive=[]
maxweight=0
maxheight=0
#input blok
height,weight = input().split()

for i in range(int(height)):
    massive.append(input().split())
    
for i in range(int(height)):
    for j in range(int(weight)):
        if int(massive[i][j])>int(massive[maxheight][maxweight]):
            maxheight=i
            maxweight=j
print(maxheight,maxweight)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
���� �������� ����� n. �������� ��������� ������ �� n?n ���������,
�������� ��� ��������� "." (������ ������� ������� �������� ������� �� ������ �������).
����� ��������� ��������� "*" ������� ������ �������, ������� ������� �������, ������� ��������� � �������� ���������.
� ���������� ������� � ������� ������ ������������ ����������� ���������.
�������� ���������� ������ �� �����, �������� �������� ������� ���������. 
"""



number = int(input())

list_=[['.'] * number for i in range(number)]
for i in range(number):
    for j in range(number):
        if i == ( number // 2 ) :
            list_[i][j]='*'
        if j == ( number // 2 ) :
            list_[i][j]='*'
        if i==j:
            list_[i][j]='*'
        if (i+j)==number-1:
            list_[i][j]='*'
            
for i in range(number):
    print()
    for j in range(number):
        print(list_[i][j],end=' ')

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
���� ��� ����� n � m. �������� ��������� ������ �������� n?m
� ��������� ��� ��������� "." � "*" � ��������� �������.
� ����� ������� ���� ������ ������ �����.
"""



def list_create(n,m,list_):
    for i in range(int(n)):
        list_.append(('. '*int(m)).split())
    return list_
#default
list_=[]
#input
n,m=input().split()
#main  
list_=list_create(n,m,list_)

for i in range(int(n)):
        if i%2!=0:
            for j in range(0,int(m),2):
                list_[i][j]='*'
        else:
            for j in range(1,int(m),2):
                list_[i][j]='*'
#print
for i in range(int(n)):
    if i!=0:
        print()
    for j in range(int(m)):
        print(list_[i][j],end=' ')

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
���� ����� n. �������� ������ �������� n?n � ��������� ��� �� ���������� �������.
�� ������� ��������� ������ ���� �������� ����� 0. �� ���� ����������, ����������� � �������, ����� 1.
�� ��������� ���� ���������� ����� 2, � �.�. 
"""



def print_array(array):
    for str in array:
        print()
        for elem in str:
            print(elem,end=' ')
n=int(input())

array=[[0] * n for i in range(n)]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i<j:
                array[i][j]=array[i+1][j]+1
            if j<i:
                array[i][j]=array[i][j+1]+1
print_array(array)

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
���� ����� n. �������� ������ �������� n?n � ��������� ��� �� ���������� �������:
����� �� ���������, ������ �� ������� �������� � ����� ������ ���� ����� 1.
�����, ������� ���� ���� ���������, ����� 0.
�����, ������� ���� ���� ���������, ����� 2.
���������� ������ �������� �� �����. ����� � ������ ���������� ����� ��������.
"""



def create_list(n,list_):
    for i in range(n):
        list_.append(('0 '*n).split())
    return(list_)
#default
list_=[]
#input
n=int(input())
#main
list_=create_list(n,list_)

for i in range(n):
    for j in range(n):
        if i+j==n-1:
            list_[i][j]=1
        if i+j>n-1:
            list_[i][j]=2
#print          
for i in range(n):
    if i!=0:
        print()
    for j in range(n):
        print(list_[i][j], end=' ')

#-----------------------------------------------------------------

 
#task6------------------------------------------------------------
"""
��� ��������� ������ � ��� �����: i � j. ��������� � ������� ������� � �������� i � j � �������� ���������.
��������� �������� �� ���� ������� ������� n � m, ����� �������� �������, ����� ����� i � j.
������� �������� � ���� ������� swap_columns(a, i, j). 
"""



def swap_columns(a, i, j):
    for k in range(n):
        a[k][j],a[k][i]=a[k][i],a[k][j]
    return a
def print_array(array):
    for str in array:
        print()
        for elem in str:
            print(elem,end=' ')
n,m=input().split()
n,m=int(n),int(m)
array=[input().split() for i in range(n)]
i,j=input().split()
i,j=int(i),int(j)
print_array(swap_columns(array,i,j))

#-----------------------------------------------------------------