import sys
# Class 02: Advanced Data Structures and Comparison
# Topics : tuple . unpacking , comparing , list vs tuple , sets(union/ intersection/difference)

# 1. Tuples : a tuple is an ordered collection just like a list ---but it cannot be change after it is created. it
# syntax : tuple_name = (value_separated_by_comma)

my_tuple = (10,20,30,'rashed','Jesmin', True, 3.1416)
print(my_tuple)

cgpa = (3.97, 3.17, 3.57, 3.75, 3.23)
print(cgpa)
print(type(cgpa))       #class tuple

person = ("Naim Hasan", 25, "Shariatpur")
print(person)
print(person[2])
print(f"Name : {person[0]}, age : {person[1]}, city : {person[2]}")


colors = ('red', 'green', 'blue', 'aqua', 'magenta','green','red', 'yellow','magenta','aqua', 'green-yellow', 'orange', 'violet', 'blue-violet')
print(colors)
print(len(colors))
print(colors.count("green"))
print(colors.index('orange'))


# index and slicing ---same as list
print(colors[0])
print(colors[0:5])
print(colors[::-1])
print(colors[:5:-1])
print(colors[1::2])     #print odd index 1 to last
print(colors[::2])      #print even index 0 to last



# tuples are immutable 
rgb_colors = ('red', 'green', 'blue')
print(rgb_colors)
# rgb_colors[0] = 'white'     # error : 'tuple' object does not support item assignment
# change tuple using trick
def change_tuple(tuple_name, value, index = 0):
    dummy_list = list(tuple_name)
    dummy_list[index] = value
    return_tuple = tuple(dummy_list)
    return return_tuple

change_rgb = change_tuple(rgb_colors,'white')
print(change_rgb)


# add value in tuple
def add_value_in_tuple(tuple_name, value, index = 0):
    dummy_list = list(tuple_name)
    dummy_list[index] = value
    return_tuple = tuple(dummy_list)
    return return_tuple

add_value = add_value_in_tuple(rgb_colors, 'aquamarine', 2)
print(add_value)


# Gotcha : a single-element tuple needs a comma
not_a_tuple = (5)
print(type(not_a_tuple))

real_tuple = (5,)
print(type(real_tuple))


# Parentheses are optional
coordinates = 10,20,30
print(coordinates)
print(type(coordinates))        #output : <class 'tuple'>

# 2. Unpacking and comparing : unpacking --pull values out into separate variables
person = ('rofiq', 29, 'dhaka')
name, age, city = person
print(name)
print(age)
print(city)


# The elegant swap
a = 10
b = 20
print(a,b)
c = a
a = b
b = c
print(a,b)


# The elegant swap (no temporary)
a = 3
b = 2
print(a,b)
a = a+b
b = a - b
a = a - b
print(a,b)


#easy way only for python
a = 9
b = 4
a,b = b,a


# advance way (xor operator)
a = 7
b = 3
print(a,b)
a = a ^ b
b = a ^ b
a = a ^ b
print(a)

#  Unpacking inside a loop
students = [("Rahim", 3.59), ("Oboy", 3.98), ("Abu musa", 3.87)]
for name, cgpa in students:
    print(f"{name} has CGPA {cgpa}")
    
students = [("Rahim",23553, 3.59), ("Oboy",32423, 3.98), ("Abu musa",234234, 3.87)]
for name, roll, cgpa in students:
    print(f"{name} roll no : {roll} has CGPA {cgpa}")
#this is exactly how dict.items() worked last class ---each item was really tuple.



# extended unpacking with 
first, *rest = [10,20,30,40,50]
print(first)
print(rest)

first, *middle , last = [1,2,3,4,5]
print(first)
print(middle)
print(last)

first , *middle, last = ['f', 'm', 'm', 'm', 'm','l']
print(first)
print(middle)
print(last)

first, *middle , s_last, last = ['f', 'm', 'm', 'm', 'sl', 'l']
print(first)
print(middle)
print(s_last)
print(last)



# comparing tuples 
# tuples compare element by element, left to right (like dictionary word order)
print((1,2,3,4) == (1,2,3,4))   #True
print((1,2,2,4) == (1,2,3,4))   #False

print((1,2,3) > (1,2,3))        #False
print((3,2,5) > (2,3,4))        #True   #first element decides 3>2

print((1, 2) == (1, 2))     # True
print((1, 2) < (1, 3))      # True   (2 < 3)
print((1, 5) < (2, 0))      # True   (first element decides: 1 < 2)
print((1, 2) < (1, 2, 3))   # True   (shorter is "smaller" when it is a prefix)





num1 = 325
num2 = 234

tuple1 = tuple(int(digit) for digit in str(num1))  #(3, 2, 5)
tuple2 = tuple(int(digit) for digit in str(num2))  # (2, 3, 4)

print("Tuple 1:", tuple1)
print("tuple 2:", tuple2)
print("_____________________________________________")


if tuple1 > tuple2:
    print(f"result : {tuple1[0]} > {tuple2[0]}")
else:
    print(f"result : {tuple1[0]} > {tuple2[0]}")



number1 = "22582012"
number2 = "17794658"
tuple_1 = tuple(number1)
tuple_2 = tuple(number2)
print(tuple_1)
print(tuple_2)
print(tuple_1 > tuple_2)



# list vs tuple 

# Feature	            List	                Tuple

# Syntax	            [1, 2, 3]	            (1, 2, 3)
# Can it change?	    Yes (mutable)	        No (immutable)
# Methods available	    many	                few (count, index)
# Speed	                slightly slower	        slightly faster
# Use it when	        the data will change	the data should stay fixed

# Reach for a tuple when: coordinates, RGB colors, a fixed record, or returning more than one value from a function.
def get_min_max(numbers):
    low = min(numbers)
    high = max(numbers)
    return low, high  # (low, high) 

result = get_min_max([5, 2, 9, 1])
print(result)  # (1, 9)


# Memory and Performance
# import sys        #import at top
# tuples use are less memory
my_list = [1,2,3,4,5,6,7,8]
my_tuple = (1,2,3,4,5,6,7,8)
print(sys.getsizeof(my_list))       #typically - 120 bytes
print(sys.getsizeof(my_tuple))      #typically - 112 bytes

# Bonus : tuples can be dictionary keys, lists can't
location  = {
    (23.8, 90.4):"Dhaka",
    (22.3, 91.8):"Chattogram"
}

print(location[(22.3, 91.8)])
print(location[(23.8, 90.4)])



# 4. Sets : a set an unordered collection of unique items. 
# it automatically removes duplicates, and it has no index. 
# written with curly braces {}.
numbers = {1, 2,3,4,3, 4, 5}
print(numbers)

fruits = {"apple", "mango", "banana", "mango"}
print(fruits)           # remove duplicates
print(len(fruits))
# note: a set has no order . so the printed order may differ from what you typed --- and there is no fruits[0]

# watch out : an empty set is set(), not {}
set_a = set()   #correct empty set
set_b = {}      #this is actually an empty dictionary

print(type(set_a))
print(type(set_b))



# add, remove , and membership

fruits.add("orange")
fruits.remove("banana")
print("apple" in fruits)        #true (very fast lookup)

# classic use : remove duplicates from a list
user_input = [1,2,2,3,4,4,5,6,7,6,5,7,8]
roll = set(user_input)
roll = list(roll)
print(roll)
print(len(roll))


# set operations : set up to groups of students: 
dept_of_a = {'karim', 'rahim', 'hamid', 'jomela', 'komola', 'sokina'}
dept_of_b = {'rofiq', 'jomela', 'azad', 'sokina', 'komola', 'zihad'}

# union : every one in either class
all_student = dept_of_b.union(dept_of_a)    # all_student = dept_of_a | dept_of_b # both are same (all_student = dept_of_b.union(dept_of_a))
print(all_student)

#intersection : --students in both class
duplicate_student = dept_of_b.intersection(dept_of_a)   #dept_of_a & dept_of_b (both are same line)
print(duplicate_student)

#difference --- in dept_of_a not dept_of_b
only_dept_of_a = dept_of_a.difference(dept_of_b)        #dept_of_a - dept_of_b (both are same line)
print(only_dept_of_a)
only_dept_of_b = dept_of_b.difference(dept_of_a)
print(only_dept_of_b)



# symmetric difference ---in exactly one class, not both
class_a = dept_of_a ^ dept_of_b
print(class_a)


# visual summary of set operation 
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"set A : {A}\nset B : {B}")
print(f"A | B (Union):        {A | B}")      # {1, 2, 3, 4, 5, 6}
print(f"A & B (Intersection): {A & B}")      # {3, 4}
print(f"A - B (Difference):   {A - B}")      # {1, 2}
print(f"B - A (Difference):   {B - A}")      # {5, 6}
print(f"A ^ B (Symmetric):    {A ^ B}")      # {1, 2, 5, 6}


# table 
# Operation	                  Symbol	        Method	                    Meaning
# Union	                        |	            .union()	                in either set
# Intersection	                &	            .intersection()	            in both sets
# Difference	                -	            .difference()	            in the first, not the second
# Symmetric diff	            ^	            .symmetric_difference()	    in exactly one




# 5. Putting it all together --mini programs

# mutual friends finder(intersection)
karim_friends = {"Rahim", "Ayesha", "Tamim", "Sadia"}
nabila_friends = {"Ayesha", "Rofiq", "Sadia", "Imran"}

common = karim_friends.intersection(nabila_friends)
print("mutual friends : ", common)


# count unique words in a sentence 
sentence = "the cat sat on the mat the cat run"
words = sentence.split()
print(words)
unique_words = set(words)
print(unique_words)

# stats function (tuple return , unpacking)
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

low, high, avg = stats([78, 94,81, 99, 71])
print(f"min: {low}, high : {high}, avg : {avg}")



# quick recap (cheat sheet)

# Concept	                        Example
# Tuple	                            t = (1, 2, 3)
# Single-element tuple	            t = (5,)
# Immutable	                        tuples cannot be changed
# Unpacking	                        a, b, c = t
# Swap	                            a, b = b, a
# Star unpacking	                first, *rest = items
# Set	                            s = {1, 2, 3}
# Empty set	                        s = set()
# Remove duplicates	                set(my_list)
# Union / Inter / Diff	            |  &  -



# ## Exercises (Try Yourself)
# Start one or two together in class — the rest is homework.

# 1. Create a tuple of 3 cities. Print the first and last using indexing.
# 2. Try to change an element of a tuple. Write a one-line comment explaining what error you get and why.
# 3. Unpack the tuple `("Karim", 22, "CSE")` into three variables and print each one.
# 4. Swap two variables using tuple unpacking (no third variable).
# 5. Given the list `[5, 3, 5, 2, 3, 1, 5]`, use a set to find how many **unique** numbers it has.
# 6. Two students take these subjects:
# `student_a = {"Math", "Physics", "Python"}` and `student_b = {"Python", "Chemistry", "Math"}`.
# Print the subjects they **both** take, and the subjects **only student_a** takes.
# 7. **(Challenge)** Write a function that takes a list of numbers and **returns a tuple** of `(smallest, largest, number_of_unique_values)`.
# 8. **(Challenge)** Given a sentence, count how many **unique words** it has, ignoring case (treat `The` and `the` as the same).




# 1. Create a tuple of 3 cities. Print the first and last using indexing.
# solution 01 : 

city = ("Dhaka", "Paris", "Berlin")
print(f"first city : {city[0]}")
print(f"last city : {city[len(city)-1]}")



# 2. Try to change an element of a tuple. Write a one-line comment explaining what error you get and why.
# solution 02:
colors = ('red', 'green', 'yellow')
# colors[2] = 'blue'      # error : TypeError: 'tuple' object does not support item assignment (tuple is immutable)
print(colors)


# trick (to change tuple value)
dummy_var = list(colors)
dummy_var[2] = 'blue'
colors = tuple(dummy_var)
print(colors)





# 3. Unpack the tuple `("Karim", 22, "CSE")` into three variables and print each one.
karim_info = ("karim", 22, "cse")
name, age , dept = karim_info
print(name)
print(age)
print(dept)



# 4. Swap two variables using tuple unpacking (no third variable).
a = 20
b = 23
print(a, b)
a,b = (b,a)
print(a, b)





# 5. Given the list `[5, 3, 5, 2, 3, 1, 5]`, use a set to find how many **unique** numbers it has.
given_list = [5, 3, 5, 2, 3, 1, 5]
x = set(given_list)
print(list(x))
print(len(x))







# 6. Two students take these subjects:
# `student_a = {"Math", "Physics", "Python"}` and `student_b = {"Python", "Chemistry", "Math"}`.
# Print the subjects they **both** take, and the subjects **only student_a** takes.
# solution
student_a = {"Math", "Physics", "Python"}
student_b = {"Python", "Chemistry", "Math"}
both_takes = student_a.intersection(student_b)
print(both_takes)
student_a_subject = student_a.difference(student_b)
print(student_a_subject)
student_b_subject = student_b.difference(student_a)
print(student_b_subject)


# 7. **(Challenge)** Write a function that takes a list of numbers and 
# **returns a tuple** of `(smallest, largest, number_of_unique_values)`.
def list_cal(given_list):
    minimum = min(given_list)
    maximum = max(given_list)
    number_of_unique_value = len(set(given_list))
    return minimum, maximum , number_of_unique_value


my_list = [23,234,53,94,123,634,12,743,32,74,23,12,45,26,62,213]
smallest, largest, unique = list_cal(my_list)
print(smallest, largest, unique)




# 8. **(Challenge)** Given a sentence, count how many **unique words** it has, ignoring case (treat `The` and `the` as the same).
# Solution
sentence = "Python is great and python is fun but Python requires practice"
print(sentence)
sentence_list = sentence.lower().split()
print(sentence_list)
sentence = set(sentence_list)
print(len(sentence))