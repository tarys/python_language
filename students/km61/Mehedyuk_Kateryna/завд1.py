# your code goes heredef distance(x1, y1, x2, y2):
   res = (x2 - x1) ** 2 + (y2 - y1) ** 2
   return res ** 0.5
    
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
 
print(distance(x1, y1, x2, y2))
