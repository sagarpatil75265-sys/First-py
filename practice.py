a= int(input("enter first digit"))
b= int(input("enter second digit"))

add = (a+b)
print (add) 

# for multiplication

a = int(input("enter first number"))
b = int(input("enter second numbers"))

mul = (a*b)
print (mul)

# # triffic light code

light = (input("enter light"))

if(light == "green"):
    print ("go")
elif(light == "yello"):
    print ("wait")
elif(light == "red"):
    print ("stop")
else:
    print("error") 


# grade distrubution 
marks = int(input("enter marks"))

if (marks >= 90):
    grade = "A+"
elif (marks >=80 and marks < 90):
    grade = "A"
elif (marks >=70 and marks <80):
    grade = "B"
elif (marks >=60 and marks <70 ):
    grade = "C"
elif (marks >= 50 and marks < 60):
    grade = ("D")
elif (marks >=35 and marks <50):
    grade = "fail"

print (grade) 

#   finding even or odd numbers 

num = int(input("enter your number"))

if (num % 2==0):
    print ("even")
else:
    print ("odd") 


movie1 = (input("enter first movie name"))
movie2 = (input("enter second movie name"))
movie3 = (input("enter third movie name"))

movie = [movie1,movie2,movie3]

print (movie) 

marks = int(input("enter marks"))

if (marks >=35):
    print("pass")
else:
    print("fail")

num = int(input("emter number"))

if (num > 0):
    print ("positive")
else:
    print ("negetive")


# divisible numbers

num = int(input("enter your number"))

if (num %5 == 0):
    print ("divisible")
else:
    print("not divisible")
    
# eligibilyty counting


age = int(input("enter age"))

if (age >= 18):
    print ("eligible for voting")
else:
    print("not eligible") 

# tempreture testing

tem = int(input("enter tempreture"))

if (tem >= 30):
    print("hot day")
elif (tem >= 30 and tem >15):
    print ("normal day")
elif (tem <=15):
    print ("cold day")
else:
    print ("not day") 

# LECTURE NOTES


info = {
    "name": "sagar",
    "age": 17,
    "height": 5.6,
    "school": "podar learning school",
    "class": 11,                                                                          
    "topic": "coding",
    "subject": "math",
}

info["name"] = "patil saheb"
info["surname"] = "patil" 

print (info) 

dic = {
    "name" : "patil",
    "surname" : "hangarge",
    "roll" : 5454721,
    "age" : 17
}

dic ["name"] = "sagar"
dic["age"] = 18 
dic["profile portpholio"] = "great"

# print (dic) 

student = {
    "name": "sagar",
    "subject":{
        "phy": 94,
        "chem": 98,
        "math": 99,
    }
}
print(student["subject"]["math"]) 

print (len(list(student.keys())))

# IF ELSE WITH NESTING 

name = (input("enter your name:-"))

print (len(name))

name = ("this is a $ and you got $")

print(name.count) 


marks = int(input("enter marks"))
if (marks >=90):
    grade = ("A")
elif(marks <90 and marks >=80):
    grade = ("B")
elif(marks<80 and marks >= 70):
    grade = ("C")
else:
    grade = ("D")

print("your grade is :-", grade) 

# NESTING

age = int(input("enter your age"))

if(age>=18):
    if(age>=80):
        print ("you can not drive")
    else:
        print("you can drive")
else:
    print("you cannot drive")

    # FINDING GRETEST NUMBER


num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))

if(num1 > num2):
    print("first is greater number")
elif(num1 < num2):
    print("second number is gretest")
else:
    print("third id gretest") 


num = int(input("enter number"))

if (num %7 == 0):
    print("multiple of seven")
else:
    print("not multiple of seven") 


dic = {"name":"sagar",
       "subject":{
           "phy":62,
           "chy":98,
           "math":99,
}
       

}
newdic = {"city":"degloor"}
dic.update(newdic)
print(dic) 

# STARTING OF SET

col = {4,1,5,2,"sagar patil","moryaa"}

print(col)
print(type(col)) 

sagar = set()
sagar.add(7)
sagar.add(4)
sagar.add(8)

sagar.remove(7)
print(sagar)

xyz = {"sagar","patil", "hangarge","saheb","malak"}

print(xyz.pop())
print(xyz.pop())
print(xyz.pop())
print(xyz.pop()) 

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.intersection(set2)) 

sub = {
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(len(sub))

# PRACTIC QUESTION WHILE LOOP AND FOR LOOP

i = 1
while i <= 100 :
    print(i)
    i += 1
print (i)  

i = 100
while i >= 1:
    print (i)
    i -= 1
print (i)


#  MAKING TABLES

n = int(input("enter number :"))
i = 1
while i <= 10:
    print (n*i)
    i += 1  

a = input("enter somthing")
if (a == a):
    print("great wall")
    
