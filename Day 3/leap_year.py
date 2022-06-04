# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

isLeapYear = None
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            isLeapYear = True
        else:
            isLeapYear = False
    else:
        isLeapYear = True
else:
    isLeapYear = False

if isLeapYear:
    print("Leap year.")
else:
    print("Not leap year.")