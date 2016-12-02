# task1------------------------------------------------------------
"""
��� �������� ����� n. �������� ��������� ������ �� n?n ���������, �������� ��� ��������� "." (������ ������� ������� �������� ������� �� ������ �������). ����� ��������� ��������� "*" ������� ������ �������, ������� ������� �������, ������� ��������� � �������� ���������. � ���������� ������� � ������� ������ ������������ ����������� ���������. �������� ���������� ������ �� �����, �������� �������� ������� ���������.
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
#������ ������
array = []
list_out = []
# input
#���� ������ � ��������
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


# task2------------------------------------------------------------
"""
���� ����� n. �������� ������ �������� n?n � ��������� ��� �� ���������� �������. �� ������� ��������� ������ ���� �������� ����� 0. �� ���� ����������, ����������� � �������, ����� 1. �� ��������� ���� ���������� ����� 2, � �.�.
"""


#default
generated_array = []
#������ ������
array_out = []
# input
#���� ������� ������ � ��������
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


# task3------------------------------------------------------------
"""
���� ����� n. �������� ������ �������� n?n � ��������� ��� �� ���������� �������:
����� �� ���������, ������ �� ������� �������� � ����� ������ ���� ����� 1.
�����, ������� ���� ���� ���������, ����� 0.
�����, ������� ���� ���� ���������, ����� 2.
���������� ������ �������� �� �����. ����� � ������ ���������� ����� ��������.
"""

#default
generated_array = []
#������ ������
array_out = []
# input
#���� ������� ������ � ��������
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