# -*- coding: utf-8 -*-

"""
    Додаткова домашня робота
    Тема: "I love Python"
    Студент: Козирєв Антон Юрійович
    Група: КМ - 62
"""

#Task: I love Python

#+-----+-----+
#|     |     |
#| *** | *** |
#|*****|*****|
#|*****|*****|
#|*****|*****|
#+-----+-----+
#|*****|*****|
#| ****|**** |
#|  ***|***  |
#|   **|**   |
#|    *|*    |
#+-----+-----+

#Main picture consist of 4 parts: 2 tops, 1 bottom, 1 reversed bottom

#Function #1: Creating field of ' ' (N x M)
def create_field(width, height):
    field = [[' '] * width for i in range(height)]
    return field
#

#Function #2: Creating top part (N / 2 x M / 2)
#Top: (if n = 10)
#+-----+
#|     |
#| *** |
#|*****|
#|*****|
#|*****|
#+-----+
def create_top(field, row, column, symbol):
    for i in range(row):
        for j in range(column):
            if (i >= 2) or ((i == 1) and (j != 0 and (j != column - 1))):
                field[i][j] = symbol
    return field
#

#Function #3: Creating bottom part (N / 2 x M / 2)
#Bottom: (if n = 10)
#+-----+
#|*****|
#| ****|
#|  ***|
#|   **|
#|    *|
#+-----+

def create_bottom(field, row, column, symbol):
    for i in range(row):
        for j in range(column):
            if (i == j) or (i - j) < 0:
                field[i][j] = symbol
    return field
#

#Function #4: Creating copy for using it in other functions 
def create_copy(field):
    copy_field = create_field(len(field), len(field))
    for i in range(len(field)):
        for j in range(len(field[i])):
            copy_field [i][j] = field [i][j]
    return copy_field
#

#Function #5 - 6: Flipping functions (by method of reversing lists)
def flip_h(field):
    reversed_field = create_copy(field)
    reversed_field.reverse()
    return reversed_field

def flip_v(field):
    reversed_field = create_copy(field)
    for row in reversed_field:
        row.reverse()
    return reversed_field
#

#Function #7 - 8: Union functions
def union_up_down(field_up, field_down):
    return field_up + field_down


def union_left_right(field_left, field_right):
    total_field = create_field(len(field_left * 2), len(field_left))
    for i in range(len(field_right)):
        total_field[i] = field_right[i] + field_left[i]
    return total_field
#

#Function #9 - 10: Turning functions (by method of transposing matrix)
def turn_right(field):
    copy_field = create_copy(field)
    turned_field = create_copy(field)
    for i in range(len(turned_field)):
        for j in range(len(turned_field)):
            turned_field[i][j] = copy_field[j][i]
    return turned_field

def turn_left(field):
    copy_field = create_copy(field)
    turned_field = create_copy(field)
    for i in range(len(turned_field)):
        for j in range(len(turned_field)):
            turned_field[i][j] = copy_field[len(turned_field) - j - 1][len(turned_field) - i - 1]
    return turned_field
#

#Function #11: 
def print_field(field):
    for Row in field:
        print(''.join([str(element) for element in Row]))



###Main block

#Input block

#Distance: N - even number () , N > 6
Distance = int(input("Enter size of heart: "))
Symbol = input("Enter symbol: ")
#
print('')

Empty_Field = create_field(Distance, Distance) #

Field = create_field(Distance, Distance)

Top = create_field(Distance // 2, Distance // 2)
Top = create_top(Top, Distance // 2, Distance // 2, Symbol)

Bottom = create_field(Distance // 2, Distance // 2)
Bottom = create_bottom(Bottom, Distance // 2, Distance // 2, Symbol)

Field = union_up_down(union_left_right(Top, Top), union_left_right(flip_v(Bottom), Bottom))

print_field(union_left_right(union_left_right(Empty_Field, Field), Empty_Field))

print_field(union_left_right(union_left_right(turn_left(Field), Empty_Field), turn_right(Field)))

print_field(union_left_right(union_left_right(Empty_Field, flip_h(Field)), Empty_Field))


#
print('')

I_love_python_string = (" " * Distance) + "I love Python"

print(I_love_python_string)

###



#Test block

#print_field(Field)

#print('')

#Field = turn_right(Field)

#print_field(Field)
