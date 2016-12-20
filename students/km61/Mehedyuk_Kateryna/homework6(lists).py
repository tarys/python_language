#task1
Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
def input_even_elements(List, n):
        if(n >= len(List)):
            return
        print(List[n])
     
        
        input_even_elements(List, n + 2)
StartIndex = 0
List = input().split()
input_even_elements(List, StartIndex)
#task2
Выведите все четные элементы списка. При этом используйте цикл for, перебирающий элементы списка, а не их индексы!
H = input().split()
for i in H:
     if int(i) % 2 == 0:
         print(end =' ' +i)
#task3
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
numbers = input().split()
for i in range(len(numbers)):
     if int(numbers[i])>int(numbers[i-1]) and i!=0:
         print(numbers[i])
#task4
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
A = [int(number) for number in input().split()]
for number in range(1, len(A)):
    if A[number] * A[number - 1] >= 0:
         print(A[number - 1])
         print(A[number])
         break
#task5
Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
A = [int(number) for number in input().split()]
sum = 0
 
for number in range(1, len(A) - 1):
     if A[number] > A[number - 1] and A[number] > A[number + 1]:
         sum += 1
print(sum)
#task6
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.
A = [int(number) for number in input().split()]
i = 0
max = A[0]
for number in range(1, len(A)):
     if A[number] > max:
         max = A[number]
         i = number
print(max, i)
#task7
Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.

Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как у Пети, то он должен встать после них.
A = [int(number) for number in input().split()]
height = int(input())
i = 1
 
for number in range(0, len(A)):
     if A[number] < height:
         i = number + 1
         break
else:
     i = len(A) + 1
print(i)
#task8
Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
def others(i, counter):
     if i == len(list_numbers):
         return counter
     if list_numbers[i] != list_numbers[i - 1]:
         return others(i + 1, counter + 1)
     return others(i + 1, counter)
 
 
list_numbers = input().split()
print(others(1, 1))
#task9
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте.
A = [int(m) for m in input().split()]
 
for m in range(0, len(A) - 1, 2):
     A[m], A[m + 1] = A[m + 1], A[m]
 
for m in A:
     print(m, end=' ')
#task10
В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
A = [int(num) for num in input().split()]
max = 0
min = 0
 
for num in range(len(A)):
     if A[num] > A[max]:
         max = num
     if A[num] < A[min]:
         min = num
A[min], A[max] = A[max], A[min]
 
for num in A:
    print(num, end = ' ')
#task11
A = [int(num) for num in input().split()]
k = int(input())
A.pop(k)
for elem in A:
 print(elem, end=' ')
 #task12
 A = [int(num) for num in input().split()]
k, c = [int(num) for num in input().split()]
temp = c
 
for num_2 in range(k, len(A)):
     A[num_2], temp = temp, A[num_2]
A.append(temp)
 
for num in A:
 print(num, end = ' ')
 #task13
 Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
 Ar = [int(num) for num in input().split()]
i = 0
 
for num in range(len(Ar)):
    for num_2 in range(num + 1, len(Ar)):
         if Ar[num] == Ar[num_2]:
             i += 1
print(i)
#task14
A = [int(num) for num in input().split()]
 
for num in range(len(A)):
     for num_2 in range(len(A)):
         if A[num] == A[num_2] and num != num_2:
             break
     else:
         print(A[num])
#task15
def change(index, index_2):
     if index > index_2:
         return
     res[index] = '.'
     change(index + 1, index_2)
 
 
def game(i):
     if i == int(N_and_K[1]):
         return
     n = [int(element) - 1 for element in input().split()]
     change(n[0], n[1])
     game(i + 1)
#task16
Q = [[int(num) for num in input().split()] for num_2 in range(8)]
beat = False
 
for num in range(len(Q)):
     x1 = Q[num][0]
     y1 = Q[num][1]
     for num_2 in range(len(Q)):
         if num == num_2:
             continue
         x2 = Q[num_2][0]
         y2 = Q[num_2][1]
         if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
             beat = True
             break
if beat:
     print('YES')
else:
     print('NO')
