#task1------------------------------------------------------------
"""
����������� ����� n ���������� ������������ 1 ? 2 ? ... ? n. �����������: n!.
�� ������� ������������ n ��������� �������� n!. ������������ �������������� ����������� math � ���� ������ ���������. 
"""



a=1

n=int(input())

for i in range (1,n+1):
    
	a*=i

print(a)


#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
�� ������� ����������� n ��������� ����� 1!+2!+3!+...+n!. � ������� ���� ������ ����� ������������ ������ ���� ����.
������������ �������������� ����������� math � ���� ������ ���������.
"""



a = 1
b = 0

for i in range(1, int(input()) + 1):
    
	a *= i
    
	b += a

print(b)


#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
���� N �����: ������� �������� ����� N, ����� �������� ����� N ����� �����. ����������� ���������� ����� ����� ��������� ����� � �������� ��� ����������.
��� ����� ���������� ���������� �����, ������ ����, � �� ���������� ����. 
"""



n=int(input())

b=0

for i in range (n):
    
a=int(input())
    
if a == 0:
        
	b=b+1

print(b)



#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
�� ������� ������������ n ? 9 �������� ������� �� n ��������, i-� ��������� ������� �� ����� �� 1 �� i ��� ��������. 
"""


n = int(input())
 
for i in range(n+1):
    
	for j in range(1, i+1):
        
		print(j, end='')
    
	print()


#-----------------------------------------------------------------