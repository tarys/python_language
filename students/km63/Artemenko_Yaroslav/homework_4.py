#task1------------------------------------------------


"""
������ ������� ���������
�� ������� ������ ����� N ������������ ��� �������� ����������� �����, �� ������������� N, � ������� �����������.
"""
#
n=int(input())

i=1

while (i**2)<=n:

    print(i**2)

    i+=1
#-----------------------------------------------------


#task2------------------------------------------------


"""
������ ������������ ���������
���� ����� �����, �� ������� 2. �������� ��� ���������� ����������� ��������, �������� �� 1.
"""
#
n=int(input())

i=2

while n%i!=0:

    i+=1

print(i)
#-----------------------------------------------------


#task3------------------------------------------------


"""
������ �������� ������
�� ������� ������������ ����� N ������� ���������� ����� ������� ������, �� ������������� N. �������� ���������� ������� � ���� �������.

��������� ���������� � ������� ������������ ������!
"""
#
n = int (input ())

k=2

m=1

while k<=n:
 
    k*=2

     m+=1

print(m-1,k//2)
#-----------------------------------------------------


#task4------------------------------------------------


"""
������ ��������� ��������
� ������ ���� ��������� �������� x ����������, � ����� �� ������ ���� ���������� ������ �� 10% �� ����������� ��������. �� ������� ����� y ���������� ����� ���, �� ������� ������ ���������� �������� �� ����� y ����������.

��������� �������� �� ���� �������������� ����� x � y � ������ ������� ���� ����������� �����.
"""
#
x=int(input())

y=int(input())

day=1

while x<y:

    x+=x*0.1

    day+=1

print(day)
#-----------------------------------------------------


#task5------------------------------------------------


"""
������ ����������� ���������
����� � ����� ���������� x ������. �������� �� ������������� �� p ���������, ����� ���� ������� ����� ������ �������������. ����������, ����� ������� ��� ����� �������� �� ����� y ������.

��������� �������� ����� ������ �������������� ��������, ��� ���� � ��� ��������� 123.4567 ������, �. �. 123 ����� � 45.67 ������, �� ����� ���������� � ��� ��������� 123 ����� � 45 ������, �.�. 123.45 ������.

��������� �������� �� ���� ��� ����������� �����: x, p, y � ������ ������� ���� ����� �����.
"""
#
x = float(input())
p = float(input())
y = float(input())
i = 0
while x < y:
    x += x * p*0.01
    x = int(x*100)/100
    i += 1
print(i)
#-----------------------------------------------------


#task6------------------------------------------------


"""
������ ������ ������������������
��������� �������� �� ���� ������������������ ����� ��������������� �����, ������ ����� �������� � ��������� ������. ������������������ ����������� ������ 0, ��� ���������� �������� ��������� ������ ��������� ���� ������ � ������� ���������� ������ ������������������ (�� ������ ������������ ����� 0). �����, ��������� �� ������ 0, ��������� �� �����.
"""
#
i=0

while True:

    n=int(input())

    if n==0:

        break

    i+=1

print(i)
#-----------------------------------------------------


#task7------------------------------------------------


"""
������ ������ ������������������
���������� ����� ���� ��������� ������������������, ������������� ������ 0. � ���� � �� ���� ��������� ������� �����, ��������� �� ������ �����, ��������� �� �����.
"""
#
sum=0
while True:
    n=int(input())
    if n==0:
        n+=n
        break
    sum+=n
print(sum)
#-----------------------------------------------------


#task8------------------------------------------------


"""
������ �������� �������� ������������������
���������� ������� �������� ���� ��������� ������������������, ������������� ������ 0.
"""
#
i=0
sum=0
while True:
    n = int(input())
    if n==0:
        n+=n
        break
    sum+=n
    i+=1
    s=sum/i
print(s)
#-----------------------------------------------------


#task9------------------------------------------------


"""
������ ��������� ������������������
������������������ ������� �� ����������� ����� � ����������� ������ 0. ���������� �������� ����������� �������� ������������������.
"""
#
i = 0
max = 0
while True:
    n = int(input())
    if n == 0:
        break
    if max<n:
        max=n
print(max)
#-----------------------------------------------------


#task10------------------------------------------------


"""
number = 1
max = 0
i = 0
index = 0
 
while number != 0:
    number = int(input())
    if number > max:
        max = number
        index = i
    i += 1
print(index)
"""
#
#-----------------------------------------------------


#task11------------------------------------------------


"""
������ ����������� ������ ��������� ������������������
���������� ���������� ������ ��������� � ������������������, ������������� ������ 0.
"""
#
number = 1
max = 0
count = 0
while number != 0:
    number = int(input())
    if number % 2 == 0 and number != 0:
        count += 1
print(count)
#-----------------------------------------------------


#task12------------------------------------------------


"""
������ ����������� ���������, ������� ������ �����������
������������������ ������� �� ����������� ����� � ����������� ������ 0. ����������, ������� ��������� ���� ������������������ ������ ����������� ��������.
"""
#
n=0

n1=1

count=0

while n1!=0:

    n1=int(input())

    if n1>n:

        if n!=0:

            count+=1

    n=n1

print(count)
#-----------------------------------------------------


#task13------------------------------------------------


"""
������ ������� ��������
������������������ ������� �� ��������� ����������� ����� � ����������� ������ 0. ���������� �������� ������� �� �������� �������� � ���� ������������������. �������������, ��� � ������������������ ���� ���� �� ��� ��������.
"""
#
n=1

n1=0

n2=0

while n!=0:

    n=int(input())

    if n>n1:

        n2=n1

        n1=n

    elif n>n2:

        n2=n

print(n2)
    
#-----------------------------------------------------


#task14------------------------------------------------


"""
������ ����������� ���������, ������ ���������
������������������ ������� �� ����������� ����� � ����������� ������ 0. ����������, ������� ��������� ���� ������������������ ����� �� ����������� ��������.
"""
#
n=1

max=0

count=1

while n!=0:

    n=int(input())

    if n>max:

        count=1

        max=n

    elif n==max:

        count+=1

print(count)
#-----------------------------------------------------


#task15------------------------------------------------


"""
������������������ ��������� ������������ ���:
?0 = 0,  ?1 = 1,  ?n = ?n?1 + ?n?2.

�� ������� ����� n ���������� n-� ����� ��������� ?n.

��� ������ ����� ������ � ������ for
"""
#
i=0

n=0

n1=1

n2=0

count=int(input())-1

for i in range(0,count):

    n=n1+n2

    n2=n1

    n1=n

    if count==0:

        n=1

print(n)
#-----------------------------------------------------


#task16------------------------------------------------


"""
������ ������ ����� ���������
���� ����������� ����� A. ����������, ����� �� ����� ������ ��������� ��� ��������, �� ���� �������� ����� ����� n, ��� ?n = A. ���� � �� �������� ������ ���������, �������� ����� -1.
"""
#
a=int(input())

i=0

n2,n1=0,1

while True:

    if n1>a:

        i=-1

        break

    elif n1==a:

        i+=1

        break

    n2,n1=n1,n2+n1

    i+=1

print(i)
#-----------------------------------------------------


#task17------------------------------------------------


"""
������ ������������� ����� ������ ������ ������ ���������
���� ������������������ ����������� �����, ������������� ������ 0. ����������, ����� ���������� ����� ������ ������ ��������� ���� ������������������ ����� ���� �����.
"""
#
n=1

i=1

previous_i=0

previous=0

while True:

    n=int(input())

    if n==0:

        break

    if n==previous:

        i+=1

    else:

        i=1

    if i>previous_i:

        previous_i=i

    previous=n

print(previous_i)
#-----------------------------------------------------


#task18------------------------------------------------


"""
���� ������������������ ����������� ����� x1x1, x2x2, ..., xnxn. ����������� ����������� ���������� ��������
?=(x1?s)2+(x2?s)2+�+(xn?s)2n?1???????????????????????????????v
?=(x1?s)2+(x2?s)2+�+(xn?s)2n?1
��� s=x1+x2+�+xnns=x1+x2+�+xnn � ������� �������������� ������������������.

���������� ����������� ���������� ��� ������ ������������������ ����������� �����, ������������� ������ 0.
"""
#

#-----------------------------------------------------
