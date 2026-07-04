# class 01 : Unlocking the power of variables and logic

# context  :
# 1.store and use data with variables
# 2. Identify  Python's 4 basic data type : int, float, str , bool 
# 3. Explain what dynamic typing means in Python
# 4. Make Decisions in code with (if, elif, else)
# 5. combine comparison and logical operators to write real programs



# 00 warm-up : print()
# our first tool ---it show output on the screen.
print("hello world!")
print("my first python code")
print("I ","can","print","many things together")


# 01_Variables 
# A variables is a named box that stores a value.
# The = sign is the assignment operator ---its means "store this value"
name = 'rahim'          # store string value in name variable
age = 25                # store integer value in age variable
height = 5.8             #store float value in height variable
is_student = True       #store boolean value in is_student variable
print(name)
print(age)
print(height)
print(is_student)

#naming rule
#valid
first_name = "rashed"
age2 = 21
_score = 97

# invalid  ====> these will throw errors
#2age = 23              #can't start with number
#first-name = 'jack'    #hyphen (-) is not allowed
#class = 10             #reserved keyword

# convention for multi word variables names. use snake_case -
# ---> total_score, total_marks, user_name, first_name, last_name, full_name




# changing a value reassignment
x = 10
print(x) #output 10

x = 20
print(x) #output 20

x = x+20
print(x) #output 20+20 = 40

x += 20 #=====> x = x+20 both are same line
print(x) #output 40+20 = 60



# multiple assign in single line
a,b,c = 20, 30, 50 # =====> a = 20, b = 30, c = 50
print(a,b,c) #output 20 30  50

p = q = r = 85
print(p,q,r) #output 85 85  85



# 02_Data Types : python has 4 basics data types we need today. use type() to check any value's type.

roll = 101          #integer (int) ---> whole number
pi = 3.1416         #float         ---> decimal number
city = "rangpur"    #string (str)  ---> text
is_passed = True    #Boolean (bool)---> True/False

print(type(roll)) #<class int>
print(type(pi))   #<class float>
print(type(city)) #<class str>
print(type(is_passed))#<class bool>

#A bit more about String
single  = 'hello python'
double = "hello world"
multi_line  = """this text 
can 
span 
multiple line"""

print(multi_line)






# 03_Dynamic Typing : python figures out the type by itself ---you never declare it. 
# and the same variable can change its type later

data  = 25
print(data, "--",type(data))        #25 -- <class 'int'>

data = "now this is a string"
print(data, "--", type(data))       #now this.... -- <class 'str'>


data = 6.673 
print(data, "--", type(data))       # 6.673 --<class 'float'>

#in C/JAVA you must write int x = 10 in python just x = 10
#that is dynamic typing


# 04_type Casting(Type conversion)
#we will need input() in a moment ---and input() always returns a string. 
# so conversion is essential

age_text = "25"
print(type(age_text))           #<class 'str'>

age_number = int(age_text)
print(type(age_number))         #<class 'int'>

print(int(2.54))                #output 2
print(float(3))                 #output 3.0


num = 100
str_num = str(num)
con_cat = str_num + "200"       #output 100200
print(con_cat)


#taking user input 
name = input("Your name : ")
age  = int(input("Your age : "))    #with out int() , age+1 would fail

print("hello ", name)
print("Next year you will be ", age+1)


# 5 comparison operators
# they compare two value ---the result is always a boolean (True/False)

#operator       meaning
#   ==          equal to
#   !=          not equal to
#   >           gater than
#   <           less than
#   >=          gater than or equal
#   <=          less than or equal

# code
a = 3
b = 5
print(a == b)   #False
print(a!=b)     #True
print(a > b)    #False
print(b > a)    #True
print(a < b)    #True
print(b < a)    #False
print(a >= b)   #False
print(a <= b)   #True


# 06 _ Logical operator 
# and, or , not ---they join multiple condition together

# and ----->
print(True and True)        #True   (True only if both are true)
print(True and False)       #false
print(True and True and False) #false


# or ---->
print(True or True)        #True   (True at least one is true)
print(True or False)       #true
print(True or True or False) #true
print(False or False or False or True) #true


# not --->
print(not True)         #false (flips the value)
print(not False)        #true




# comparison + logical together 
age = 22
has_nid = True
print(age>=18 and has_nid)      #true _can vote
print(age > 18 or has_nid)      #true
print( not(age >= 15))          #false   


# if Statement : python uses indentation (4space = 1 tab)
# to define a block. after the clone (:), the next line must be pushed inside.

# just if 
age = 20
if age >= 18 :
    print("you are an adult.") 
    
    
#if else
age = 17
if age >= 18:
    print("you are adult, you can vote")
else:
    print("you are child, you can't vote.")
    
    
#if elif else 
marks = 97
if marks >= 80:
    print("you got A+")
elif marks >=70:
    print("you got A")
elif marks >= 50:
    print("you got A-")
else:
    print("fail")
    

# logical operator inside if 
username = "admin"
password = "123abc"

if username == 'admin' and password == '123abc':
    print("log in successful")
else:
    print("wrong password")
    



# Nested if (an if inside another if)
age = 25
monthly_income = 50000
if age >= 18:
    if monthly_income >= 40000:
        print("loan approved")
    else:
        print("income to low, loan not approved!")
else:
    print("too young fo a loan")
    
    
# Putting it all together --mini programs 
# even or odd:
number = int(input("enter a number : "))
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number , "is an odd number")
    

# ticket price by age  
age = int(input("enter your age : "))
if age<5:
    print("free ticket")
elif age <=10:
    print("Ticket price 50 taka")
elif age < 18:
    print("ticket price 100")
else:
    print("ticket price 150 taka")
    
    

# cricket milestone checker :
runs = int(input("shakib's runs today : "))
if runs >= 100:
    print("Century")
elif runs >= 50:
    print("Half-Century")
elif runs > 0:
    print("good effort")
else:
    print("duck! better luck next match")