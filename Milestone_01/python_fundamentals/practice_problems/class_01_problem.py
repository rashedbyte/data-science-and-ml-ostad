# practice problem 01 : Store your name and age in two variables, then print: My name is ... and I am ... years old
name = 'Rashed'
age = 21
print("My name is", name, "and I am", age, "years old.")

# practice problem 02 : Take two numbers as input and print which one is bigger (also handle the equal case).
num_1 = int(input("Enter 1st number : "))
num_2 = int(input("Enter 2nd number : "))

if num_1 > num_2:
    print(num_1, "is bigger than", num_2)
elif num_1 == num_2:
    print("Both are the same.")
else:
    print(num_2, "is bigger than", num_1)


# practice problem 03: Take a year as input and check whether it is a leap year.
# Hint: divisible by 4 but not by 100 — OR divisible by 400.
year = int(input("Enter a year to check if it is a leap year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is a normal year.")


# practice problem 04 : Take a user's age and is_member (yes/no). Give a discount.
age = int(input("Enter your age : "))
is_member = input("Are you a member? (yes/no) : ")

if age > 60 and is_member == "yes": 
    print("You have a 30% discount.")
elif age > 60 and is_member == "no":
    print("You have a 20% discount.")
else:
    print("No discount.")
    
    
# practice problem 04 : Take marks (0–100) as input and print the grade using the grading rules above.
marks = int(input("Marks (0-100): "))
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
else:
    print("Fail")
    
    
# practice problem 05 : (Challenge) Take 3 numbers and find the largest one — using only if/else and comparison operators.
a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
    
    
# practice problem 06 : (Challenge) Simple login: if the username is ostad and the password is python2026, print a welcome message — otherwise show an error.
user_name = input("Enter your username : ")
password = input("Enter your password : ")

if user_name == "rashed.byte":
    print("username✅")
    if password == "1234":
        print("Password ✅")
        print("Login Successful✅")
    else:
        print("Wrong Password❌")
else:
    print("Wrong username❌")
    
    
def login(user_name, password):       # It's a security issue, but practiced for building logic
    count = 0
    if user_name == "rashed.byte":
        print("username✅")
        count += 1
    else:
        print("Wrong username❌")
    
    if password == "1234":
        print("Password ✅")
        count += 1
    else:
        print("Wrong Password❌")
    
    if count == 2:
        print("Login Successful✅")
        count = 0
        
        
login(user_name, password)