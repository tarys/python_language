# -*- coding: utf-8 -*-

"""
    Домашня робота №8
    Тема: "2d arrays optimal storage"
    Студент: Козирєв Антон Юрійович
    Група: КМ - 62
"""

from math import fabs

#Task_1----------------------------------------------------#

"""
    Условие
    Дано нечетное число n.
    Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа).
    Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ.
    В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""

def create_triangular_matrix(size):
    return [['.']*count_of_element for count_of_element in range(size,0,-1) ]    
    
def set_element(triangular_matrix,i,j,value):
    if j<i:
        return    
    triangular_matrix[i][j-i]=value
  
def get_element(triangular_matrix,i,j):
    if j<i:
        return triangular_matrix[j][i-j]  # Inverse matrix value    
    return triangular_matrix[i][j-i]

def print_triangular_matrix(triangular_matrix):
    size=len(triangular_matrix[0])
    for i in range(size):
        for j in range(size):
            print(get_element(triangular_matrix,i,j),'',end='')
        print('')

def fill_triangular_matrix(triangular_matrix):
    counter = 0
    diagonal_counter = 0
    for row in triangular_matrix:
        for i in range(len(row)):
            if i == 0:
                row[i]='*'
            elif (len(triangular_matrix[0]) - 1) // 2 == i + counter:
                row[i]='*'
                counter+=1
            elif (len(triangular_matrix[0]) - 1) == i + 2 * diagonal_counter:
                row[i]='*'
                diagonal_counter+=1
            elif (len(triangular_matrix[0]) - 1) // 2 == len(row) - 1:
                row[i]='*'

def fill_matrix(triangular_matrix):
    size=len(triangular_matrix[0])
    for i in range(size):
        for j in range(size):
            if j>=i:
                set_element(triangular_matrix,i,j,j-i+1)

size=int(input())
matrix=create_triangular_matrix(size)
fill_triangular_matrix(matrix)
print_triangular_matrix(matrix)

#----------------------------------------------------------#

#Task_2----------------------------------------------------#

"""
    Условие
    Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
    На главной диагонали должны быть записаны числа 0.
    На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
"""

def create_triangular_matrix(size):
    return [[0]*count_of_element for count_of_element in range(size,0,-1) ]    
    
def set_element(triangular_matrix,i,j,value):
    if j<i:
        return    
    triangular_matrix[i][j-i]=value
  
def get_element(triangular_matrix,i,j):
    if j<i:
        return triangular_matrix[j][i-j]  # Inverse matrix value    
    return triangular_matrix[i][j-i]

def print_triangular_matrix(triangular_matrix):
    size=len(triangular_matrix[0])
    for i in range(size):
        for j in range(size):
            print(get_element(triangular_matrix,i,j),' ',end='')
        print('')

def fill_triangular_matrix(triangular_matrix):
    for row in triangular_matrix:
        for i in range(len(row)):
            row[i]=i


def fill_matrix(triangular_matrix):
    size=len(triangular_matrix[0])
    for i in range(size):
        for j in range(size):
            if j>=i:
                set_element(triangular_matrix,i,j,j-i+1)

size=int(input())
matrix=create_triangular_matrix(size)
fill_triangular_matrix(matrix)
print_triangular_matrix(matrix)

#----------------------------------------------------------#

#Task_3----------------------------------------------------#

"""
    Условие
    Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
    Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
    Числа, стоящие выше этой диагонали, равны 0.
    Числа, стоящие ниже этой диагонали, равны 2.
    Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""

def create_triangular_matrix(size):
    return [[0]*count_of_element for count_of_element in range(size,0,-1) ]    
    
def set_element(triangular_matrix,i,j,value):
    if j<i:
        return    
    triangular_matrix[i][j-i]=value
  
def get_element(triangular_matrix,i,j):
    if j<i:
        return triangular_matrix[j][i-j]  # Inverse matrix value    
    return triangular_matrix[i][j-i]

def print_triangular_matrix(triangular_matrix):
    size=len(triangular_matrix[0])
    for i in range(size):
        for j in range(size):
            print(get_element(triangular_matrix,j,i),' ',end='')
        print('')

def fill_triangular_matrix(triangular_matrix):
    for row in triangular_matrix:
        for i in range(len(row)):
            row[i]=i


def fill_matrix(triangular_matrix):
    size=len(triangular_matrix[0])
    for i in range(size):
        for j in range(size):
            if j>=i:
                set_element(triangular_matrix,j,i, len(triangular_matrix[j]))

size=int(input())
matrix=create_triangular_matrix(size)
fill_triangular_matrix(matrix)
print_triangular_matrix(matrix)

#----------------------------------------------------------#


