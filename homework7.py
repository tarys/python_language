#task1------------------------------------------------------------
 size = input().split()
 m=int(size[0])
 n=int(size[1])
 matrix = []
 for i in range(m):
     row = input().split()
     for i in range(len(row)):
         row[i] = int(row[i])
   matrix.append(row)
 for i in range(m):
     for j in range(n):
         if (i==0) and (j==0):
             x=i
             y=j
             max = matrix[0][0]
         elif matrix[i][j] > max:
             x=i
             y=j
             max=matrix[i][j]
 +print (x, y, end=' ')
 +#task2------------------------------------------------------------
 size=int(input())
 matrix = []
 matrix = ['.'] * size
 for i in range(size):
     matrix[i] = ['.'] * size
 for i in range(size):
     for j in range(size):
         if i==j:
             matrix[i][j] = '*' 
         elif (size-j) == (i+1):
             matrix[i][j] = '*'
         if size//2 == j:
             matrix[i][j] = '*'
       if size//2 == i:
             matrix[i][j] = '*'
 for i in range(size):
     for j in range(size):
         print(matrix[i][j], end=' ')
     print() 
 #task_3------------------------------------------------------------
 raw = input().split()
 n = int(raw[0]); m = int(raw[1])
 mas = [(".*."[1-(i%2):2-(i%2)+1])*(m//2) for i in range(1,n+1)]
 for row in mas:
     print(' '.join(row))
 
 +#task4------------------------------------------------------------
 
size = int(input())
 matrix = [0] * size
 for i in range(size):
     matrix[i] = [0] * size
 for k in range(1, size):
     for i in range(size-k):
         for j in range(size-k):
            if i == j:
                 matrix[i][j+k] = k
                 matrix[i+k][j] = k
 for i in range(size):
     for j in range(size):
         print(matrix[i][j], end=' ')
     print()
 +#task5------------------------------------------------------------------------------------------------------------------------
 size = int(input())
 matrix = [0] * size
 for i in range(size):
     matrix[i] = [0] * (size-i-1) + [1] + [2] * i
 for i in range(size):
     for j in range(size):
         print(matrix[i][j], end=' ')
     print() 
 #task6------------------------------------------------------------
 def swap_colums(matrix, i, j):
     for raw in range(len(matrix)):
         matrix[raw][i], matrix[raw][j] = matrix[raw][j], matrix[raw][i]
     return matrix
 raw = input().split(); n=int(raw[0]); m=int(raw[1])
 matrix = [input().split() for i in range(n)]
 raw = input().split(); 
c1=int(raw[0]); 
c2=int(raw[1])
 matrix = swap_colums(matrix, c1, c2)
 for raw in matrix:
     print(' '.join([str(i) for i in raw]))