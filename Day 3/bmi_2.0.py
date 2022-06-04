# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height ** 2)
bmi = round(bmi)
print(f"Your BMI is {bmi}, ", end="")
if bmi < 18.5:
    print("you are underweight.")
elif bmi < 25:
    print("you have a normal weight.")
elif bmi < 30:
    print("you are slightly overweight.")
elif bmi < 35:
    print("you are obese.")
else:
    print("you are clinically obese.")