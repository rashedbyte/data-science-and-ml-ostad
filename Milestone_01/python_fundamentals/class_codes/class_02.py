import math
import sys
from collections import Counter

# Class 02: Loops, Strings and Smart Operations

# 0. Warm-up : Recap of class 01
x = 7 
if x % 2 == 0 and x > 0 : 
    print("Even and positive")
else:
    print("something else")
    
# output something else --- because 7 % 2 = 1 . so the first condition is false.

# 01 . arithmetic operations 
a = 18
b = 5
print(a + b)    # output 22
print(a - b)    # output 13
print(a * b)    # output 90
print(a / b)    # 3.6     (division ALWAYS gives a float)
print(a // b)   # 3        (floor division - drops the decimal)
print(a % b)    # 3        (modulus - the remainder)
print(a ** b)   # 1889568  (18 to the power 5)


# A real life use of // and % (floor division and modulus)
total_taka = 1000
price_per_kg = 75
kg_can_buy = total_taka // price_per_kg
change = total_taka % price_per_kg

print(f"you can buy {kg_can_buy} kg")   #13
print(f"change {change} taka")          #25



#assignment shortcuts (smart operations)
score = 97

score += 1      #score = score + 1 ----> score  = 97 +1 = 98
print(score)    #98     score = 98

score -= 3      #score = score - 3 -----> score = 98 - 3 = 95
print(score)    #95     score = 95

score *= 2      #score = score * 2 ----> score = 95 * 2 = 190
print(score)    #190    score = 190



# Operator Precedence  : which operation runs first ?  same idea as BODMAS from school math.
#  order (hight to low): () --> ** ---> *,/, // , % --> +-

print(2+3*4)        #3*4 = 2+12 = 14(right),  not 2+3 = 5 * 4 = 20 (wrong)
print((2+3) * 4)    #(2+3 = 5) --> 5 * 4 = 20
print(10 - 4 -3)    #3
print(100 / 10 * 2) #20.0
print(2 ** 3 ** 2)
print(2 ** 9)           # =======> python working up to down and right to left
#teaching tip : when in doubt . use parentheses. code that is easy to read beats code that is clever.

# 3. math function 
# built in (no import needed)

print(abs(-8))
print(round(2.343234234, 2))    #round(number, ndigits)
print(min(234,23432,2354,234,23,4234,23))
print(max(234,234,234,23536,4567,7,3452,3473456,2345 ,65436,2345))
print(pow(2,8))     # 2 to the power 8

# the math module 
# import math  : import at the first line of the file 
print(math.sqrt(23))
print(math.floor(23.23432))
print(math.ceil(23.53))
print(math.factorial(1558))
x = math.factorial(1558)        # (default) most factorial calculate using python 1558
print(len(str(x)))      #4300   # if you want to extend this using 
                                # import sys # sys.set_int_max_str_digits(number_of_digit)
# sys.set_int_max_str_digits(20000)


# 4. String : a String is a sequence of characters --and every character has a position (index). starting from 0
# index and slicing 
course = "python for data science"

print(len(course))      # total number of characters (including space)
print(course[0])        # p     ---> (first index character)) 
print(course[-1])       # e     ----> (last character)
print(course[-2])       # s     ----> (second last character)
print(course[0:6])      # python ---> (index 0 to index 4 ..(5-1))
print(course[2:])       # thon for data science (index 2 to end)
print(course[:6])       # python (index 0 to 5)
print(course[11:])      # data science (index 11 to end)

#joining and repeating 
first = "tamim"
last = "iqbal"
full = first + " " + last
print(full)     #tamim iqbal

print("ha"*3)   #hahaha


# useful String method  
city  = " dhaka    "
print(city.strip())         #dhaka (remove side space)
print(city.upper())   #DHAKA 

msg  = "I love BanglaDesh"
print(msg.lower())          #i love bangladesh
print(msg.replace("love", "miss"))  # i miss bangladesh
print(msg.capitalize())     # I Love Bangladesh
print(msg.count("e"))       # print number of e in this string
print(msg.split())          
print("love" in msg)         #true

# f String --- the modern way to print
name = "karim"
age = 22
print(f"My name is{name} , next year i will {age + 1}")
#from today onwards , prefer f string over comma separated print

# 5. for loops : a for loop repeats a block a known number of times . range () generated the numbers 
# syntax : for item in iterable
# range_function(start, stop , step)
for i in range(5):        #0, 1,2,3,4  (5 is excluded)
    print(i)
    
for i in range(1,5):        #range(start, stop) ---> star = 1 , stop  = 5-1
    print(i)                #1,2,3,4
    
for i in range(1,10,2):         #range(start , stop , step)
    print(i)                    #1,3,5,7, 9
    
#revers loop 
for i in range(0, 10, -1):
    print(i)

# looping over a string 
for i in "Bangladesh":
    print(i) 


my_list = [1,2,3,4,5,6,7,8,9,10]
for item in my_list:
    print(i)


# the accumulator pattern (very important)
total = 0
for i in range (1, 11):
    total += i
print("some of 1 to 10", total )



# while loops  : a while loop repeats as long as a condition stays true ,
# use it when yuo do not know in advance  ho many times you need 

count  = 1 
while count <= 5:
    print("count : ", count)
    # count = count + 1
    count += 1

#repeating until the user says stop 

answer = ""
while answer != "quit":
    answer = input("Type 'quit' to stop : ")
print("loop ended")

#(for vs while) 
# for : known number repeats 
# while: repeats until something happen

# 07 . Break and continue : break ---> exit the loop immediately.
    #                       continue ---> skip this round , go to the next one.


# break 
for number in range (1,100):
    print(number)
    if number % 7 == 0:
        print(f"first number divisible by 7 : {number}")
        break   #quit the loop 

while True : 
    text = input("type 'exit' to stop : ")
    if text == "exit":
        break
    print(f'you typed : {text}')
    # print('you typed : ', text)   #both are same


# continue 
for i in range(1,11):
    if i % 2  == 0:         #skip even number
        # print(f"skipped value {i}")     #see skipped number.
        continue            
    print(i)


# 08 putting it all together --- mini program
# 01 : multiplication table (namta) of any number 

n = int(input("which table do you want: "))

for i in range(1,11):
    print(f"{n}*{i} = {n*i}")

name  = input("Enter your name : ").lower()
vowels = 0
for character in name :
    if character in "aeiou":
        vowels += 1
        print(f"vowel = {character}")  #check vowel
print(f"your name has {vowels} vowels")


#bkash pin (3 attempts)
pin = "727433"
attempt = 0
while True:
    print(f"your attempt left : {3 - attempt}")
    user_input = input("Enter your pin : ")
    attempt += 1 
    if user_input == pin:
        print("login successful. (pin match)")
        break
    print("you entered wrong pin")
    if attempt == 3:
        print("pin block. your attempt over limit")
        break


correct_pin = "2026"
attempts = 0

while attempts < 3:
    pin = input("Enter your bKash PIN: ")
    if pin == correct_pin:
        print("Login successful. Balance: Tk 5,250")
        break
    attempts += 1
    print("Wrong PIN. Attempts left:", 3 - attempts)

if attempts == 3:
    print("Account locked for 24 hours")




# Quick Recap (Cheat Sheet)
# Concept
# Example

# Arithmetic
# +  -  *  /  //  %  **

# Shortcuts
# +=  -=  *=

# Precedence
# () → ** → * / // % → + -

# Math
# abs() round() min() max(), math.sqrt() math.floor() math.ceil()

# String index/slice
# s[0], s[-1], s[2:5], len(s)

# String methods
# .upper() .lower() .strip() .replace() .split() .count()

# f-string
# f"Hello {name}"

# For loop
# for i in range(1, 11):

# While loop
# while condition:

# Control
# break (exit), continue (skip)



# Exercises (Try Yourself)
# Start one or two together in class — the rest is homework.

# 1. Take a sentence and count how many times the letter a appears — using a loop, without .count().
# 2. Print the numbers 1 to 20 using a for loop.
# 3. Print all even numbers from 1 to 50 — once using range() with a step, and once using if with %.
# 4. Take a number N as input and print the sum of 1 to N.
# 5. Take a number N and count down from N to 1, then print Happy New Year!
# 6. Take a word as input and print it reversed (use a loop; slicing shortcut is a bonus).
# 7. (Challenge) Take a number and check whether it is a prime number (use a loop, %, and break).
# 8. (Challenge) Take a number N and calculate N! (factorial) using a loop.

#qs : Take a sentence and count how many times the letter a appears — using a loop, without .count().
# solution 01 
sentence = input("Input a sentence : ")
find_ch = input("Which character you find : ")
count = 0 
for character in sentence:
    # if character  == "a":
    if character  == find_ch:
        count += 1

print(f"'{find_ch}' is {count} times in the sentence")


# qs : Print the numbers 1 to 20 using a for loop.
# solution : 02
for i in range(1,21):
    print(i)


# qs : 3. Print all even numbers from 1 to 50 — once using range() with a step, and once using if with %.
# solution 03 
# using range()
for i in range(1,50,2):
    print(i)

# using if with %
for i in range(50):
    if i % 2 == 1:
        print(i)



# qs : 4. Take a number N as input and print the sum of 1 to N.
# solution ; 04

num = int(input("Enter a number to calculate sum : "))
sum = 0

for i in range(1,num+1):
    sum += i
print(f"sum 1 to {num} = {sum}")



# qs : 5. Take a number N and count down from N to 1, then print Happy New Year!
# solution : 05

# using for loop 
num = int(input("enter a number : "))

for i in range(num,0,-1):
    print(i)
print("Happy New Year.")

num = int(input("Enter a number : "))
i = num
while num >= 1:         
    print(num)
    num -= 1
print("Happy new year.")

#using while loop 
# num = 25#int(input("Enter a number : "))
# print(f"num = {num}")
# i = num
# print(f"i = {i}")
# num = 20
# print(f"num = {num}")
# print(f"i = {i}")

# qs : 6. Take a word as input and print it reversed (use a loop; slicing shortcut is a bonus).
# solution 06 : 
word = "hello"#input("enter a word : ")
rev_word = ""
word_len = len(word) - 1
while word_len >= 0:
    print(word[word_len])
    rev_word += word[word_len]
    word_len -= 1

print(rev_word)

# ============================================================
# practice code (false) ======================================
# word = "hello"#input("enter a word : ")
# list_str = list(word)
# print(f"list word = {list_str}")
# str_list = str(list_str)
# print(f"str list : {str_list}")

# rev_word = list()
# word_len = len(word) - 1
# while word_len >= 0:
#     print(word[word_len])
#     rev_word.append(word[word_len])
#     word_len -= 1

# print(str(rev_word))

# ===============================================================


word = "bangladesh"
w_l = len(word)-1   #length of word - 1 = 9
# print(word[start:stop:step])
print(word[w_l:0:-1]) # word[w_l = 9 : 0 : -1] -1 means decrees 1 


# qs : (Challenge) Take a number and check whether it is a prime number (use a loop, %, and break).
# solution 07 : 
num = 1#int(input("Enter a number to check it is prime or not : "))
is_prime = True

if num >= 2:
    for i in range(2,num):
        print("loop run")
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("this is prime number")
    else:
        print('this is not a prime number')
else:
    print("invalid number (negative and 0,1 are not prime number!)")



# 8. (Challenge) Take a number N and calculate N! (factorial) using a loop.

value = 1558#int(input("Enter a value to calculate factorial : "))
fact = 1
for i in range(1,value+1):
    fact *= i
# print(f"{value}! = {fact}")
# print(str(fact))
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0
count_0 = 0
for n in str(fact):
    if n == "0":
        count_0 += 1
    elif n == "1":
        count_1 += 1
    elif n == "2":
        count_2 += 1
    elif n == "3":
        count_3 += 1
    elif n == "4":
        count_4 += 1
    elif n == "5":
        count_5 += 1
    elif n == "6":
        count_6 += 1
    elif n == "7":
        count_7 += 1
    elif n == "8":
        count_8 += 1
    elif n == "9":
        count_9 += 1
        

print(f"count (1) : {count_1}")
print(f"count (2) : {count_2}")
print(f"count (3) : {count_3}")
print(f"count (4) : {count_4}")
print(f"count (5) : {count_5}")
print(f"count (6) : {count_6}")
print(f"count (7) : {count_7}")
print(f"count (8) : {count_8}")
print(f"count (9) : {count_9}")
print(f"count (0) : {count_0}")

# total_zero  = str(value).count("0")
# print(total_zero)


# short method 

val = 1558
fact = 1

for i in range(1, val+1):
    fact *= i

fact_str = str(fact)

for digit in range(10):
    count = fact_str.count(str(digit))
    print(f"count {digit} : {count}")


# advance method (Data scientist vibe)
# from collections import Counter  # import at top

value = 1558
f = 1

for i in range(1,value+1):
    f *= i


digit_counts = Counter(str(f))
# print(digit_counts.get("x",10)) default value , 10, when some value are not in dict then return 0
for digit in range(10):
    print(f"count ({digit}) : {digit_counts.get(str(digit), 0)}")