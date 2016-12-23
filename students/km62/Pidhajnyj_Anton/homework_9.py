#task1------------------------------------------------------------
"""
Дан список чисел. Определите, сколько в нем встречается различных чисел.

Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""



print(len(set(input()))-1)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""



print(len(set(input().split()) & set(input().split())))

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.

Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
"""



li=(list(set(input().split()) & set(input().split())))
li.sort(key=int)
for elem in li:
    print(elem,end=' ')

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
"""



li=input().split()
a=set()
for elem in li:
    if elem in a:
        print('YES')
    else:
        print('NO')
        a.add(elem)


#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету.
Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
Для этого они занумеровали все цвета случайными числами от 0 до 108. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.

В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори. В следующих N строках заданы номера цветов кубиков Ани.
В последних M строках номера цветов Бори.

Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; номера цветов кубиков, которые есть только у Ани и номера цветов кубиков,
которые есть только у Бори. Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.
"""


n,m=input().split()
n,m=int(n),int(m)
li_n,li_m=[int(input()) for i in range(n)],[int(input()) for i in range(m)]
li_1=list(set(li_n) & set(li_m))
li_1.sort()
print(len(li_1))
for el in li_1:
    print(el,end=' ')
print()
li_2=list(set(li_n)-set(li_m))
li_2.sort()
print(len(li_2))
for el in li_2:
    print(el,end=' ')
print()
li_3=list((set(li_m)-set(li_n)))
li_3.sort()
print(len(li_3))
for el in li_3:
    print(el,end=' ')


#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.

Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
"""


n=int(input())
arr=[input().split() for x in range(n)]
A=set()
for row in arr:
    for el in row:
        A.add(el)
print(len(A))


#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае. После нескольких заданныъх вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.

В первой строке задано n - максимальное число, которое мог загадать Август. Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом) и ответ Августа на этот вопрос.

Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
"""



n=int(input())
s=''
save=s
yes={str(x) for x in range(1,n+1)}
no=set()
while s!='HELP':
    s=input()
    if (s!='YES') and (s!='NO') and (s!='HELP'):
        save=s.split()
    elif s=='YES':
        yes&=set(save)
    elif s=='NO':
        no|=set(save)
li=list(yes-no)
li.sort()
for elem in li:
    if int(elem)<=n:
        print(elem,end=' ')
    else:
        break


#-----------------------------------------------------------------


#task8------------------------------------------------------------
"""
Август и Беатриса продолжают играть в игру, но Август начал жульничать.
На каждый из вопросов Беатрисы он выбирает такой вариант ответа YES или NO,
чтобы множество возможных задуманных чисел оставалось как можно больше.
Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2,
то Август ответит NO, а если Беатриса спросит про 1, 2, 3, то Август ответит YES.

Если же Бетриса в своем вопросе перечисляет ровно половину из задуманных чисел,
то Август из вредности всегда отвечает NO. Наконец, Август при ответе учитывает
все предыдущие вопросы Беатрисы и свои ответы на них, то есть множество возможных
задуманных чисел уменьшается.

Первая строка содержит наибольшее число, которое мог загадать Август.
Каждая следующая строка содержит очередной вопрос Беатрисы: набор чисел, разделенных пробелами.
Последняя строка входных данных содержит одно слово HELP.

Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос.
После этого выведите через пробел, в порядке возрастания, все числа,
которые мог загадать Август после ответа на все вопросы Беатрисы.
"""



count=int(input())
numbers=set()
numbers_=set()

for i in range(count):
    numbers.add(str(i+1))
    
while True:
    string=input()
    if string=='HELP':
        break
    else:
        numbers_=set(string.split())
    if len(numbers-numbers_)>=len(numbers&numbers_):
        print('NO')
        numbers=numbers-numbers_
    else:
        print('YES')
        numbers=numbers&numbers_

for elements in sorted(numbers, key=int):
    print(elements, end=' ')

#-----------------------------------------------------------------


#task9------------------------------------------------------------
"""
Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков.
Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.

В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков,
которое он знает, а затем - названия языков, по одному в строке.

В первой строке выведите количество языков, которые знаю все школьники. Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков. Языки нужно выводить в лексикографическом порядке, по одному на строке.
"""



n=int(input())
arr=[]
for i in range(n):
    m=int(input())
    arr.append({input() for x in range(m)})
li_1=set()
li_2=set()
li_1|=arr[0]
for elem in arr:
    li_1&=elem
    li_2|=elem
print(len(li_1))
li_1=list(li_1)
li_1.sort()
for el in li_1:
    print(el)
print(len(li_2))
li_2=list(li_2)
li_2.sort()
for el in li_2:
    print(el)


#-----------------------------------------------------------------


#task10-----------------------------------------------------------
"""
Политическая жизнь одной страны очень оживленная.
В стране действует K политических партий, каждая из которых регулярно объявляет национальную забастовку.
Дни, когда хотя бы одна из партий объявляет забастовку,
при условии, что это не суббота или воскресенье (когда и так никто не работает),
наносят большой ущерб экономике страны.

i-я партия объявляет забастовки строго каждые b_i дней, начиная с дня с номером a_i.
То есть i-я партия объявляет забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д.
Если в какой-то день несколько партий объявляет забастовку,
то это считается одной общенациональной забастовкой.

В календаре страны N дней, пронумерованных, начиная с единицы.
Первый день года является понедельником, шестой и седьмой дни года — выходные, неделя состоит из семи дней.

В первой строке даны числа N и K. Далее идет K строк, описывающие графики проведения забастовок.
i-я строка содержит числа a_i и b_i. Вам нужно определить число забастовок, произошедших в этой стране в течении года.
"""



strikes=[]
strikes_=set()

days , parties = input().split()
days=int(days)
parties=int(parties)
for i in range(parties):
    a_i,b_i=input().split()
    for j in range(int(a_i),days+1,int(b_i)):
        if (j%6!=0) and (j%7!=0):
            strikes.append(j)
strikes_=set(strikes)
print(len(strikes_))

#-----------------------------------------------------------------


