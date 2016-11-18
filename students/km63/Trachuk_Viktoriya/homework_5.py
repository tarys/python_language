#task1--------------------------------------------
"""
Given four real numbers: x1, y1, x2, y2. Write a function distance (x1, y1, x2, y2), calculates the distance between the point (x1, y1) and (x2, y2).
"""
import math
def distance(x1,x2,y1,y2):
	result=0
	result=math.sqrt((x2-x1)**2+(y2-y1)**2))
	return result
x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())
res=distance(x1,x2,y1,y2)
print(res)
#-------------------------------------------------
#task2--------------------------------------------
"""
Äàíî äåéñòâèòåëüíîå ïîëîæèòåëüíîå ÷èñëî a è öåëîe ÷èñëî n.

Âû÷èñëèòå an. Ðåøåíèå îôîðìèòå â âèäå ôóíêöèè power(a, n).

Ñòàíäàðòíîé ôóíêöèåé âîçâåäåíèÿ â ñòåïåíü ïîëüçîâàòüñÿ íåëüçÿ.
"""
def power(a,n):
	if n==1:
		result=a
	else:
		k=2
		while k<=n:
			result*=a
			k+=1
	return result
a=float(input())
n=int(input())
res=power(a,n)
print(res)
#-------------------------------------------------

#task3--------------------------------------------
"""
Äàíî äåéñòâèòåëüíîå ïîëîæèòåëüíîå ÷èñëî a è öåëîå íåîòðèöàòåëüíîå ÷èñëî n.
 Âû÷èñëèòå an íå èñïîëüçóÿ öèêëû, âîçâåäåíèå â ñòåïåíü ÷åðåç ** è ôóíêöèþ math.pow(),
 à èñïîëüçóÿ ðåêóððåíòíîå ñîîòíîøåíèå an=a*an-1.
"""
def power(a, n):

    if n == 0:

        return 1

    else:

        return a*power(a, n - 1)



a = float(input())

n = int(input())

res=power(a,n)
print(res)
#---------------------------------------------------

#task4----------------------------------------------
"""
Íàïèøèòå ôóíêöèþ fib(n),
 êîòîðàÿ ïî äàííîìó öåëîìó íåîòðèöàòåëüíîìó
 n âîçâðàùàåò n-e ÷èñëî Ôèáîíà÷÷è.
"""

def fib(n):

    if n == 1 or n == 2:

        return 1
    else:

        return fib(n - 1) + fib(n - 2)



n = int(input())
res=fib(n)

print(res)
#-----------------------------------------------------
