# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

days_in_ninety_years = 90 * 365
days_in_age = age * 365
days_left = days_in_ninety_years - days_in_age

weeks_in_ninety_years = 90 * 52
weeks_in_age = age * 52
weeks_left = weeks_in_ninety_years - weeks_in_age

months_in_ninety_years = 90 * 12
months_in_age = age * 12
months_left = months_in_ninety_years - months_in_age

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
