# Assignment on Module 2
# Assignment 02 : Understanding Advance Data Structures, Function and Comparison

#========================================================================================
# problem 01. Write a Python program that takes a list of numbers as input,
# removes duplicates using a suitable list method, 
# and returns a dictionary containing the original list, 
# the unique values, and their count. 
# Use a function with parameters and a return statement to perform this task.

# solution : 
def my_func(my_list):
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)

    count = len(unique_list)

    my_dict = {
        "original_list":my_list,
        "unique_list":unique_list,
        "count":count
    }
    return my_dict

user_input = input("Enter numbers separated by spaces : ")
original_list = [int(x) for x in user_input.split()]

print(my_func(original_list))
#===================================================================================





#===================================================================================
# 2. Create a function that accepts two sets as parameters 
# and returns their union, intersection, and difference. 
# Use keyword arguments with default parameter values 
# so the function can work even if one of the sets is not provided by the user. 
# Display the results clearly.

def calculate_set_operation(set_1 ={1,3,4,5}, set_2={2,6,8,9}):
    union_result = set_1 | set_2
    intersection_result = set_1 & set_2
    diff_result = set_1 - set_2
    
    result = {
        "union_result":union_result,
        "intersection_result":intersection_result,
        "difference_result":diff_result
    }
    print(result)
    return result

calculate_set_operation()

my_set_a = {12,4,53,6,21,3,32}
my_set_b = {23,21,53,76,21,32}
calculate_set_operation(set_1=my_set_a, set_2=my_set_b)
#===================================================================================





#===================================================================================
# 3. Define a tuple containing mixed data types, 
# unpack its values into separate variables, 
# and compare them with another tuple using comparison operators. 
# Then, explain in code comments the main difference between lists 
# and tuples in Python.

# solution
my_tuple_1 = ("Shakib", 75, 6.3)
my_tuple_2 = ("Joe Root", 66, 6.6)

name, jersey_no, height = my_tuple_1
print(name, jersey_no, height)
name, jersey_no, height = my_tuple_2
print(name, jersey_no, height)

# compare 
print(my_tuple_1>my_tuple_2)        # true - 75 > 66

# diff between list and tuple 
    #mutability
# 1.    list is mutable , 
#       tuple is immutable .

    #syntax
# 2.    list declare a square bracket []
#       tuple declare a parentheses ()

    #performance
# 3.    list is slow
#       tuple is fast

    #memory
# 4.    list list contain more memory
#       tuple contain less memory

    #security
# 5.    list less security
#       tuple more security
#===================================================================================