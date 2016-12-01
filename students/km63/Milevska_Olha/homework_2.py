#task1------------------------------------------------------------

"""
Minimum of two numbers

"""
a=input( “Enter integer number A”) 
b=input( “Enter integer number B”)
if a<b:
    print(a)
else:
    print(b)

#----------------------------------------------------------------
#task2------------------------------------------------------------
"""
Sign function
"""
x = float(input(“Enter  real number X”))
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

#----------------------------------------------------------------
#task3------------------------------------------------------------
"""
Minimum of three numbers
"""
a=input( “Enter integer number A”)
b=input(“Enter integer number  B” )
c=input(“Enter integer number  C” )
if a < b:
    if a < c:
        #a < b, a < c
        print(a)
if b<a:
    if b < c:
      #b < a, b < c
    print(b)
if c < a:
    if c < b:
        # c < a, c < b
      print(c)

#----------------------------------------------------------------
#task4------------------------------------------------------------
"""
Leap year
"""
a=int(input( “Enter  the year”))
if (a//4):
    print("LEAP")
else:
    print ("COMMON")

#----------------------------------------------------------------
#task5------------------------------------------------------------
"""
 Equal numbers
"""
a=int(input(“Enter first integer number” ))
b=int(input( “Enter second integer number”))
c=int(input(“Enter third integer number” ))
if a == b:
    if a==C:
        if c == b:
            #a == b, a == c, c == b
            print(3)
if a != b:
    if a == c:
        if b != c:
            #a != B, a == c, b != c
            print(2)
if a != b:
    if a !=c:
        if b != c:
           #a != b, a != b, b != c  
            print(0)

#----------------------------------------------------------------
#task6------------------------------------------------------------
"""
Rook move
"""
x1 = int(input(“Enter  integer number of column where rook is located”))   
x2 = int(input(“Enter integer number of row where rook is located”))		
y1 = int(input(“Enter integer number of column where rook must be moved”))	
y2 = int(input(“Enter integer number of row where rook must be moved”))
if x1==y1 or x2==y2:
    print("YES")
else:
    print("NO") 

#----------------------------------------------------------------
#task7------------------------------------------------------------
"""
Chess board
"""
x1 = int(input(“Enter integer number of the first column”))
x2 = int(input(“Enter integer number of the first row”))
y1 = int(input(“Enter integer number of the second column”))
y2 = int(input(“Enter integer number of the second row”))
if (x1+x2)%2==0 and (y1+y2)%2==0:
    print("YES")
elif (x1+x2)%2!=0 and (y1+y2)%2!=0:
    print("YES")
else:
    print("NO")

#----------------------------------------------------------------
#task8------------------------------------------------------------
"""
King move
"""
x1 = int(input(“Enter integer number of the first column”))
x2 = int(input(“Enter integer number of the first row”))
y1 = int(input(“Enter integer number of the second column”))
y2 = int(input(“Enter integer number of the second row”))
if -1<=(x1-y1)<=1 and -1<=(x2-y2)<=1:
    print("YES")
else:
    print("NO")

#----------------------------------------------------------------
#task9------------------------------------------------------------
"""
Bishop move
"""
x1 = int(input(“Enter integer number of the first column”))
x2 = int(input(“Enter integer number of the first row”))
y1 = int(input(“Enter integer number of the second column”))
y2 = int(input(“Enter integer number of the second row”))
if (x1/y1)==(x2/y2):
    print("YES")
elif (x1+x2)==(y1+y2):
    print("YES")
else:
    print("NO")

#----------------------------------------------------------------
#task10------------------------------------------------------------
"""
Queen move
"""
x1 = int(input(“Enter integer number of the first column”))
x2 = int(input(“Enter integer number of the first row”))
y1 = int(input(“Enter integer number of the second column”))
y2 = int(input(“Enter integer number of the second row”))
if x1==y1 or x2==y2:
    print("YES")
elif (x1/y1)==(x2/y2):
    print("YES")
elif  (x1+x2)==(y1+y2)  or (x1-x2)==(y1-y2):
    print("YES")   
else:
    print("NO")

#----------------------------------------------------------------
#task11------------------------------------------------------------
"""
Knight move
"""
x1 = int(input(“Enter integer number of the first column”))
x2 = int(input(“Enter integer number of the first row”))
y1 = int(input(“Enter integer number of the second column”))
y2 = int(input(“Enter integer number of the second row”))
if abs(x1-y1)==2 and abs(x2-y2)==1:
    print("YES")
elif abs(x1-y1)==1 and abs(x2-y2)==2:
    print("YES")
else:
    print("NO")

#----------------------------------------------------------------
#task12------------------------------------------------------------
"""
Chocolate bar
"""
n = int(input(“Enter length of the bar”))
n = int(input(“Enter width of the bar”))
n = int(input(“Enter quantity of bars into which choco bar must be splitted”))
if n*m-k==a or n*m-k==b and n*m>k and k!=1:
    print('YES')
elif (n*m-k)%2==0 and n*m>k and k!=1:
     print('YES')
else:
    print('NO')

#----------------------------------------------------------------
