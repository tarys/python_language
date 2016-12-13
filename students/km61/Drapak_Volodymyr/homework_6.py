#task1------------------------------------------------------------
"""
Виведіть всі елементи списку з парними індексами (тобто A [0], A [2], A [4], ...).
"""



#write your answer here...
"""
# Program outputs all even elements of list

# functions/procedures
# procedure prints all elements with recursion; n - counter
def input_even_elements(List, n):

    # exit
    if(n >= len(List)):
        return

    # body
    print(List[n])

    # call
    input_even_elements(List, n + 2)

# default
StartIndex = 0

# input
List = input().split()

# body
input_even_elements(List, StartIndex)

"""

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Виведіть всі парні елементи списку.
"""



#write your answer here...
"""
# Program outputs all even elements of list

# functions/procedures
# procedure prints all even elements of list; n - counter
def printEvenElements(List, n):

    # exit
    if(n == len(List)):
        return

    # body
    if(List[n]%2 == 0):
        print(List[n])

    # call
    printEvenElements(List, n + 1)

# procedure converts list to list of integers
def strListToIntList(List):
    for i in range(len(List)):
        List[i] = int(List[i])

# input
List = input().split()

# body
strListToIntList(List)
printEvenElements(List, 0)
"""

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Дано список чисел. Виведіть всі елементи списку, які більше попереднього елемента.
"""



#write your answer here...
"""
# Program outputs elements of list that are more than previous elements

# functions/procedures
# procedure prints specified elements
def printBiggerElements(List, n):

    # exit
    if(n >= len(List)):
        return

    # body
    if(List[n] > List[n - 1]):
        print(List[n])

    # call
    printBiggerElements(List, n + 1)

def strListToIntList(List):
    for i in range(len(List)):
        List[i] = int(List[i])

# input
List = input().split()

# body
strListToIntList(List)
printBiggerElements(List, 1)
"""

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Дано список чисел. Якщо в ньому є два сусідні елементи одного знака, виведіть ці числа.
Якщо сусідніх елементів одного знака немає - не виводьте нічого. Якщо таких пар сусідів кілька - виведіть першу пару.
"""



#write your answer here...
"""
# Program outputs elements of list that have the same sign with their neighbor elements

# functions/procedures
# function sign
def sign(n):
    number_sign = 0
    if(n < 0):
        number_sign = -1
    if(n > 0):
        number_sign = 1
    return number_sign

# procedure prints specified elements
def printEqualSignElements(List, n):

    # exit
    if(n >= len(List)):
        return

    # body/exit
    if(sign(List[n]) == sign(List[n - 1])):
        print(List[n - 1], List[n])
        return

    # call
    printEqualSignElements(List, n + 1)

def strListToIntList(List):
    for i in range(len(List)):
        List[i] = int(List[i])

# input
List = input().split()

# body
strListToIntList(List)
printEqualSignElements(List, 1)
"""

#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Дано список чисел. Визначте, скільки в цьому списку елементів, які більше двох своїх сусідів, і виведіть кількість таких елементів.
Крайні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
"""



#write your answer here...
"""
# Program outputs count of elements of list that are more than their neighbor elements

# functions/procedures
# procedure prints specified elements
def printBiggerElementsCount(List, n, count):

    # exit
    if(n + 1 >= len(List)):
        print(count)
        return

    # body
    if(List[n - 1] < List[n] > List[n + 1]):
        count += 1

    # call
    printBiggerElementsCount(List, n + 1, count)

def strListToIntList(List):
    for i in range(len(List)):
        List[i] = int(List[i])

# input
List = input().split()

# body
strListToIntList(List)
printBiggerElementsCount(List, 1, 0)
"""

#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Дано список чисел. Виведіть значення найбільшого елементу в списку, а потім індекс цього елемента в списку.
Якщо найбільших елементів декілька, виведіть індекс першого з них.
"""



#write your answer here...
"""
# Program outputs first max element of list and his index

# functions/procedures
# procedure prints max and his index
def printBiggestElement(List, n, max_value, index):

    # exit
    if(n >= len(List)):
        print(max_value)
        print(index)
        return

    # body
    if(max_value < List[n]):
        max_value = List[n]
        index = n

    # call
    printBiggestElement(List, n + 1, max_value, index)

def strListToIntList(List):
    for i in range(len(List)):
        List[i] = int(List[i])

# input
List = input().split()

# body
strListToIntList(List)
printBiggestElement(List, 1, List[0], 0)
"""

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Петя перейшов в іншу школу. На уроці фізкультури йому знадобилося визначити своє місце в строю.
Допоможіть йому це зробити.Програма отримує на вхід незростаючу послідовність натуральних чисел, що означають ріст кожної людини в строю.
Після цього вводиться число X - ріст Петі. Всі числа у вхідних даних натуральні і не перевищують 200.
Виведіть номер, під яким Петя повинен стати в шеренгу.
Якщо в строю є люди з однаковим зростом, таким же, як у Петі, то він повинен стати після них.
"""



#write your answer here...
"""
# Program outputs number of place where Petya should stay in line with his height

# functions/procedures
# procedure prints specified number
def printPosNumber(List, n, Petya_height):

    # exit
    if(n >= len(List) or Petya_height > List[n]):
        print(n + 1)
        return

    # call
    printPosNumber(List, n + 1, Petya_height)

def strListToIntList(List):
    for i in range(len(List)):
        List[i] = int(List[i])

# input
List = input().split()
Petya_height = int(input())

# body
strListToIntList(List)
printPosNumber(List, 0, Petya_height)
"""

#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Дано список, упорядкований по неспаданню елементів в ньому. Визначте, скільки в ньому різних елементів.
"""



#write your answer here...
"""
# Program outputs count of unique elements of list

# functions/procedures
# procedure prints specified number
def printUniqueElementsCount(List, n, count):

    # exit
    if(n >= len(List)):
        print(count)
        return

    # body
    if(List[n] != List[n - 1]):
        count += 1

    # call
    printUniqueElementsCount(List, n + 1, count)

# input
List = input().split()

# body
printUniqueElementsCount(List, 1, 1)
"""

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Переставте сусідні елементи списку (A [0] з A [1], A [2] з A [3] і т. Д.).
Якщо елементів непарне число, то останній елемент залишається на своєму місці.
"""



#write your answer here...
"""
# Program outputs list with swapped neighbor elements

# functions/procedures
# procedure prints specified list
def printSwappedList(List, n):

    # exit
    if(n + 1 >= len(List)):
        print(' '.join(List))
        return

    # body
    temp = List[n]
    List[n] = List[n + 1]
    List[n + 1] = temp

    # call
    printSwappedList(List, n + 2)

# input
List = input().split()

# body
printSwappedList(List, 0)
"""

#-----------------------------------------------------------------


#task10------------------------------------------------------------
"""
У списку всі елементи різні. Поміняйте місцями мінімальний і максимальний елементи цього списку.
"""



#write your answer here...
"""
# Program outputs list with swapped minimal and maximal elements

# functions/procedures
# procedure converts list of integers to list of strings
def intListToStrList(List):
    for i in range(len(List)):
        List[i] = str(List[i])

# procedure prints specified list
def printSwappedList(List, n, min_value, max_value, index_min, index_max):

    # exit
    if(n >= len(List)):
        temp = List[index_min]
        List[index_min] = List[index_max]
        List[index_max] = temp

        intListToStrList(List)
        print(' '.join(List))
        return

    # body
    if(min_value > List[n]):
        min_value = List[n]
        index_min = n
    elif(max_value < List[n]):
        max_value = List[n]
        index_max = n

    # call
    printSwappedList(List, n + 1, min_value, max_value, index_min, index_max)

def strListToIntList(List):
    for i in range(len(List)):
        List[i] = int(List[i])

# input
List = input().split()

# body
strListToIntList(List)
printSwappedList(List, 1, List[0], List[0], 0, 0)
"""

#-----------------------------------------------------------------


#task11------------------------------------------------------------
"""
Дано список з чисел і індекс елемента в списку k.
Видаліть зі списку елемент з індексом k, зсунувши вліво всі елементи, що стоять правіше елемента з індексом k.
Програма отримує на вхід список, потім число k.
Програма зсуває усі елементи, а після цього видаляє останній елемент списку за допомогою методу pop () без параметрів.

Програма повинна здійснювати зрушення безпосередньо в списку, а не робити це при виведенні елементів.
Також не можна використовувати додатковий список. Також не слід використовувати метод pop (k) з параметром.
"""



#write your answer here...
"""
# Program removes element with index k from list and outputs this list

# functions/procedures
# procedure removes element with index k and prints the list
def printListDeletingElement(List, n):

    # exit
    if(n + 1 >= len(List)):
        List.pop()
        print(' '.join(List))
        return

    # body
    temp = List[n]
    List[n] = List[n + 1]
    List[n + 1] = temp

    # call
    printListDeletingElement(List, n + 1)

# input
List = input().split()

# body
printListDeletingElement(List, int(input()))

"""

#-----------------------------------------------------------------


#task12------------------------------------------------------------
"""
Дано список цілих чисел, число k і значення C.
Необхідно вставити в список на позицію з індексом k елемент, рівний C, зсунувши усі елементи, що мали індекс не менше k, вправо.
Поскільки при цьому кількість елементів у списку збільшується, після зчитування списку в його кінець потрібно буде додати новий елемент,
 використовуючи метод append.

Вставку необхідно здійснювати вже в зчитаному списку, не роблячи цього при виведенні і не створюючи додаткового списку.
"""



#write your answer here...
"""
# Program puts element C with index k to list and outputs the list

# functions/procedures

def intListToStrList(List):
    for i in range(len(List)):
        List[i] = str(List[i])

# procedure does specified in condition actions
def printPuttingElementList(List, n, curr_index):

    # exit
    if(curr_index <= n):
        intListToStrList(List)
        print(' '.join(List))
        return

    # body
    temp = List[curr_index]
    List[curr_index] = List[curr_index - 1]
    List[curr_index - 1] = temp

    # call
    printPuttingElementList(List, n, curr_index - 1)

def strListToIntList(List):
    for i in range(len(List)):
        List[i] = int(List[i])

# input
List = input().split()
two_numbers = input().split()

# body
strListToIntList(List)
strListToIntList(two_numbers)
k = two_numbers[0]
c = two_numbers[1]
List.append(c)
printPuttingElementList(List, k, len(List) - 1)
"""

#-----------------------------------------------------------------


#task13------------------------------------------------------------
"""
Дано список чисел. Порахуйте, скільки в ньому пар елементів, рівних один одному.
Вважається, що будь-які два елементи, рівні один одному утворюють одну пару, яку необхідно порахувати.
"""



#write your answer here...
"""
# Program counts pairs of equal elements in list and outputs this number

# functions/procedures
# function counts equal pairs with variable element
def EqualElementsCount(List, n, element):

    # exit
    if(n >= len(List)):
        return 0

    # body
    count = 0
    if(List[n] == element):
        count += 1

    # call/return
    return count + EqualElementsCount(List, n + 1, element)

# function counts pairs of equal elements
def EqualElementsPairsCount(List, n):

    # exit
    if(n >= len(List)):
        return 0

    # call/body
    count = EqualElementsPairsCount(List, n + 1) + EqualElementsCount(List, n + 1, List[n])

    # return
    return count

def intListToStrList(List):
    for i in range(len(List)):
        List[i] = int(List[i])

# input
List = input().split()

# body
intListToStrList(List)
print(EqualElementsPairsCount(List, 0))
"""

#-----------------------------------------------------------------


#task14------------------------------------------------------------
"""
Дано список. Виведіть ті його елементи, які зустрічаються в списку тільки один раз.
Елементи потрібно виводити в тому порядку, в якому вони зустрічаються в списку.
"""



#write your answer here...
"""
# Program outputs unique elements of list

# functions/procedures
# function revises whether element is unique
def isElementUnique(List, n, element, curr_elem_index):

    # exit
    if(n >= len(List)):
        return True

    # body
    is_unique = None
    if(curr_elem_index != n and List[n] == element):
        is_unique = False
    else:
        # call
        is_unique = isElementUnique(List, n + 1, element, curr_elem_index)

    # return
    return is_unique

# procedure prints unique elements
def printUniqueElements(List, n):

    # exit
    if(n >= len(List)):
        return

    # body
    if(isElementUnique(List, 0, List[n], n)):
        print(List[n])

    # call
    printUniqueElements(List, n + 1)

# input
List = input().split()

# body
printUniqueElements(List, 0)
"""

#-----------------------------------------------------------------


#task15------------------------------------------------------------
"""
N кеглів виставили в один ряд, занумеровавши їх зліва направо числами від 1 до N.
Потім з цього ряду кинули K куль, при цьому i-а куля збила усі кеглі з номерами від l (i) до г (i) включно.
Визначте, які кеглі залишилися стояти на місці.
Програма отримує на вхід кількість кеглів N і кількість кидків K. Далі йде K пар чисел l (i), г (i), при цьому 1≤ l (i) ≤ г (i) ≤ N.

Програма повинна вивести послідовність з N символів, де j-й символ є "I", якщо j-я кегля залишилася стояти,
 або ".", якщо j-я кегля була збита.
"""



#write your answer here...
"""
# Program models bowling

# functions/procedures
# procedure sets points on positions of pins which were knocked by ball
def gameModeling(pins_list, l, r, n):

    # exit
    if(n >= r):
        return

    # body
    pins_list[n] = "."

    # call
    gameModeling(pins_list, l, r, n + 1)

def strListToIntList(List, n):

    # exit
    if(n >= len(List)):
        return

    # body
    List[n] = int(List[n])

    # call
    strListToIntList(List, n + 1)

# procedure realizes input of numbers l and r instead cycle and calls procedure for modelling of game
def inputNumbers(pins_list, K, n):

    # exit
    if(n >= K):
        return

    # body
    two_numbers = input().split()
    strListToIntList(two_numbers, 0)
    l = two_numbers[0]
    r = two_numbers[1]
    gameModeling(pins_list, l, r, l - 1)

    # call
    inputNumbers(pins_list, K, n + 1)

# procedure creates list of "I" (pins)
def pinsListCreation(pins_list, N, n):

    # exit
    if(n >= N):
        return

    # body
    pins_list.append("I")

    # call
    pinsListCreation(pins_list, N, n + 1)

# input
two_numbers = input().split()
strListToIntList(two_numbers, 0)
N = two_numbers[0]
K = two_numbers[1]
pins_list = []
pinsListCreation(pins_list, N, 0)
inputNumbers(pins_list, K, 0)

# body
print(''.join(pins_list))
"""

#-----------------------------------------------------------------


#task16------------------------------------------------------------
"""
Відомо, що на дошці 8 × 8 можна розставити 8 ферзів так, щоб вони не били один одного.
Вам дана розстановка 8 ферзів на дошці, визначте, чи є серед них пара ферзів, які б'ють один одного.
Програма отримує на вхід вісім пар чисел, кожне число від 1 до 8 - координати 8 ферзів.
Якщо ферзі не б'ють один одного, виведіть слово NO, інакше виведіть YES.
"""



#write your answer here...
"""
# Program revises whether pair of queens those shot each other or not

# functions/procedures
# function returns True if cell is under rook shot and False otherwise
def is_under_rook_shot(x_of_rook, y_of_rook, x_of_cell, y_of_cell):
    Truth = False
    if(x_of_rook == x_of_cell or y_of_rook == y_of_cell):
        Truth = True
    return Truth

# function returns True if cell is under bishop shot and False otherwise
def is_under_bishop_shot(x_of_bishop, y_of_bishop, x_of_cell, y_of_cell):
    Truth = False
    if(abs(x_of_bishop - x_of_cell) == abs(y_of_bishop - y_of_cell)):
        Truth = True
    return Truth

# function returns True if cell is under queen shot and False otherwise
def is_under_queen_shot(x_of_queen, y_of_queen, x_of_cell, y_of_cell):
    Truth = False
    if(is_under_bishop_shot(x_of_queen, y_of_queen, x_of_cell, y_of_cell) or
       is_under_rook_shot(x_of_queen, y_of_queen, x_of_cell, y_of_cell)):
        Truth = True
    return Truth

# function returns True if there exists specified pair of queens
def is_some_queen_under_another_queen_shot(queens_number, x_list, y_list):
    # function returns the same value as outer function
    def revisingQueens(x_list, y_list, current_queen_index, queens_number, n):

        # exit
        if(n >= queens_number):
            return False

        # body
        is_shot = None
        if is_under_queen_shot(x_list[current_queen_index],
        y_list[current_queen_index], x_list[n], y_list[n]):
            is_shot = True
        else:
            # call
            is_shot = (revisingQueens(x_list, y_list, current_queen_index, queens_number, n + 1) or
            revisingQueens(x_list, y_list, n, queens_number, n + 1))
        return is_shot

    Truth = revisingQueens(x_list, y_list, 0, queens_number, 1)
    return Truth

def strListToIntList(List, n):

    # exit
    if(n >= len(List)):
        return

    # body
    List[n] = int(List[n])

    # call
    strListToIntList(List, n + 1)

# procedure realizes input of coordinates of queens
def inputCoordinates(x_list, y_list, N, n):

    # exit
    if(n >= N):
        return

    # body
    two_numbers = input().split()
    strListToIntList(two_numbers, 0)
    x_list[n] = two_numbers[0]
    y_list[n] = two_numbers[1]

    # call
    inputCoordinates(x_list, y_list, N, n + 1)

# procedure creates list with N zeros
def zeroListCreation(List, N):

    # exit
    if(N <= 0):
        return

    # body
    List.append(0)

    # call
    zeroListCreation(List, N - 1)

# default
QueensNumber = 8
x_list = []
y_list = []
zeroListCreation(x_list, QueensNumber)
zeroListCreation(y_list, QueensNumber)

# input
inputCoordinates(x_list, y_list, QueensNumber, 0)

# body
if(is_some_queen_under_another_queen_shot(QueensNumber, x_list, y_list)):
    print("YES")
else:
    print("NO")
"""

#-----------------------------------------------------------------