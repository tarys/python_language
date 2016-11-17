#task1--------------------------
"""
Âûâåäèòå âñå ýëåìåíòû ñïèñêà ñ ÷åòíûìè èíäåêñàìè (òî åñòü A[0], A[2], A[4], ...).
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    data = []

    for i in range(0, len(elements), 2):

        data.append(elements[i])

    return data



def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))

#-----------------------------------------


#task2--------------------------
"""
Âûâåäèòå âñå ÷åòíûå ýëåìåíòû ñïèñêà.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    data = []

    for i in elements:

        if int(i) % 2 == 0:

            data.append(i)

    return data



def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))


#-----------------------------------------


#task3--------------------------
"""
Äàí ñïèñîê ÷èñåë. Âûâåäèòå âñå ýëåìåíòû ñïèñêà, êîòîðûå áîëüøå ïðåäûäóùåãî ýëåìåíòà.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    data = []

    for i in range(0, len(elements)):

        if i < len(elements)-1:

            if int(elements[i]) < int(elements[i + 1]):

                data.append(elements[i +1])

    return data



def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))
#-----------------------------------------


#task4--------------------------
"""
Äàí ñïèñîê ÷èñåë. Åñëè â íåì åñòü äâà ñîñåäíèõ ýëåìåíòà îäíîãî çíàêà, 
âûâåäèòå ýòè ÷èñëà. Åñëè ñîñåäíèõ ýëåìåíòîâ îäíîãî çíàêà íåò — íå âûâîäèòå íè÷åãî. 
Åñëè òàêèõ ïàð ñîñåäåé íåñêîëüêî — âûâåäèòå ïåðâóþ ïàðó.
"""
def input_data():

    data = input().split()

    return data


def operation_data(elements):

    data = []

    for i in range(0, len(elements)):

        if len(data) == 0:

            if i < len(elements)-1:

                if int(elements[i]) * int(elements[i + 1]) > 0:
                    data = [elements[i]]

                    data.append(elements[i + 1])

    return data


def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))









#-----------------------------------------


#task5--------------------------
"""
Äàí ñïèñîê ÷èñåë. Îïðåäåëèòå, ñêîëüêî â ýòîì ñïèñêå ýëåìåíòîâ, 
êîòîðûå áîëüøå äâóõ ñâîèõ ñîñåäåé, è âûâåäèòå êîëè÷åñòâî òàêèõ ýëåìåíòîâ. 
Êðàéíèå ýëåìåíòû ñïèñêà íèêîãäà íå ó÷èòûâàþòñÿ, ïîñêîëüêó ó íèõ íåäîñòàòî÷íî ñîñåäåé.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    counter = 0

    for i in range(1, len(elements)-1):

        if int(elements[i-1]) < int(elements[i]) > int(elements[i+1]):
            counter +=1

    return counter
 


def print_data(output_data):

    print (output_data)



print_data(operation_data(input_data()))

#-----------------------------------------


#task6--------------------------
"""
Äàí ñïèñîê ÷èñåë. Âûâåäèòå çíà÷åíèå íàèáîëüøåãî ýëåìåíòà â ñïèñêå, 
à çàòåì èíäåêñ ýòîãî ýëåìåíòà â ñïèñêå. Åñëè íàèáîëüøèõ ýëåìåíòîâ íåñêîëüêî, 
âûâåäèòå èíäåêñ ïåðâîãî èç íèõ.
"""
def input_data():
    data = input().split()
    return data
    
def operation_data(elements):

    data = []

    max_elements = elements[0]

    data = [max_elements]

    data.append(0)

    for i in range(1, len(elements)):

        if int(max_elements) < int(elements[i]):

            max_elements = elements[i]

            data = [max_elements]

            data.append(i)
       
    return data
    
def print_data(output_data):
    for i in output_data:
        print (i, end=' ')

print_data(operation_data(input_data()))

#-----------------------------------------
#task7--------------------------
"""
Ïåòÿ ïåðåø¸ë â äðóãóþ øêîëó. 
Íà óðîêå ôèçêóëüòóðû åìó ïîíàäîáèëîñü îïðåäåëèòü ñâî¸ ìåñòî â ñòðîþ. 
Ïîìîãèòå åìó ýòî ñäåëàòü.
Ïðîãðàììà ïîëó÷àåò íà âõîä íåâîçðàñòàþùóþ ïîñëåäîâàòåëüíîñòü íàòóðàëüíûõ ÷èñåë, 
îçíà÷àþùèõ ðîñò êàæäîãî ÷åëîâåêà â ñòðîþ. Ïîñëå ýòîãî ââîäèòñÿ ÷èñëî X – ðîñò Ïåòè. 
Âñå ÷èñëà âî âõîäíûõ äàííûõ íàòóðàëüíûå è íå ïðåâûøàþò 200.

Âûâåäèòå íîìåð, ïîä êîòîðûì Ïåòÿ äîëæåí âñòàòü â ñòðîé. 
Åñëè â ñòðîþ åñòü ëþäè ñ îäèíàêîâûì ðîñòîì, òàêèì æå, êàê ó Ïåòè, 
òî îí äîëæåí âñòàòü ïîñëå íèõ.
"""
def input_data():

    data = input().split()

    return data


def operation_data(elements):

    hight = int(input())

    position = 0

    while position < len(elements) and int(elements[position]) >= hight:

        position += 1

    return position


def print_data(output_data):

        print (output_data + 1)



print_data(operation_data(input_data()))

#-----------------------------------------
#task8--------------------------
"""
Äàí ñïèñîê, óïîðÿäî÷åííûé ïî íåóáûâàíèþ ýëåìåíòîâ â íåì. 
Îïðåäåëèòå, ñêîëüêî â íåì ðàçëè÷íûõ ýëåìåíòîâ.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    counter = 0

    for i in range(0, len(elements)-1):

        if int(elements[i]) != int(elements[i + 1]):

            counter +=1

    return counter



def print_data(output_data):

        print (output_data + 1)



print_data(operation_data(input_data()))

#-----------------------------------------
#task9--------------------------
"""
Ïåðåñòàâüòå ñîñåäíèå ýëåìåíòû ñïèñêà (A[0] c A[1], A[2] c A[3] è ò. ä.). 
Åñëè ýëåìåíòîâ íå÷åòíîå ÷èñëî, òî ïîñëåäíèé ýëåìåíò îñòàåòñÿ íà ñâîåì ìåñòå.
"""
def input_data():

    data = input().split()

    return data

    

def operation_data(elements):

    for i in range(0, len(elements)//2):

	elements[i*2], elements[i*2 + 1] = elements[i*2 + 1], elements[i*2]
    return element


def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))

#-----------------------------------------
#task10--------------------------
"""
Â ñïèñêå âñå ýëåìåíòû ðàçëè÷íû. 
Ïîìåíÿéòå ìåñòàìè ìèíèìàëüíûé è ìàêñèìàëüíûé ýëåìåíò ýòîãî ñïèñêà.
"""
def input_data():

    data = input().split()

    return data



def operation_data(elements):

    max_element = elements[0]

    min_element = elements[0]

    index_min = 0

    index_max = 0

    for i in range(0, len(elements)):

        if  int(min_element) > int(elements[i]):

            min_element = elements[i]

            index_min = i

        if  int(max_element) < int(elements[i]):

            max_element = elements[i]

            index_max = i
    
    elements[index_min], elements[index_max] = elements[index_max], elements[index_min]    
    return elements



def print_data(output_data):

    for i in output_data:

        print (i, end=' ')



print_data(operation_data(input_data()))


#-----------------------------------------
#task11--------------------------
"""
Äàí ñïèñîê èç ÷èñåë è èíäåêñ ýëåìåíòà â ñïèñêå k. 
Óäàëèòå èç ñïèñêà ýëåìåíò ñ èíäåêñîì k, 
ñäâèíóâ âëåâî âñå ýëåìåíòû, ñòîÿùèå ïðàâåå ýëåìåíòà ñ èíäåêñîì k.
Ïðîãðàììà ïîëó÷àåò íà âõîä ñïèñîê, çàòåì ÷èñëî k. 
Ïðîãðàììà ñäâèãàåò âñå ýëåìåíòû, à ïîñëå ýòîãî óäàëÿåò ïîñëåäíèé ýëåìåíò 
ñïèñêà ïðè ïîìîùè ìåòîäà pop() áåç ïàðàìåòðîâ.

Ïðîãðàììà äîëæíà îñóùåñòâëÿòü ñäâèã íåïîñðåäñòâåííî â ñïèñêå, 
à íå äåëàòü ýòî ïðè âûâîäå ýëåìåíòîâ. Òàêæå íåëüçÿ èñïîëüçîâàòü äîïîëíèòåëüíûé ñïèñîê. 
Òàêæå íå ñëåäóåò èñïîëüçîâàòü ìåòîä pop(k) ñ ïàðàìåòðîì.
"""
def input_data():

    data = input().split()

    return data


def operation_data(elements):

    k = int(input())

    for i in range(k, len(elements) - 1):

        elements[i] = elements[i + 1]

    elements.pop()

    return elements
    

def print_data(output_data):

    for i in output_data:
        print (i, end=' ')
        


print_data(operation_data(input_data()))


#-----------------------------------------
#task12--------------------------
"""
Äàí ñïèñîê öåëûõ ÷èñåë, ÷èñëî k è çíà÷åíèå C. 
Íåîáõîäèìî âñòàâèòü â ñïèñîê íà ïîçèöèþ ñ èíäåêñîì k ýëåìåíò, 
ðàâíûé C, ñäâèíóâ âñå ýëåìåíòû, èìåâøèå èíäåêñ íå ìåíåå k, âïðàâî.
Ïîñêîëüêî ïðè ýòîì êîëè÷åñòâî ýëåìåíòîâ â ñïèñêå óâåëè÷èâàåòñÿ, 
ïîñëå ñ÷èòûâàíèÿ ñïèñêà â åãî êîíåö íóæíî áóäåò äîáàâèòü íîâûé ýëåìåíò, 
èñïîëüçóÿ ìåòîä append.

Âñòàâêó íåîáõîäèìî îñóùåñòâëÿòü óæå â ñ÷èòàííîì ñïèñêå, íå äåëàÿ ýòîãî 
ïðè âûâîäå è íå ñîçäàâàÿ äîïîëíèòåëüíîãî ñïèñêà.
"""
def input_data():

    data = input().split()

    return data

    

def operation_data(elements):

    data = input().split()

    elements.append(data[1])

    for i in range(len(elements) - 1, int(data[0]), -1):

        elements[i] = elements[i - 1]

    elements[int(data[0])] = int(data[1])

    return elements

    

def print_data(output_data):
   for i in output_data:

        print (i, end=' ')
  
      

print_data(operation_data(input_data()))


#-----------------------------------------
#task13--------------------------
"""
Äàí ñïèñîê ÷èñåë. Ïîñ÷èòàéòå, ñêîëüêî â íåì ïàð ýëåìåíòîâ, 
ðàâíûõ äðóã äðóãó. Ñ÷èòàåòñÿ, ÷òî ëþáûå äâà ýëåìåíòà, 
ðàâíûå äðóã äðóãó îáðàçóþò îäíó ïàðó, êîòîðóþ íåîáõîäèìî ïîñ÷èòàòü.
"""
def input_data(): 
    data = input().split() 
    return data 
def operation_data(elem): 
    count=0 
    for i in elem: 
        for j in elem: 
            if i==j: 
                count+=1 
        count-=1 
    return(count // 2) 
def print_data(output_data): 
    print(output_data) 
print_data(operation_data(input_data()))

#-----------------------------------------


#task14--------------------------
"""
Äàí ñïèñîê. Âûâåäèòå òå åãî ýëåìåíòû, 
êîòîðûå âñòðå÷àþòñÿ â ñïèñêå òîëüêî îäèí ðàç. 
Ýëåìåíòû íóæíî âûâîäèòü â òîì ïîðÿäêå, 
â êîòîðîì îíè âñòðå÷àþòñÿ â ñïèñêå.
"""
#-----------------------------------------

#task15--------------------------
"""
N êåãëåé âûñòàâèëè â îäèí ðÿä, çàíóìåðîâàâ èõ ñëåâà íàïðàâî ÷èñëàìè îò 1 äî N. 
Çàòåì ïî ýòîìó ðÿäó áðîñèëè K øàðîâ, ïðè ýòîì i-é øàð ñáèë âñå êåãëè ñ 
íîìåðàìè îò li äî ri âêëþ÷èòåëüíî. Îïðåäåëèòå, êàêèå êåãëè îñòàëèñü 
ñòîÿòü íà ìåñòå.
Ïðîãðàììà ïîëó÷àåò íà âõîä êîëè÷åñòâî êåãëåé N è êîëè÷åñòâî áðîñêîâ K. 
Äàëåå èäåò K ïàð ÷èñåë li, ri, ïðè ýòîì 1? li? ri? N.

Ïðîãðàììà äîëæíà âûâåñòè ïîñëåäîâàòåëüíîñòü èç N ñèìâîëîâ, ãäå j-é ñèìâîë 
åñòü “I”, åñëè j-ÿ êåãëÿ îñòàëàñü ñòîÿòü, èëè “.”, åñëè j-ÿ êåãëÿ áûëà ñáèòà.
"""

s = input().split(' ')
 outs = ["I" for i in range(int(s[0]))]
 print(outs)
 for i in range(int(s[1])):
     ns = input().split(' ')
     for f in range(int(ns[0])-1, int(ns[1])):
         outs[f] = "."
 for i in outs:
     print(i, end='')

#-----------------------------------------
#task16--------------------------
"""
Óñëîâèå
Èçâåñòíî, ÷òî íà äîñêå 8?8 ìîæíî ðàññòàâèòü 8 ôåðçåé òàê, ÷òîáû îíè íå 
áèëè äðóã äðóãà. Âàì äàíà ðàññòàíîâêà 8 ôåðçåé íà äîñêå, îïðåäåëèòå, 
åñòü ëè ñðåäè íèõ ïàðà áüþùèõ äðóã äðóãà.
Ïðîãðàììà ïîëó÷àåò íà âõîä âîñåìü ïàð ÷èñåë, 
êàæäîå ÷èñëî îò 1 äî 8 — êîîðäèíàòû 8 ôåðçåé. 
Åñëè ôåðçè íå áüþò äðóã äðóãà, âûâåäèòå ñëîâî NO, èíà÷å âûâåäèòå YES.
"""
#-----------------------------------------

