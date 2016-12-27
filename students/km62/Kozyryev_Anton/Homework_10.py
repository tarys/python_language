# -*- coding: utf-8 -*-

"""
    Домашня робота №10
    Тема: "DICT"
    Студент: Козирєв Антон Юрійович
    Група: КМ - 62
"""

#Task_1----------------------------------------------------#

"""
    Условие
    В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
    Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
"""

def get_all_elements(Dict):
    Answer_dict = []
    for key, value in Dict.items():
        Answer_dict.append(key)
        Answer_dict.append(value)
    return ' '.join(Answer_dict)

Words = input().split()
Values_of_Words = dict(zip(Words, ["-1"]*len(Words)))
values = []
Answer = ""

for word in Words:
    if (Values_of_Words[word] == ["-1"]):
        Values_of_Words[word] == ["0"]
    else:
        Current_element = int(Values_of_Words.get(word))
        Values_of_Words[word]  = str(Current_element + 1)

    
Answer = get_all_elements(Values_of_Words)

print(Answer)

#----------------------------------------------------------#

#Task_2----------------------------------------------------#

"""
    Условие
    Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
    Все слова в словаре различны. Для слова из словаря, записанного в последней строке, определите его синоним.
"""

Sum_of_synonims = int(input())

Definitions = []
Synonims = []

for i in range(Sum_of_synonims):
    Input_string = input().split()
    Definitions.append(Input_string[0])
    Synonims.append(Input_string[1])

Dictionary = dict(zip(Definitions, Synonims))

Searching_word = input()

for key in Dictionary.keys():
    if Searching_word == key:
        print(Dictionary[key])
    elif Searching_word == Dictionary[key]:
        print(key)
        

#----------------------------------------------------------#

#Task_3----------------------------------------------------#

"""
    Условие
    Как известно, в США президент выбирается не прямым голосованием, а путем двухуровневого голосования.
    Сначала проводятся выборы в каждом штате и определяется победитель выборов в данном штате.
    Затем проводятся государственные выборы: на этих выборах каждый штат имеет определенное число голосов — число выборщиков от этого штата.
    На практике, все выборщики от штата голосуют в соответствии с результами голосования внутри штата, то есть на заключительной стадии выборов в голосовании участвуют штаты, имеющие различное число голосов.
    В первой строке дано количество записей. Далее, каждая запись содержит фамилию кандидата и число голосов, отданных за него в одном из штатов.
    Подведите итоги выборов: для каждого из участника голосования определите число отданных за него голосов. Участников нужно выводить в алфавитном порядке.
"""

Sum_of_notes = int(input())

Notes_lastname = []
Notes_votes = []

for i in range(Sum_of_notes):
    Input_string = input().split()
    Notes_lastname.append(Input_string[0])
    Notes_votes.append(Input_string[1])

Data_dict = dict(zip(Notes_lastname, Notes_votes))

for key in Data_dict.keys():
    Data_dict[key] = "0"

for i in range(len(Notes_lastname)):
    if Notes_lastname[i] in Data_dict.keys():
        Current_value = int(Data_dict[Notes_lastname[i]])
        Data_dict[Notes_lastname[i]] = str(Current_value + int(Notes_votes[i]))
        
for candidat in sorted(Data_dict.keys()):
    print(candidat, Data_dict[candidat])

#----------------------------------------------------------#

#Task_4----------------------------------------------------#

"""
    Условие
    Дан текст: в первой строке задано число строк, далее идут сами строки.
    Выведите слово, которое в этом тексте встречается чаще всего.
    Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
"""

Sum_of_notes = int(input())

Notes_lastname = []
Notes_votes = []
Words = []
Final_data = []
Dictionary = dict()

for i in range(Sum_of_notes):
    Input_string = input().split()
    for Word in Input_string:
       Words.append(Word) 
    
for word in Words:
    if word in Dictionary:
        current_value = int(Dictionary[word])
        Dictionary[word] = str(current_value + 1)
    else:
        Dictionary[word] = "0"
        
Max_repeat = int(max(Dictionary.values()))

for note in Dictionary:
    if int(Dictionary[note]) == Max_repeat:
        Final_data.append(note) 
        
Final_data = sorted(Final_data)
print(Final_data[0])

#----------------------------------------------------------#

#Task_5----------------------------------------------------#

"""
    Условие
    В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам.
    Для каждого файла известно, с какими действиями можно к нему обращаться:
        запись W,
        чтение R,
        запуск X.
    В первой строке содержится число N — количество файлов содержащихся в данной файловой системе.
    В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами.
    Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл.
    К одному и тому же файлу может быть применено любое колличество запросов.
    Вам требуется восстановить контроль над правами доступа к файлам (ваша программа для каждого запроса должна будет возвращать OK если над файлом выполняется допустимая операция, или же Access denied, если операция недопустима.
"""

Files_of_data_sum = int(input())

Files_nameing = []
Files_data = []

for i in range(Files_of_data_sum):
    Temporary_data = input().split()
    Files_nameing.append(Temporary_data[0])
    Files_data.append(Temporary_data[1:])

for element in Files_data:
    for i in range(len(element)):
        if element[i] == "W":
            element[i] = "write"
        if element[i] == "R":
            element[i] = "read"
        if element[i] == "X":
            element[i] = "execute"
            
All_files_and_configs = dict(zip(Files_nameing, Files_data))

Commands_sum = int(input())
for i in range(Commands_sum):
    current_comand = input().split()
    current_todo = current_comand[0]
    current_file = current_comand[1]
    if (current_todo in All_files_and_configs[current_file]):
        print("OK")
    else:
        print("Access denied")

#----------------------------------------------------------#
