#task1------------------------------------------------------------
'''
	По данному натуральному n вычислите значение n!.
	Пользоваться математической библиотекой math в этой задаче запрещено.
'''
n = int(input(""))
result = 1
for i in range(1, n+1):
	result *= i
print(result)
#-----------------------------------------------------------------

#task2------------------------------------------------------------
'''
	По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!.
	В решении этой задачи можно использовать только один цикл.
	Пользоваться математической библиотекой math в этой задаче запрещено.
'''
n = int(input(""))
result = 1
suma = 0
for i in range(1,n+1):
	result *= i
	suma += result
print(suma)
#-----------------------------------------------------------------

#task3------------------------------------------------------------
'''
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. 
Подсчитайте количество нулей среди введенных чисел и выведите это количество. 
Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
'''
n = int(input())
k = 0
for i in range(1, n+1):
	x = int(input())
	if x == 0:
		k  += 1
print(k)
#-----------------------------------------------------------------

#task4------------------------------------------------------------
'''
По данному натуральному n ? 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
'''
n = int(input())
string = ""
for i in range(1, n+1):
	str += string(i)
	print(string)
#-----------------------------------------------------------------
