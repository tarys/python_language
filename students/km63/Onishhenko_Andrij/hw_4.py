#task1-----------------------------------------------------------
"""
�� ������� ������ ����� N ������������ ��� �������� ����������� 
�����, �� ������������� N, � ������� �����������.
"""
n = int(input(""))
i = 1
while i**2<=n:
	print(i**2)
	i += 1
	
#--------------------------------------------------------------

#task2------------------------------------------------------------
"""
���� ����� �����, �� ������� 2. �������� ��� ���������� �����������
��������, �������� �� 1.
"""
n = int(input())
i = 2
while n%i != 0:
    i += 1
print(i)
#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
�� ������� ������������ ����� N ������� ���������� ����� ������� 
������, �� ������������� N. �������� ���������� ������� � ���� 
�������.
��������� ���������� � ������� ������������ ������!
"""
n = int(input())
num = 2
power = 1
while num <= n:
    num *= 2
    step += 1
print(step - 1, num // 2)
#---------------------------------------------------------------

#task4------------------------------------------------------------
"""
� ������ ���� ��������� �������� x ����������, � ����� �� ������ 
���� ���������� ������ �� 10% �� ����������� ��������. �� ������� 
����� y ���������� ����� ���, �� ������� ������ ����������
�������� �� ����� y ����������.
��������� �������� �� ���� �������������� ����� x � y � ������
������� ���� ����������� �����.
"""
x = int(input())
y = int(input())
i = 1
t = x
while y>t:
    t += t * 0.1
    i += 1
print(i)
#-----------------------------------------------------------------

#task5----------------------------------------------------------
"""
����� � ����� ���������� x ������. �������� �� ������������� �� p 
���������, ����� ���� ������� ����� ������ �������������. 
����������, ����� ������� ��� ����� �������� �� ����� y ������.
��������� �������� ����� ������ �������������� ��������, ��� ����
� ��� ��������� 123.4567 ������, �. �. 123 ����� � 45.67 ������,
�� ����� ���������� � ��� ��������� 123 ����� � 45 ������, �.�. 
123.45 ������.
��������� �������� �� ���� ��� ����������� �����: x, p, y � ������
������� ���� ����� �����.
"""
x = float(input())
p = float(input())
y = float(input())
money = x
i = 0
while money < y:
    money = int(money*100)/100
    money = round(money, 2)
    i += 1
print(i)
#-----------------------------------------------------------------

#task6-----------------------------------------------------------
"""
��������� �������� �� ���� ������������������ ����� ��������������-
-� �����, ������ ����� �������� � ��������� ������. 
������������������ ����������� ������ 0, ��� ���������� �������� 
��������� ������ ��������� ���� ������ � ������� ���������� ������ 
������������������ (�� ������ ������������ ����� 0). �����, 
��������� �� ������ 0, ��������� �� �����.
"""
i = 0
while True:
    n = int(input())
    if n == 0:
        break
    i += 1
print(i)
#---------------------------------------------------------------

#task7----------------------------------------------------------
"""
���������� ����� ���� ��������� ������������������, �������������
������ 0. � ���� � �� ���� ��������� ������� �����, ��������� ��
������ �����, ��������� �� �����.
"""
i = 0
while True:
    n = int(input())
    if n == 0:
        break
    i += n
print(i)
#--------------------------------------------------------------

#task8----------------------------------------------------------
"""
���������� ������� �������� ���� ��������� ������������������, 
������������� ������ 0.
"""
i = 0
x = 0
while True:
    n = int(input())
    if n == 0:
        break
    i += n
    x += 1
print(i/x)
#-----------------------------------------------------------------

#task9--------------------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� 
������ 0. ���������� �������� ����������� �������� ������������������.
"""
i = 0
max = 0
while True:
    n = int(input())
    if n == 0:
        break
    if max<n:
        max = n
print(max)
#-----------------------------------------------------------------

#task10---------------------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� ������
0. ���������� ������ ����������� �������� ������������������. ���� 
���������� ��������� ���������, �������� ������ ������� �� ���. 
��������� ��������� ���������� � ����.
"""
i = 0
max = 0
max_i = 0
while True:
    n = int(input())
    if n == 0:
        break
    if max<n:
        max = n
        maxi = i
    i += 1
print(maxi)
#-----------------------------------------------------------------

#task11--------------------------------------------------------
"""
���������� ���������� ������ ��������� � ������������������, �����-
-�������� ������ 0.
"""
i = 0
e = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n%2 == 0:
        i += 1
print(i)
#-----------------------------------------------------------------

#task12-------------------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� 
������ 0. ����������, ������� ��������� ���� ������������������ 
������ ����������� ��������.
"""
i = 0
x = float()
while True:
    n = int(input())
    if n == 0:
        break
    if n > x:
        i += 1
    x = n
print(i)
#-----------------------------------------------------------------

#task13---------------------------------------------------------
"""
������������������ ������� �� ��������� ����������� ����� � 
����������� ������ 0. ���������� �������� ������� �� �������� 
�������� � ���� ������������������. �������������, ��� � 
������������������ ���� ���� �� ��� ��������.
"""
#--------------------------------------------------------------
i = 0
max = 0
n_max = 0
l = []
while True:
    n = int(input())
    l.append(n)
    if n == 0:
        break
l.sort()
print(l[-2])
#-----------------------------------------------------------------

#task14---------------------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� 
������ 0. ����������, ������� ��������� ���� ������������������ 
����� �� ����������� ��������.
"""
max = 0
max_i = 0
l = []
k = 0
while True:
    n = int(input())
    if n == 0:
        break
    l.append(n)
    if max<n:
        max = n
for i in l:
    if i == max:
        k += 1
print(k)
#-----------------------------------------------------------------

#task15--------------------------------------------------------
"""
������������������ ��������� ������������ ���:
?0 = 0,  ?1 = 1,  ?n = ?n?1 + ?n?2.
�� ������� ����� n ���������� n-� ����� ��������� ?n.
��� ������ ����� ������ � ������ for.
"""
n = int(input())
if n == 0:
    print(0)
else:
    f = []
    f.append(0)
    f.append(1)
    i = 2
    while i<=n:
        f.append(f[i-1] + f[i-2])
        i += 1
    print(f[-1])
#-----------------------------------------------------------------

#task16---------------------------------------------------------
"""
���� ����������� ����� A. ����������, ����� �� ����� ������ 
��������� ��� ��������, �� ���� �������� ����� ����� n, ��� 
?n = A. ���� � �� �������� ������ ���������, �������� ����� -1.
"""
a = int(input())
f1 = 0
f2 = 1
n = 0
fibo = 0
while fibo != a:
    fibo = f1 + f2
    f2 = f1
    f1 = fibo
    n += 1
    if fibo > a:
        n = -1
        break
print(n)
#-----------------------------------------------------------------

#task17----------------------------------------------------------
"""
���� ������������������ ����������� �����, ������������� ������ 0.
����������, ����� ���������� ����� ������ ������ ��������� ����
������������������ ����� ���� �����.
"""
i = 0
max = 0
n_max = 0
l = []
l2 = [0]
k = 1
while True:
    n = int(input())
    if n == 0:
        break
    l.append(n)
for i in range(1, len(l)):
    if l[i-1] == l[i]:
        k += 1
    else:
        l2.append(k)
        k = 1
l2.append(k)
l2.sort()
print(l2[-1])
#--------------------------------------------------------------

#task18------------------------------------------------------------
"""
���� ������������������ ����������� ����� x1x1, x2x2, ..., xnxn. ����������� ����������� ���������� ��������
��� s=x1+x2+�+xnns=x1+x2+�+xnn � ������� �������������� ������������������.
���������� ����������� ���������� ��� ������ ������������������ ����������� �����, ������������� ������ 0.
"""
i = 1
up = 0
l = []
suM = 0
while True:
    x = int(input())
    if x == 0:
        break
    l.append(x)
    suM += x
    i += 1
s = suM/(i-1)
n = i-1
for i in l:
    up += (i - s) ** 2
print((up/(n-1)) ** 0.5)
#--------------------------------------------------------------