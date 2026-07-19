# Q1. Create a Python class representing a student with attributes such as name and ID, and include both a default constructor and a parameterized constructor. Add a method to display the student details, and use the pass statement inside an empty placeholder method. Then create multiple objects from this class to test each constructor.

# Q2. Write a Python program demonstrating single, multilevel, and hierarchical inheritance using simple classes such as Person, Student, and Teacher. Include at least one overridden method in the child classes to show method overriding.

# Q3. Define a class that shows encapsulation by using private attributes and public getter/setter methods. Add two methods with the same name but different parameter counts to illustrate method overloading (using default arguments). Then create another class to demonstrate multiple inheritance.



# Q1. Create a Python class representing a student with attributes such as name and ID, and include both a default constructor and a parameterized constructor. Add a method to display the student details, and use the pass statement inside an empty placeholder method. Then create multiple objects from this class to test each constructor.
# solution :  
class Student:
    def __init__(self, name="Unknown", student_id="000"):
        self.name = name
        self.student_id = student_id

    def display_details(self):
        print(f"Student Name: {self.name}, ID: {self.student_id}")

    def future_update_method(self):
        pass  


student1 = Student()
print("Using Default Constructor:")
student1.display_details()
student2 = Student("Rahim", "101")

print("Using Default Parameterized Constructor:")
student2.display_details()



# Q2. Write a Python program demonstrating single, multilevel, and hierarchical inheritance using simple classes such as Person, 
# Student, and Teacher. Include at least one overridden method in the child classes to show method overriding.
# solution : 
class Person:
    def intro(self):
        print("I am a normal Person.")


class Student(Person):
    def intro(self):
        print("I am a Student. I study in school.")

class Teacher(Person):
    def intro(self):
        print("I am a Teacher. I teach students.")

class GradStudent(Student):
    def intro(self):
        print("I am a Graduate Student. I do research.")


person = Person()
student = Student()
teacher = Teacher()
grad_student = GradStudent()

#overridding
person.intro()        
student.intro()       
teacher.intro()       
grad_student.intro()   

# Q3. Define a class that shows encapsulation by using private attributes and public getter/setter methods. 
# Add two methods with the same name but different parameter counts to illustrate 
# method overloading (using default arguments). Then create another class to demonstrate multiple inheritance.
# souation 

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  


    def get_balance(self):
        return self.__balance


    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount!")

    def deposit(self, amount1, amount2=0):
        total_deposit = amount1 + amount2
        self.__balance += total_deposit
        print(f"Deposited: {total_deposit}. New Balance: {self.__balance}")


class AcademicActivity:
    def study(self):
        print("Participating in academic classes.")

class SportsActivity:
    def play_sports(self):
        print("Playing in the university sports team.")

class StudentAthlete(AcademicActivity, SportsActivity):
    pass


print("--- Encapsulation & Overloading Test ---")
account = BankAccount("John", 1000)

print(f"Initial Balance: {account.get_balance()}")

account.set_balance(1500)
print(f"Updated Balance: {account.get_balance()}")

account.deposit(500)

account.deposit(200, 300)

athlete = StudentAthlete()
athlete.study()        
athlete.play_sports()