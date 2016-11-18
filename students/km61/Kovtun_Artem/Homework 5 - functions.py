#(1)
#Function that counts lenght of segment by coordinates of its ends

def distance(first_end_x,first_end_y,second_end_x,second_end_y):
    lenght = ((first_end_x - second_end_x) ** 2 + (first_end_y - second_end_y) ** 2) ** 0.5
    return lenght

#input
first_end_x = float(input("Enter first coordinate of first end - "))
first_end_y = float(input("Enter second coordinate of first end - "))

second_end_x = float(input("Enter first coordinate of second end - "))
second_end_y = float(input("Enter second coordinate of second end - "))

#output
print(distance(first_end_x,first_end_y,second_end_x,second_end_y))






#(2)
#Function that counts number in power
#Both inputs by user

def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

#main
user_number = float(input("Enter real number - "))
power = int(input("Enter integer(power) - "))

#output
print(power(user_number,power))






#(3)
#Function that counts number in power
#Both inputs by user

def power(a, n):
    res = 1
    for i in range(n):
        res *= a
    return res


#main
user_number = float(input("Enter real number - "))
power_of_number = int(input("Enter integer(power) - "))

#output
print(power(user_number,power_of_number))






#(4)
#Function that prints Fibbonacci number which stands on n position
#number "n" inputs by user

def fibb(sequence_number):
    if sequence_number < 0:
         return 0
    elif sequence_number == 1 or sequence_number == 2:
        return 1
    else:
        return fibb(sequence_number-1) + fibb(sequence_number-2)


#input
user_number = int(input("Enter integer - "))

#output
print(fibb(user_number))