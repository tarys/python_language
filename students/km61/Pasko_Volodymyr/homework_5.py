# task 1 --------------------------------------------------------------------------
'''
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние
между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
'''
# program calculating the distance between tho points using the function
import math


def distance(x1, y1, x2, y2):
    abscissa_distance = abs(x1 - x2)  # distance in the abscissa axis
    ordinate_distance = abs(y1 - y2)  # distance in the ordinate axis
    # According to the above measured data it can be easily calculated the distance between two points
    two_points_distance = math.sqrt(abscissa_distance ** 2 + ordinate_distance ** 2)
    return print(two_points_distance)


cordinate_1 = float(input('input the coordinate: '))
cordinate_2 = float(input('input the coordinate: '))
cordinate_3 = float(input('input the coordinate: '))
cordinate_4 = float(input('input the coordinate: '))
distance(cordinate_1, cordinate_2, cordinate_3, cordinate_4)


# ----------------------------------------------------------------------------------

# task 2---------------------------------------------------------------------------
'''
Дано действительное положительное число a и целоe число n.
Вычислите an. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
'''
# program calculating the any power from the number using written function
def power(base_power, power):
    result = 1
    for i in range(1, abs(power) + 1):
        result = base_power ** i
    if power > 0:
        return result
    else:
        return 1 / result


input_base_power = float(input('Enter the base of the power: '))
input_power = int(input('Enter the power: '))
print(power(input_base_power, input_power))


# ----------------------------------------------------------------------------------

# task 3---------------------------------------------------------------------------
'''
Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, возведение
 в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.
'''
# program printing the power of the number using the function with recursion
def power(base_number, power_number):
    if power_number == 0:
        return 1
    return base_number * power(base_number, power_number - 1)


input_base_number = float(input('Enter the base of the number: '))
input_power_number = int(input('Enter the power of the number: '))
print(power(input_base_number, input_power_number))


# ----------------------------------------------------------------------------------

# task 4---------------------------------------------------------------------------
'''
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой задаче
нельзя использовать циклы — используйте рекурсию.
'''
# program printing the number from the fibonacci's sequence according to its index

def fib(sequence_number):
    if sequence_number < 0:
        return 0
    elif sequence_number == 1 or sequence_number == 2:
        return 1
    return fib(sequence_number - 1) + fib(sequence_number - 2)


input_sequence_number = int(input("Enter the index from the sequence: "))
print(fib(input_sequence_number))

# ----------------------------------------------------------------------------------
