# task1------------------------------------------------------------
"""
Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""

#default
element_buffer = 0
#Список вывода
array_main = []
list_out = []
# input
#Ввод списка и разбивка
array_size= input().split()
# main
list = input().split()
element_buffer = int(list[0])
list_out = '0 '+'0'
array_main.append(list)
for max in range(len(list)):
    if int(array_main[0][max]) > element_buffer:
        element_buffer = int(array_main[0][max])
        list_out = '0 '+ str(max)
for n in range (1,int(array_size[0]),1):
    list = input().split()
    array_main.append(list)
    for max in range(len(list)):
        if int(array_main[n][max]) > element_buffer:
            element_buffer = int(array_main[n][max])
            list_out = str(n) + ' ' + str(max)
# result
print(list_out)

# -----------------------------------------------------------------


# task2------------------------------------------------------------
"""
ано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""

def create_array(size):
    list_main = []
    [list_main.append([]) for i in range(size)]
    for i in range(size):
        [list_main[i].append('.') for r in range(size)]
    for n in range(size):
       list_main[n][n]='*'
    return list_main
def array_up_down(array):
    copy_array = []
    for i in range (len(array)-1, -1, -1):
        copy_array.append(array[i])
    return copy_array
def array_vertical_flip(array):
    copy_array = []
    for i in range(len(array)):
        position = []
        for n in range(len(array[i])):
            position.append(array[i][n])
        copy_array.append(position)
    for i in range(len(array)):
        copy_array[i].reverse()
    return copy_array
def merge_up_down (array_up, array_down):
    copy_array = []
    string_element = '*'*len(array_up)
    copy_array+=array_up
    list_string = []
    for n in range(len(string_element)):
        list_string+=string_element[n] 
    copy_array.append(list_string)
    copy_array+=array_down
    return copy_array
def merge_vertical (array_left, array_right):
    copy_array = []
    for i in range(len(array_left)):
        copy_array.append([])
    for i in range(len(array_left)):
        copy_array[i].append(array_left[i])
        copy_array[i].append(' * ')
        copy_array[i].append(array_right[i])
    return copy_array
#default
#Список вывода
array = []
list_out = []
# input
#Ввод списка и разбивка
size = int(input())
size = int((size-1)/2)
# main
array=create_array(size)
left_part_array = merge_up_down (array, array_up_down(array))
full_array = merge_vertical (left_part_array , array_vertical_flip(left_part_array))
# result
for i in range(len(full_array)):
    text = ''
    for n in range(len(full_array[i])):
        text += ' '.join(full_array[i][n])
    print(text)

# -----------------------------------------------------------------


# task3------------------------------------------------------------
"""
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
"""


#default
generated_array = []
#Список вывода
list_out = []
# input
#Ввод размера списка и разбивка
array_size = input().split()
# main
for height in range(int(array_size[0])):
    generated_array = []
    copy_array = []
    if height % 2 == 0:
        for index in range(int(array_size[1])):
            if index % 2 == 0:
                generated_array.append('.')
            else:
                generated_array.append('*')
            copy_array.append(generated_array[index])
    else:
        for index in range(int(array_size[1])):
            if index % 2 == 0:
                generated_array.append('*')
            else:
                generated_array.append('.')
            copy_array.append(generated_array[index])
    list_out.append(copy_array)
# result
for i in range(len(list_out)):
    print(' '.join(list_out[i]))

# -----------------------------------------------------------------


# task4------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
"""


#default
generated_array = []
#Список вывода
array_out = []
# input
#Ввод размера списка и разбивка
height = int(input())
# main
generate_skeleton = []
[generate_skeleton.append(abs(i)) for i in range(-height+1,height)]
for h in range(height):
    copy_array=[]
    [copy_array.append(str(generate_skeleton[i])) for i in range(len(generate_skeleton))]
    for left_erase in range (height-1-h):
        copy_array.pop(0)
    for left_erase in range (h):
        copy_array.pop()
    array_out.append(copy_array)
# result
for i in range(len(array_out)):
    print(' '.join(array_out[i]))

# -----------------------------------------------------------------


# task5------------------------------------------------------------
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
"""

#default
generated_array = []
#Список вывода
array_out = []
# input
#Ввод размера списка и разбивка
height = int(input())
# main
generate_skeleton = []
[generate_skeleton.append('0') for i in range(height-1)]
generate_skeleton.append('1')
[generate_skeleton.append('2') for i in range(height-1)]
for h in range(height):
    copy_array=[]
    [copy_array.append(str(generate_skeleton[i])) for i in range(len(generate_skeleton))]
    for left_erase in range (h):
        copy_array.pop(0)
    for left_erase in range (height-1-h):
        copy_array.pop()
    array_out.append(copy_array)
# result
for i in range(len(array_out)):
    print(' '.join(array_out[i]))

# -----------------------------------------------------------------


# task6------------------------------------------------------------
"""
Условие
Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.

Решение оформите в виде функции swap_columns(a, i, j).
"""


#default
#Список вывода
array_out = []
# input
#Ввод размера списка и разбивка
array_size = input().split()
for height in range(int(array_size[0])):
    array_out.append(input().split())
array_swap = input().split()
for i in range(len(array_out)):
    array_out[i][int(array_swap[0])],array_out[i][int(array_swap[1])] = array_out[i][int(array_swap[1])],array_out[i][int(array_swap[0])]
#result
for i in range(len(array_out)):
    print(' '.join(array_out[i]))

# -----------------------------------------------------------------