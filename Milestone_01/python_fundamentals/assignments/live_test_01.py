# live test 01 : input score and check Grade

score = int(input("enter your score : "))
if score >= 90 and score <= 100:
    print("A")
elif score >=80 and score <=89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 50 and score <=59:
    print("E")
elif score >= 40 and score <= 49:
    print("E-")
elif score <40 :
    print("Fail")
else:
    print("invalid mark")