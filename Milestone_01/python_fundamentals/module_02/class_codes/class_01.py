import copy
# Module 02, class 01
# Understanding Data Structures and functions

# Topics :  list. list method. dictionaries functions. 
        #   parameters/ argument. keyword argument.
        #   default parameter value. return statement

# 1. list : a list an ordered collection that holds multiple items in one variable
#           items can even be of mixed types.

# example 
fruits = ["apple", "banana", "cherry", "mango", "litchi"]
numbers = [10,20,30,40,50,60]
mixed = ["Shakib", 75, 51.39, True , "Rashed", "Jesmin"]

print(fruits)
print(len(fruits))


#index and slicing (same rule as strings)
fruits = ["apple", "banana", "mango", "jackfruits", "litchi", "cherry"]
print(f"fruits after before : {fruits}")
fruits_clone = fruits[:]
print(f"fruits clone before append {fruits_clone}")

fruits.append("blackberry")
print(f"fruits after append : {fruits}")
print(f"fruits clone after append : {fruits_clone}")

#reverse list 
fruit_revers = fruits[::-1]
print(fruit_revers)

# advance cloning and slicing
fruits = ["apple", "banana", "mango", "jackfruits", "litchi", "cherry"]
print(fruits[0::-1])    #[0--> start index:default last index: -1--> right to left]
                        # fruit[0] = apple ---> go left ---> no item ---> loop complete
print(fruits[0:-1])     #[0--->start: -1---> stop]  ==> negative 1 == last index  negative 2 == second last Index
                        # [0 to last index -1]      ==>  ["apple", "banana", "mango", "jackfruits", "litchi"]

print(fruits[0:4:-1])   #start 0, stop 4, right to left step 1
print(fruits[5:0:-1])   #star 5, stop , right to left , step 1

#advance cloning (deep copy)
# import copy # import at top
nested_list = [[1,2],[3,5]]

perfect_clone = copy.deepcopy(nested_list)
perfect_clone[0][1] = 75
print(f"original nested list {nested_list}")
print(f"copy nested list {perfect_clone}")

# list can change (mutable) : unlike string, you can edit a list after creating it .
my_list = [1,2,3,3,5,6,7]
print(my_list)
my_list[3] = 4
print(my_list)

# looping over list 
prices = [23,50,30,100]
for p in prices:
        print(p,"taka")

# membership check
brand = ["walton", "xiaomi", "oppo", "vivo", "apple", "samsung" ]
print("xiaomi" in brand)        #true
print("microsoft" in brand)     #false


# 2. List method 
cart = ["rice", "oil", "egg"]
cart.append("salt")
print(cart)

cart.insert(0, "chicken")
print(cart)

cart.reverse()
print(cart)

cart.sort()
print(cart)

cart.sort(reverse=True)
print(cart)

cart.remove("salt")
print(cart)
cart.remove("chicken")
print(cart)

print(brand)

# brand.extend("hello")
# print(brand)

xiaomi_index = brand.index("xiaomi")
print(xiaomi_index)
brand.pop()
print(brand)

brand.clear()
print(brand)



numbers = [20,30,50,40,90,60,40,60,80,70]
numbers.sort()
print("sorted number", numbers)
numbers.sort(reverse=True)
print("revers sorted number : ", numbers)


numbers.reverse()
print(numbers)

print(len(numbers))
print(numbers.count(60))

print(numbers.index(50))

# Method	What it does
# append(x)	add x to the end
# insert(i, x)	add x at index i
# remove(x)	remove first matching x
# pop()	        remove and return the last item
# sort()	sort in place
# reverse()	reverse in place
# count(x)	how many times x appears
# index(x)	position of x


# 3. Dictionaries : a dictionary stores data as key : value pairs. think of a student record or a price list , 
#    where you look something up by name instead of by position.

student = {
        "name": "Rashed",
        "age":22,
        "dept":"CSE",
        "cgpa" : 3.80
}
print(student["name"])
print(student["age"])
print(student['dept'])


# add and update 
student["age"] = 21
student["university"] = "DUET"
print(student)

# safe access and useful method 
print(student.keys())
print(student.values())
print(student.get('phone',"N/A"))


for key in student:
        print(key)


for key, value in student.items():
        print(f"key : {key}, value : {value}")


# real example (price list)
prices = {
        "rice":60,
        "oil":200,
        "egg":50
}

print(prices['oil'])

print(f"5kg Rice : {prices['rice']*5} taka")

# 4. Function : a function is reusable block of code with a nem. write it once ,
# use it many times . this keeps code short and organized, function define "def" keyword

def greet():
        print("Welcome to ostad")

greet()         #call it 
greet()         #reuse it

# Parameters and arguments
# a parameter is the name in the definition.  
# an argument is the actual value you pass when calling.

def greet(name):
        print(f"hello {name}. welcome")

greet("Rashed")         #call with argument
greet("Jesmin")         #reuse the function

# multiple parameters :
def add(a,b):
        print(a+b)

add(2,3)
add(40,60)

#Keyword argument (kewargs) : pass value by name --then the order does not matter
def student_info(name, dept, cgpa):
        print(f"{name} studies {dept} with CGPA {cgpa}")

student_info(dept="CSE", name="Rashed", cgpa=3.86)
student_info(dept="ALIM", name="Jesmin", cgpa=3.96)


# default parameters : give a parameter a fallback value, 
# used when the caller does not provide one.
def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}")

greet("Jack")
greet("Abu Musa", "Assalamualaikum")


# 5. The return statement : print only shows a value on screen. 
# return sends a value back so you can store it  and use it later. 
# this is the difference that matters most.

def add(a,b):
        return a+b

result = add(23,35)
print(result)

# compare a function only prints : 
def add_print(a,b):
        print(a+b)
x = add_print(2,5)
print(x)                #output None


# a function  with logic and return
def grade_print(marks):
        if marks >= 80:
                print("A+")
        elif marks >=70:
                print("A")
        elif marks >= 50:
                print("A-")
        else:
                print("fail")

def grade_return(marks):
        if marks >= 80:
                return "A+"
        elif marks >=70:
                return "A"
        elif marks >= 50:
                return "A-"
        else:
                return "fail"

grade_print(90)
print(grade_return(95))

#return function use to other operation.
x = grade_return(40)
if x == "A+":
        print("congratulation!")
elif x == "fail":
        print("don't worry, try again.")


# return also ends the function immediately --nothing after it runs.
# 7. Putting is all together --mini programs

# average of a list 
# solution : 
def average(numbers):
        return sum(numbers) / len(numbers)

student_01_marks = [90,100,100]
student_01_avg = average(student_01_marks)
print(f"Student 01 Avg marks : {student_01_avg}")


# phone number lookup using name,
# solution :

phone_book = {
        'Abu Musa' : '01729206099',
        'Rashed':'01780949775',
        'Shohag':'01906166350'
}

def find_number(name):
        result = phone_book.get(name, "not found")
        print(f"{name} : {result}")

find_number("Rashed")
find_number("rofiq")



# shopping bill (list, dict , function , loop , return)

prices = {
        "rice":70,
        "chicken":300,
        "oil":200,
        "egg":20
}

def total_bill(items):
        total  = 0
        for item in items:
                total += prices[item]
        return total

cart = ['rice', 'egg', 'oil']

print(f"total bill : {total_bill(cart)} taka")



# QUICK RECAP (CHEAT SHEET)
# Concept	        Example
# List	                items =[1, 2, 3]
# Index / slice	        items[0], items[-1], items[1:3]
# List methods	        .append() .insert() .remove() .pop() .sort()
# Dictionary	        d = {"name": "Ayesha"}
# Access	        d["name"], d.get("key", default)
# Dict loop	        for k, v in d.items():
# Define function	def name(params):
# Default value	        def f(x, y=10):
# Keyword call	        f(y=5, x=2)
# Return	        return value



## Exercises (Try Yourself)

# Start one or two together in class — the rest is homework.

# 1. Create a list of your 5 favorite foods. Print the first and the last item using indexing.
# 2. Make a list of 5 numbers. Print the largest and the smallest (use `max()`/`min()` or `sort()`).
# 3. Create a dictionary of 3 students with their CGPA. Print one student's CGPA using its key.
# 4. Write a function `square(n)` that **returns** n squared. Call it for the numbers 1 to 5 in a loop.
# 5. Write a function `is_passed(marks)` that returns `True` if marks are 40 or above, otherwise `False`.
# 6. Write a function `greet(name, language="English")` that prints a different greeting depending on the language.
# 7. **(Challenge)** Write a function `count_even(numbers)` that takes a list and **returns** how many even numbers are in it.
# 8. **(Challenge)** Build a small phone book using a dictionary, with one function to add a contact and another to look one up by name.


# qs  : 1. Create a list of your 5 favorite foods. Print the first and the last item using indexing.
# solution :
foods = ["coffee", "burger", "noodles", "ramen",  "pizza"]
first = foods[0]
last = foods[len(foods)-1]
print(first, last)


# qs 02. Make a list of 5 numbers. Print the largest and the smallest (use `max()`/`min()` or `sort()`).
# solution : 
nums = [23,33,64,25,15,63,47,86,18,84,93,21]

# way - 01 to find largest and smallest number 
nums.sort()
largest = nums[len(nums)-1]
smallest = nums[0]
print(f"largest = {largest}, smallest = {smallest}")

# way 02 : to find largest and smallest number 
largest = max(nums)
smallest = min(nums)
print(largest, smallest)

# way 03 : to find largest and smallest number (using loop)
maximum = 0
minimum = nums[0]
for num in nums:
        if num > maximum: 
                maximum = num
        if num < minimum :
                minimum = num
print(minimum, maximum)


# qs ; 3. Create a dictionary of 3 students with their CGPA. Print one student's CGPA using its key.
# solution
cgpa = {
        "student_1":3.87,
        "student_2":3.98,
        "student_3":3.97
}

print(f"student 1 : {cgpa['student_1']}")
print(f"student 2 : {cgpa['student_2']}")
print(f"student 3 : {cgpa['student_3']}")



# qs  : 4. Write a function `square(n)` that **returns** n squared. Call it for the numbers 1 to 5 in a loop.
# solution 
def square(n):
        return n*n

for i in range(6):
        print(square(i))


# qs : 5. Write a function `is_passed(marks)` that returns `True` if marks are 40 or above, otherwise `False`.
# solution 
def is_passed(marks):
        if marks > 40:
                return True
        else:
                return False

print(is_passed(87))



# qs :  6. Write a function `greet(name, language="English")` that prints a different greeting depending on the language.
# solution 
def greet(name, language = "english"):
        if language.lower() == "english":
                return f"Hello {name}, Good Morning. \nHow are you ?"
        elif language.lower() == "hindi":
                return f"Namaste {name}, Supravat. \nkaise hon ap ?"
        elif language.lower() == "italian":
                return f"ciao {name}, buongiorno. \ncome stai ?"
        elif language.lower() == "german":
                return f"hallo {name}, guten morgen. \nWie geht es Ihnen ?"
        elif language.lower() == "bangla":
                return f"Assalamualaikum {name}, Shuvo shokal. \nkemon achen ?"
        elif language.lower() == "chinese":
                return f"Ni hao {name}, zao an. \nnin hao ?"
        else:
                print("your language is not found")
                return greet(name,"english")
print(greet("Rashed", "hindi"))
print(greet("Rashed", "italian"))
print(greet("Rashed", "german"))
print(greet("Rashed", "chinese"))


# 7. **(Challenge)** Write a function `count_even(numbers)` that takes a list and **returns** how many even numbers are in it.
# solution:
def count_even(numbers):
        result = 0
        for num in numbers:
                if num % 2 == 0:
                        result = result+1
                
        return result

print(count_even(numbers))

# 8. **(Challenge)** Build a small phone book using a dictionary, with one function to add a contact and another to look one up by name.
# solution
#
# create dictionary
contact_book = {}
print(type(contact_book))

#create add function
def add_contact(name, number):
        contact_book[name.lower()] = number

#create find function
def find_contact(name):
        return contact_book.get(name.lower(),"Not found")

add_contact("rashed", "0112xxxxx")
add_contact("jesmin", "0334xxxxx")
print(contact_book)
print(find_contact("jesmin"))

