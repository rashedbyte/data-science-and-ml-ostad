# Class 01 : introduction to oop concepts 
# 1. why oop ? 
# so far we wrote procedural code: data in variables, separate functions, 
# to work on it that works for small programs 
# but real system have many related things (students, accounts, products) 
# --each with its own actions.
# OOP lets us **bundle data and behavior together** into one unit called an object, modeled on a real-world thing.

# Mental model:

# - A **class** is a blueprint (a design /). It describes what every object will look like.
# - An **object** is one real thing built from that blueprint.

# One `Student` blueprint → many student objects (Ayesha, Karim, Sadia), each with their own data.




# 2. Classes and Objects
class Student:
    pass        # a class cannot be empty: pass is a placeholder for future code
s1 = Student()  # create an object of Student class(also call an instance of Student class)
# this works, but it is tedious and easy to forget a field. We can do better by 
# defining a constructor method that sets up the object with its initial data. 




# 3. the parameterized constructor.
class Student:
    def __init__(self, name, age, roll_no, cgpa):  # constructor method
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.cgpa = cgpa
        
s1 = Student("Ayesha", 20, 101, 3.5)  # create an object of Student class
s2 = Student("Karim", 21, 102, 3.8)  # create another object of Student class

print(s1.name, s1.age, s1.roll_no, s1.cgpa)  # output : Ayesha 20 101 3.5
print(s2.name, s2.age, s2.roll_no, s2.cgpa)  # output : Karim 21 102 3.8


# what is self?
# self refers to the specific object being worked on.
# when you write Student("Ayesha", 20, 101, 3.5), 
# the constructor is called with self referring to the new object being created.
# so self.name  = name  means "store this name on this particular object"

# you never pass self yourself ---python does it for you, it is just always the first parameter.


# 4.method 
# a method is simply a function defined inside a class . its first parameter is always self . which gives it access to the object's own data.

class Student:
    def __init__(self, name, cgpa):
        self.name = name 
        self.cgpa = cgpa
    
    def show_info(self):
        print(f"{self.name} has a CGPA of {self.cgpa}.")
    
    def is_on_deans_list(self):
        return self.cgpa >= 3.75

s1 = Student("Rashed", 3.96)

s1.show_info()                      #output  :  Rashed has a CGPA 3.96.
print(s1.is_on_deans_list())        #output : True

# Notice : show_info() needs no arguments from us  ---it already knows the object's data through self.




# 5. The default constructor : these are two things people mean by default constructor know both

# (a) the one gives python you for free
# if you do not write __init__ . python provides a hidden one that takes no arguments Student() worked back in section 2.

class Empty: 
    pass

e = Empty()     #works, thanks to the free constructor


# (b)  a constructor where you supply default values .
#  this connects to the default parameter values from module 02. give parameters fallback values , so the object can be created with or without arguments.

class Student:
    def __init__(self, name = "Unknown", cgpa = 0.0):
        self.name = name
        self.cgpa = cgpa 

s1 = Student()      #use the defaults
s2 = Student("Jack", 3.87)  #override them

print(s1.name, s1.cgpa)     #default value (unknown 00)
print(s2.name, s2.cgpa)     #Jack 3.87

# 6. the pass statement : pass does nothing , it is a placeholder for places where python requires some code but you have not written it yet. it keeps the program valid so it still runs.

class FutureFeature:
    pass                #will build this later

def todo():
    pass                #not implement yet

for i in range(5):
    pass                #body intentionally empty for now

# with out pass , an empty class function , or loop body is a syntax error



# 7. intro to Inheritance : Inheritance lets one class reuse the attributes and methods of another. the original is the parent(base/super)class. the new one is the child (derived class. the child gets everything the parent  has and can add more.
class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age 
    
    def gree(self):
        print(f"Hi, I'm {self.name}, age {self.age}")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying python.")

s1 = Student("Nahar", 23)
s1.gree()
s1.study()


# the same parent can be reused by many children:
class Teacher(Person):
    def tech(self):
        print(f"{self.name} teaches at MIT")
t1 = Teacher("Ashraful Hoque", 32)
t1.gree()
t1.tech()

# we will  go deeper next class (overriding methods, super()). for today the key idea is : write common code once in the parent , reuse it in every child.




# 8. Putting it all to gether ---mini programs
# bank account(the classic oop example)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"deposit {amount} successfully. balance : {self.balance}")
        
    def withdraw(self, amount):
        self.balance -= amount
        print(f"withdraw : {amount} successfully. balance : {self.balance}")

emp1 = BankAccount("Abdul Hoque", 50000)
print(emp1.owner)
emp1.deposit(2300)

emp2 = BankAccount("Shahabuddin", 75000)
print(emp2.owner)
emp2.deposit(50000)
emp2.withdraw(20000)

emp1.withdraw(3000)



# Rectangle with methods (Optional , time, permitting):
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(5, 3)
print("Area : ", r.area())
print("Perimeter : ", r.perimeter())


# Inheritance in action (optional, time permitting):

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} is starting..")

class Car(Vehicle):
    def honk(self):
        print("beep beep")

car1 = Car("Toyota")
car1.start()
car1.honk()




# quick recap   (cheat sheet)

# concept                   example
# ==========================================================
# define a class            class Student:
# crate an object           s = Student(....)
# constructor               def __init__(self...)
# store data                self.name = name
# method                    def show(self):
# default values            def __init__(self, name = "guest")
# placeholder               pass
# inheritance               class Student(Person)



# exercises (try your self) : start one or two together in class ---the rest is homework.
# 1. Create a class `Dog` with attributes `name` and `breed` using `__init__`. Create two dog objects and print their info.
# 2. Add a method `bark()` to the `Dog` class that prints `"<name> says Woof!"`.
# 3. Create a class `Circle` with a `radius`, and a method `area()` that returns `3.1416 * radius * radius`.
# 4. Create a class `Student` with `name` and `marks`. Add a method `result()` that returns `"Pass"` if marks are 40 or above, otherwise `"Fail"`.
# 5. Create a class whose constructor uses default values (`name="Guest"`, `age=0`). Make one object with defaults and one with custom values.
# 6. Use the `pass` statement to create a placeholder class `FutureModel` and a placeholder method inside it.
# 7. **(Challenge)** Extend the `BankAccount` class so it also counts how many transactions (deposits + withdrawals) have happened.
# 8. **(Challenge)** Create a parent class `Person` (with `name` and a `greet()` method) and a child class `Employee` that inherits from it and adds a `work()` method. Show that an `Employee` object can both greet and work.



# 1. Create a class `Dog` with attributes `name` and `breed` using `__init__`. Create two dog objects and print their info.

#  solution : 
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("tommy", "Persian")
dog2 = Dog("Max", "German Shepherd")
print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)



# 2. Add a method `bark()` to the `Dog` class that prints `"<name> says Woof!"`.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says woof woof!")

dog1 = Dog("Tommy", "Persian")
dog2 = Dog("Teddy", "Golden Retriever")

dog1.bark()
dog2.bark()


# 3. Create a class `Circle` with a `radius`, and a method `area()` that returns `3.1416 * radius * radius`.
# solution: 
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.1416 * (self.radius **2)

circle = Circle(2.5)
print(circle.area())

# 4. Create a class `Student` with `name` and `marks`. Add a method `result()` that returns `"Pass"` if marks are 40 or above, otherwise `"Fail"`.
# solution  : 
class Student: 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

s1 = Student("Karim", 69)
s2 = Student("Sadia", 37)

print(s1.result())
print(s2.result())

# 5. Create a class whose constructor uses default values (`name="Guest"`, `age=0`).
# Make one object with defaults and one with custom values.
class Person:
    def __init__(self, name = "guest", age = 0):
        self.name = name 
        self.age = age
p1 = Person()   #default value
p2 = Person("Rashed", 21)
print(p1.name, p1.age)
print(p2.name)
print(p2.age)



# 6. Use the `pass` statement to create a placeholder class `FutureModel` and a placeholder method inside it.
class FutureModel:
    def __init__(self):
        pass
    
    def train(self):
        pass
    
    pass


# 7. **(Challenge)** Extend the `BankAccount` class so it also counts how many transactions (deposits + withdrawals) have happened.
# solution : 
class BankAccount:
    def __init__(self, account_holder, amount):
        self.owner = account_holder
        self.balance = amount
        print(f"Bank Account Created.\nAccount Holder : {self.owner}\nAccount Balance : {self.balance}")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.owner} deposited : {amount}taka Successfully.\nNew Balance : {self.balance}")
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"{self.owner} successfully withdraw : {amount}, \nNew Balance : {self.balance}")

acc1 = BankAccount("Rashed", 2300000)
acc1.deposit(230000)
acc1.withdraw(20000)

acc2 = BankAccount("Jesmin", 999999)
acc2.deposit(999999)
acc2.withdraw(11111)




# 8. **(Challenge)** Create a parent class `Person` (with `name` and a `greet()` method) and 
# a child class `Employee` that inherits from it and adds a `work()` method. 
# Show that an `Employee` object can both greet and work.
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"hello {self.name}")

class Employee(Person):
    def work(self):
        print(f"{self.name} worked in google")


emp = Employee("Michel")
emp.greet()
emp.work()
