#task1------------------------------------------------------------
"""
�������� ��� �������� ������ � ������� ��������� (�� ���� A[0], A[2], A[4], ...).
"""



a = [int(i) for i in input().split()]

for i in range(0, len(a), 2):
	print(a[i])

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
�������� ��� ������ �������� ������. ��� ���� ����������� ���� for, ������������ �������� ������, � �� �� �������!
"""



a = [int(i) for i in input().split() if int(i) % 2 == 0]

for i in a:
    print(i)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
��� ������ �����. �������� ��� �������� ������, ������� ������ ����������� ��������.
"""



a = [int(i) for i in input().split()]

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
��� ������ �����. ���� � ��� ���� ��� �������� �������� ������ �����, �������� ��� �����. ���� �������� ��������� ������ ����� ��� � �� �������� ������. ���� ����� ��� ������� ��������� � �������� ������ ����.
"""



a = [int(i) for i in input().split()]

for i in range(1, len(a)):
    if a[i] * a[i - 1] >= 0:
        print(a[i - 1])
        print(a[i])
        break

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
��� ������ �����. ����������, ������� � ���� ������ ���������, ������� ������ ���� ����� �������, � �������� ���������� ����� ���������. ������� �������� ������ ������� �� �����������, ��������� � ��� ������������ �������.
"""



a = [int(i) for i in input().split()]
count = 0

for i in range(1, len(a) - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        count += 1
print(count)

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
��� ������ �����. �������� �������� ����������� �������� � ������, � ����� ������ ����� �������� � ������. ���� ���������� ��������� ���������, �������� ������ ������� �� ���.
"""



a = [int(i) for i in input().split()]
index = 0
max = a[0]

for i in range(1, len(a)):
    if a[i] > max:
        max = a[i]
        index = i 
print(max, index)

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
���� ������� � ������ �����. �� ����� ����������� ��� ������������ ���������� ��� ����� � �����. �������� ��� ��� �������.
��������� �������� �� ���� �������������� ������������������ ����������� �����, ���������� ���� ������� �������� � �����. ����� ����� �������� ����� X � ���� ����. ��� ����� �� ������� ������ ����������� � �� ��������� 200.

�������� �����, ��� ������� ���� ������ ������ � �����. ���� � ����� ���� ���� � ���������� ������, ����� ��, ��� � ����, �� �� ������ ������ ����� ���.
"""



a = [int(i) for i in input().split()]
x = int(input())
index = 1

for i in range(0, len(a)):
    if a[i] < x:
        index = i + 1
        break
else:
    index = len(a) + 1
print(index)

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
��� ������, ������������� �� ���������� ��������� � ���. ����������, ������� � ��� ��������� ���������.
"""



a = [int(i) for i in input().split()]
b = []

for i in a:
    for j in b:
        if i == j:
            break
    else:
        b.append(i)
print(len(b))

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
����������� �������� �������� ������ (A[0] c A[1], A[2] c A[3] � �. �.). ���� ��������� �������� �����, �� ��������� ������� �������� �� ����� �����.
"""



a = [int(i) for i in input().split()]

for i in range(0, len(a) - 1, 2):
    a[i], a[i+1] = a[i+1], a[i]
for i in a:
    print(i)

#-----------------------------------------------------------------


#task10-----------------------------------------------------------
"""
� ������ ��� �������� ��������. ��������� ������� ����������� � ������������ ������� ����� ������.
"""



a = [int(i) for i in input().split()]
max = 0
min = 0

for i in range(len(a)):
    if a[i] > a[max]:
        max = i
    if a[i] < a[min]:
        min = i
a[min], a[max] = a[max], a[min]

for i in a:
    print(i)

#-----------------------------------------------------------------


#task11-----------------------------------------------------------
"""
��� ������ �� ����� � ������ �������� � ������ k. ������� �� ������ ������� � �������� k, ������� ����� ��� ��������, ������� ������ �������� � �������� k.
��������� �������� �� ���� ������, ����� ����� k. ��������� �������� ��� ��������, � ����� ����� ������� ��������� ������� ������ ��� ������ ������ pop() ��� ����������.

��������� ������ ������������ ����� ��������������� � ������, � �� ������ ��� ��� ������ ���������. ����� ������ ������������ �������������� ������. ����� �� ������� ������������ ����� pop(k) � ����������.
"""



a = [int(i) for i in input().split()]
k = int(input())

for j in range(k, len(a) - 1):
    a[j], a[j + 1] = a[j + 1], a[j]
a.pop()
for i in a:
    print(i)

#-----------------------------------------------------------------


#task12-----------------------------------------------------------
"""
��� ������ ����� �����, ����� k � �������� C. ���������� �������� � ������ �� ������� � �������� k �������, ������ C, ������� ��� ��������, ������� ������ �� ����� k, ������.
��������� ��� ���� ���������� ��������� � ������ �������������, ����� ���������� ������ � ��� ����� ����� ����� �������� ����� �������, ��������� ����� append.

������� ���������� ������������ ��� � ��������� ������, �� ����� ����� ��� ������ � �� �������� ��������������� ������.
"""



a = [int(i) for i in input().split()]
k, c = [int(i) for i in input().split()]
temp = c

for j in range(k, len(a)):
    a[j], temp = temp, a[j]
a.append(temp)

for i in a:
    print(i)

#-----------------------------------------------------------------


#task13-----------------------------------------------------------
"""
��� ������ �����. ����������, ������� � ��� ��� ���������, ������ ���� �����. ���������, ��� ����� ��� ��������, ������ ���� ����� �������� ���� ����, ������� ���������� ���������.
"""



a = [int(i) for i in input().split()]
count = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            count += 1
print(count)

#-----------------------------------------------------------------


#task14-----------------------------------------------------------
"""
��� ������. �������� �� ��� ��������, ������� ����������� � ������ ������ ���� ���. �������� ����� �������� � ��� �������, � ������� ��� ����������� � ������.
"""



a = [int(i) for i in input().split()]

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j] and i != j:
            break
    else:
        print(a[i])

#-----------------------------------------------------------------


#task15-----------------------------------------------------------
"""
N ������ ��������� � ���� ���, ����������� �� ����� ������� ������� �� 1 �� N. ����� �� ����� ���� ������� K �����, ��� ���� i-� ��� ���� ��� ����� � �������� �� li �� ri ������������. ����������, ����� ����� �������� ������ �� �����.
��������� �������� �� ���� ���������� ������ N � ���������� ������� K. ����� ���� K ��� ����� li, ri, ��� ���� 1? li? ri? N.

��������� ������ ������� ������������������ �� N ��������, ��� j-� ������ ���� �I�, ���� j-� ����� �������� ������, ��� �.�, ���� j-� ����� ���� �����.
"""



n, k = [int(i) for i in input().split()]
throws = [[int(i) for i in input().split()] for j in range(k)]

for i in range(1, n + 1):
    for j in throws:
        if i >= j[0] and i <= j[1]:
            print('.', end = '')
            break
    else:
        print('I', end = '')

#-----------------------------------------------------------------


#task16-----------------------------------------------------------
"""
��������, ��� �� ����� 8?8 ����� ���������� 8 ������ ���, ����� ��� �� ���� ���� �����. ��� ���� ����������� 8 ������ �� �����, ����������, ���� �� ����� ��� ���� ������ ���� �����.
��������� �������� �� ���� ������ ��� �����, ������ ����� �� 1 �� 8 � ���������� 8 ������. ���� ����� �� ���� ���� �����, �������� ����� NO, ����� �������� YES.
"""



queens = [[int(i) for i in input().split()] for j in range(8)]
beat = False

for i in range(len(queens)):
    x1 = queens[i][0]
    y1 = queens[i][1]
    for j in range(len(queens)):
        if i == j:
            continue
        x2 = queens[j][0]
        y2 = queens[j][1]
        if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
            beat = True
            break
if beat:
    print('YES')
else:
    print('NO')

#-----------------------------------------------------------------

