#task1------------------------------------------------------------
"""
���� ������ �������������� �����: x1, y1, x2, y2. �������� ������� distance(x1, y1, x2, y2), ����������� ���������� ����� ������ (x1,y1) � (x2,y2). �������� ������ �������������� ����� � �������� ��������� ������ ���� �������.

"""
#
from math import sqrt

def distance(x1, y1, x2, y2):

	dis=sqrt((x2-x1)**2+(y2-y1)**2)

	print("distance",round(dis,3))
x1=float(input("Enter number:"))

y1=float(input("Enter number:"))

x2=float(input("Enter number:"))

y2=float(input("Enter number:"))

distance(x1,y1,x2,y2)
#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
���� �������������� ������������� ����� a � ����e ����� n.

��������� an. ������� �������� � ���� ������� power(a, n).

"""
#
a=float(input("Enter number:"))

n=int(input("Enter number:"))

def power(a, n):

	p=1

	for i in range(n):

		p=p*a

	print("a**n:",round(p,3))

power(a,n)
#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
���� �������������� ������������� ����� a � ����e ����� n.

��������� an. ������� �������� � ���� ������� power(a, n).

"""
#
a=float(input("Enter number:"))

n=int(input("Enter number:"))

def power(a, n):

	p=1

	for i in range(n):

		p=p*a

	print("a**n:",round(p,3))

power(a,n)
#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
���� �������������� ������������� ����� a � ����� ��������������� ����� n. ��������� an �� ��������� �����, ���������� � ������� ����� ** � ������� math.pow(), � ��������� ������������ ����������� an=a?an-1.
"""
#
a=float(input("Enter number:"))

while a<0:

	if a<0:

		print("incorrect input,try again...")

	a=float(input("Enter number:"))

n=int(input("Enter number:"))

while n<0:

	if n<0:

		print("incorrect input,try again...")

	n=int(input("Enter number:"))

def power(a, n):

	if n==0:

		return 1

	else:

		return a*power(a,n-1)

p=power(a,n)

print(round(p,3))
#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
�������� ������� fib(n), ������� �� ������� ������ ���������������� n ���������� n-e ����� ���������. � ���� ������ ������ ������������ ����� � ����������� ��������.

"""
#
n=int(input("Enter number:"))

def fib(n):

	if n==1 or n==0:

		return 1

	return fib(n-1)+fib(n-2)

print(fib(n))
#-----------------------------------------------------------------