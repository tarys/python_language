# 4.цикл for
#task7----------------------------------------------------------— 
""" 
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.

""" 
fac=1
n = int(input())

for i in range (1,n+1,1):
fac = fac*i

print(fac)

#---------------------------------------------------------------— 
#task8----------------------------------------------------------— 
""" 
По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено.
""" 
fac=1
sum=0
n = int(input())

for i in range(1,n+1):
fac=fac*i
sum=sum+fac

print(sum)

#---------------------------------------------------------------— 

#task9----------------------------------------------------------— 
""" 
Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
""" 
n = int(input())
kol = 0

for i in range(n):
    num = int(input())
    if num==0: 
        kol+=1 
print(kol)

#---------------------------------------------------------------— 

#task10---------------------------------------------------------— 
""" 
По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
""" 
n = int(input())
for i in range(n):
    for j in range(1,i+2):
        print(j,end='')
    print()


#---------------------------------------------------------------— 
