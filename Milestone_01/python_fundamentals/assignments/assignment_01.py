# Assignment on Module 01

# Assignment : 01  Loops and smart Operations

# =======================================================================
# Problem 01 : Write a Python program that takes a number as input and 
# checks whether it is even or odd
# Solution : 
num = int(input("enter a (integer) number to check it is odd or even : ")) 

if num == 0:
    print("this is zero")
elif num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
# ========================================================================




# ========================================================================
# Problem 02 : write a Python program that takes two numbers and 
# an operator (+,-,/,*,%) and performs the calculation.

number_1 = int(input("Enter an Integer number (n1) : "))
number_2 = int(input("Enter an Integer number (n1) : "))
operator = input(f"Enter an operator (+,-,*,/,%) to calculate {number_1} and {number_2} : ")

if operator == "+":
    result = number_1 + number_2 # sum of 2 number
    print(f"result : {number_1} + {number_2} = {result}")
elif operator == "-":
    result = number_1 - number_2 # subtraction of 2 number
    print(f"result : {number_1} - {number_2} = {result}")
elif operator == "*":
    result = number_1 * number_2 # multiplication of 2 number   
    print(f"result : {number_1} * {number_2} = {result}")
elif operator == "/":
    result = number_1 / number_2 # division of 2 number 
    print(f"result : {number_1} / {number_2} = {result}")
elif operator == "%":
    result = number_1 % number_2 # division of number as a remainder
    print(f"result : {number_1} % {number_2} = {result}")
# =====================================================================





# =====================================================================

# problem 03 : write a python program using a for loop that 
# calculates the sum of even number between 1 to 100

sum_of_even = 0
for i in range(1,101):
    if i % 2 == 0:
        sum_of_even += i

print(sum_of_even)


# ======================================================================







# # method 2
# range_start = int(input("enter start index : "))
# range_stop = int(input("enter stop index : "))
# sum_of_even = 0
# for i in range(range_start, range_stop+1):
#     if i % 2 == 0:
#         sum_of_even += i
# print(f"sum of even number between {range_start} to {range_stop} = {sum_of_even}")


# # method 03
# range_start = int(input("enter start index : "))
# range_stop = int(input("enter stop index : "))
# sum_of_odd = 0
# for i in range(range_start, range_stop+1):
#     if i % 2 == 1:
#         sum_of_odd += i
# print(f"sum of odd number between {range_start} to {range_stop} = {sum_of_odd}")