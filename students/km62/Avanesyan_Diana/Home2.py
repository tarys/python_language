Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
print ('Home work №2') 
print() 

 # task #1 

Задача №1 
Умова: Дано два цілих числа. Вивести найменше з них. 
Вхідні дані: користувач вводить ціле число 
Вихідні дані: вивести ціле число 

# input 
a=int(input()) 
b=int(input()) 
#output 
print('Task 1') 
if a<b: 
print(a) 
else: 
print(b) 
print("First task complited!") 

# task #2 

Умова: Вивести результат функціїsign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0.. 
Вхідні дані: користувач вводить дійсне число. 
Вихідні дані: вивести результат sign. 

# input 
x=int(input()) 
#output 
print(‘ 
if x>0: 
print('sign(x)=1') 
elif x<0: 
print('sign(x)=-1') 
elif x==0: 
print('sign(x)=0')

        #task3 #2

  a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))

if (a<b and a<c):
    print(a)
elif (b<a and b<c):
    print(b)
elif (c<a and c<b): 
    print(c)
4.	x=int(input('Enter year: '))
if ((x%4==0) and (x%100 != 0)):
    	print('LEAP')
       elif (x%400==0):
    	print('LEAP')
        else:
    	print('COMMON')

5.	a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))

if ((a==b) and (b==c)):
    	print('3')
         elif ((a==b) or (b==c) or (a==c)):
    	print('2')
         else:
    	print('0')

6.	a=int(input('Enter number of the first cell line(1-8): '))
b=int(input('Enter number of the first cell column(1-8):'))
a2=int(input('Enter number of the second cell line(1-8): '))
b2=int(input('Enter number of the second cell column(1-8):'))

If (((a2-1==a) and (b2=b)) or ((a2==a) and (b2+1==b)) or ((a2+1==a) and (b2==b)) or ((a2==a) and (b2-1==b))):
print('Yes')
       else:
print('NO')


7.	a=int(input('Enter number of the first cell line(1-8): '))
b=int(input('Enter number of the first cell column(1-8):'))
a2=int(input('Enter number of the second cell line(1-8: '))
b2=int(input('Enter number of the second cell column(1-8):'))

if (((a+b)+(a2+b2))%2==0):
print('YES')
        else:
  	print('NO')

8.	a=int(input('Enter number of the first cell line(1-8): '))
b=int(input('Enter number of the first cell column(1-8):'))
a2=int(input('Enter number of the second cell line(1-8): '))
b2=int(input('Enter number of the second cell column(1-8):'))

if (((b2==b) or (b2==b+1) or (b2==b-1)) and ((a2==a) or (a2==a-1) or(a2==a+1))):
    print('Yes')
else:
    print('No')

9.	a=int(input('Enter number of the first cell line(1-8): '))
b=int(input('Enter number of the first cell column(1-8):'))
a2=int(input('Enter number of the second cell line(1-8): '))
b2=int(input('Enter number of the second cell column(1-8):'))

if (a+b==a2+b2):
    print('Yes')
else:
    print('No')

10.	a=int(input('Enter number of the first cell line(1-8): '))
b=int(input('Enter number of the first cell column(1-8):'))
a2=int(input('Enter number of the second cell line(1-8): '))
b2=int(input('Enter number of the second cell column(1-8):'))

if (((a+b==a2+b2) or (b2==b) or (a2==b)) and (0<(abs(a)+abs(b))<11)):
    print('Yes')
else:
    print('No')

11.	a=int(input('Enter number of the first cell line(1-8): '))
b=int(input('Enter number of the first cell column(1-8):'))
a2=int(input('Enter number of the second cell line(1-8): '))
b2=int(input('Enter number of the second cell column(1-8):'))

if (((b==b2)or(a==a2)) and (((a2==a-1) or (a2==a-2)) or ((b2==b+1)or(b2==b+2))) and (0<a+b<11)):
    print('Yes')
else:
    print('No')

12.	 a=int(input('Enter the lenght chokolate: '))
b=int(input('Enter the width chokolate: '))
z=int(input())

if ((z<(a*b)) and (z%a==0 or z%b==0)):
print('Yes')
elif ((a<0) or (b<0) or (z<0)) :
print('Invalid number')
else:
print('No')



