# light = input("light: ")
# if(light == "red"):
#     print("Stop")
# if(light == "green"):
#     print("go")
# if(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")



# food = input("food:")
# eat = "Yes" if food == "apple" else "No"
# print(eat) 



# age = 21
# if(age >= 18):
#     print("can vote and apply for license")
#     print ("can drive and can vote")

# a = int(input("Enter Valid Number:"))
# if(a > 4):
#     print("a greater than 4")
# elif(a < 3):
#     print("a is not greater than 3")
# else:
#     print("Enter valid value")


marks = int(input("Enter student Marks:"))

if(marks >= 90 and marks <= 100):
    print ("You have A grade")
elif(marks >= 80 and marks < 90):
    print ("You have B grade")
elif(marks >= 70 and marks < 80):
    print ("You have C grade")
elif(marks >= 50 and marks < 70):
    print ("You have D grade")
elif(marks < 50  and marks > 0):
    print ("You have E grade")
else:
    print ("enter valid value")

