#task1------------------------------------------------------------
"""
���� ������ �������������� �����: x1, y1, x2, y2. �������� ������� distance(x1, y1, x2, y2), ����������� ���������� ����� ������ (x1,y1) � (x2,y2). �������� ������ �������������� ����� � �������� ��������� ������ ���� �������.
"""
#Program calculates length of line
import math 
def distance(x1,y1,x2,y2):
    result=round(math.sqrt((x2-x1)**2+(y2-y1)**2),5)
    return result
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
print(distance(x1,y1,x2,y2))

#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
���� �������������� ������������� ����� a � ����e ����� n.
��������� an. ������� �������� � ���� ������� power(a, n).
"""
#Program calculates power of number 
def power(a,n):
    original_number=a
    if n<0:
        for i in range(1,n,-1):
            a/=original_number
    elif n>0:
        for i in range(1,n):
            a*=original_number
    else:
        a=1
    return a
a=float(input())
n=int(input())
print(power(a,n))

#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
���� �������������� ������������� ����� a � ����� ��������������� ����� n. 
��������� an �� ��������� �����, ���������� � ������� ����� ** � ������� math.pow(), � ��������� ������������ ����������� an=a?an-1.
������� �������� � ���� ������� power(a, n).
"""
#Program calculates power of number with recursion
def power(a,n):
    if n==0:
        return 1
    else:
        return a*power(a,n-1)
a=float(input())
n=int(input())
print(power(a,n))
#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
�������� ������� fib(n), ������� �� ������� ������ ���������������� n ���������� n-e ����� ���������. � ���� ������ ������ ������������ ����� � ����������� ��������.
"""
#Program calculates Fibonachi number with recursion
def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))

#-----------------------------------------------------------------