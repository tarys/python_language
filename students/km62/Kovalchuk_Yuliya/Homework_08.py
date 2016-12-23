#task1------------------------------------------------------------
"""
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "."(каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""

size=int(input())

def create_triangular_matrix(size):
    return [[0]*count_of_element for count_of_element in range(size,0,-1) ]    

def get_element(triangular_matrix,i,j):
    if i==j or i+j==size-1 or i==size//2 or j==size//2:
         return "*"
    else:
        return "."
    return triangular_matrix[i][j-i]    

def print_triangular_matrix(triangular_matrix):
    size=len(triangular_matrix[0])
    for i in range(size):
        for j in range(size):
            print(get_element(triangular_matrix,i,j),'',end='')
        print('')
        
matrix=create_triangular_matrix(size)
print_triangular_matrix(matrix)


#task2------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
Числа, стоящие выше этой диагонали, равны 0.
Числа, стоящие ниже этой диагонали, равны 2.
Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""


size=int(input())

def create_triangular_matrix(size):
    return [[0]*count_of_element for count_of_element in range(size,0,-1) ]    

def get_element(triangular_matrix,i,j):
  
    if i + j > size - 1:
        return 2
    if i + j == size - 1:
        return 1
        
    return triangular_matrix[i][j-i]    

def print_triangular_matrix(triangular_matrix):
    size=len(triangular_matrix[0])
    for i in range(size):
        for j in range(size):
            print(get_element(triangular_matrix,i,j),'',end='')
        print('')
        
matrix=create_triangular_matrix(size)
print_triangular_matrix(matrix)