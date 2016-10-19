List of squares
"""
For a given integer N, print all the squares of integer numbers less or equal than N, in ascending order.
"""
# Print all the squares of integer numbers less or equal than N, in ascending order:
# N=int(input())
     N=int(input())
x = 1
while (x**2) <=N:
# print(x ** 2)
	print(x ** 2)
	x += 1

Least divisor
"""
Given an integer not less than 2. Print its smallest integer divisor greater than 1.
"""
# Print its smallest integer divisor greater than 1:
# number=int(input())
number=int(input())
x=2
while number%x!=0:
    if number<2:
#number<2
     break
    x+=1
else:
#print(x)
    print(x)
The power of two
"""
For a given integer number N find the greatest integer that is a power of two, less or equal than N. Print the exponent and the power of two itself.
"""
# Print the exponent and the power of two itself:
# N=int(input())
     N=int(input())
x=2
i=0
while x<=N:
#x<=N
	x*=2
	i+=1
else:
# print(i,x/2)
	print(i,x/2)

Morning jog
"""
On the first day of the athlete ran x miles, and then every day it increased the mileage by 10% from the previous value. For the given number y determine the number of the day on which the mileage of the athlete will be not less than ymiles.
The program takes two real numbers x and y and should print one integer number.

"""
# The program takes two real numbers x and y and should print one integer number:
# x=int(input())
x=int(input())

# y=int(input())
y=int(input())
i=1
while x<y:
#x<y
	i+=1
	x+=(0.1*x)
else:
#print(i)
	print(i)


The length of the sequence
"""
The program takes a sequence of non-negative integers, each number is written in a separate line. The sequence ends with a number 0. After reaching 0 the program should stop and print length of the sequence before it (not counting the final 0). The numbers following the number 0 should be omitted.
"""
# The program takes a sequence of non-negative integers, each number is written in a separate line:
x=1
i=0
while x>0:
#x>0
	x=int(input())
	i+=1
#print(i-1)
print(i-1)



The sum of the sequence
"""
Determine the sum of all elements in the sequence, ending with the number 0. 
"""
# Determine the sum of all elements in the sequence:
b=0
x=1
while x>0 or x<0:
#x>0, x<0
	x=int(input())
	b+=x
# print(b)

print(b)


The average of the sequence 
"""
Determine the average of all elements of the sequence ending with the number 0.
"""
# Determine the average of all elements:
b=0
x=1
i=0
while x>0 or x<0:
#x>0, x<0
# x=int(input())
	x=int(input())
	b+=x
	i+=1
# print(b/(i-1))
print(b/(i-1))



The maximum of the sequence 
"""
A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence.
"""
# Determine the largest element of the sequence:
x=1
b=0
while x>0:
#x>0
# x=int(input())
	x=int(input())
	if x>b:
#x>b
    	b=x
#print(b)
print(b)


The index of the maximum of a sequence 
"""
A sequence consists of integer numbers and ends with the number 0. Determine the index of the largest element of the sequence. If the highest element is not unique, print the index of the first of them.
"""
# Determine the index of the largest element of the sequence:
x=1
b=0
i=0
i1=0
while x>0:
#x>0
# x=int(input())
	x=int(input())
	i+=1
#If the highest element is not unique, print the index of the first of them
	if x>b:
#x>b
    	b=x
    	i1=i
# print(i1-1)
print(i1-1)



The number of even elements of the sequence 

"""
 Determine the number of even elements in the sequence ending with the number 0.

"""
# Determine the number of even elements in the sequence ending with the number 0:
x=1
b=0
while x>0:
#x>0
	x=int(input())
	if x%2==0:
#x%2=0
    	b+=1
# print(b-1)
print(b-1)


The number of elements that are greater than the previous one 
"""
A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are greater than their neighbours above.
"""
# Determine how many elements of this sequence are greater than their neighbours above:
x=1
b=0
k=0
while x>0:
#x>0
# x=int(input())
	x=int(input())
	z=x
	if k<x:
#k>x
    	k=x
    	b+=1
	else:
    	k=z
# print(b-1)
print(b-1)



The second maximum
"""
The sequence consists of pairwise distinct integer numbers and ends with the number 0. Determine the value of the second largest element in this sequence. It is guaranteed that the sequence has at least two elements.
"""
# Determine the value of the second largest element in this sequence:
x=1
b=0
z=0
# It is guaranteed that the sequence has at least two elements
while x>0:
#x>0
# x=int(input())
	x=int(input())
	if x>b:
#x>b
    	z=b
    	b=x
	elif x>z:
#x>z
    	z=x    	
# print(z)
print(z)

The number of elements equal to the maximum 
"""
 A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are equal to its largest element.
"""
# Determine how many elements of this sequence are equal to its largest element:
x=1
b=0
i=0
while x>0:
#x>0
# x=int(input())
	x=int(input())
	if b<x:
#b<x
    	b=x
    	i=0
	elif x==b:
#x==b
    	i+=1
# print(i+1)
print(i+1)





