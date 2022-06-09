#Write your code below this line 👇
import math

def prime_checker(number):
    if number < 2 or number % 2 == 0:
        print("It's not a prime number.")
        exit()
    sqrt = math.sqrt(number)
    integer_sqrt = math.ceil(sqrt)
    for divisor in range(3, integer_sqrt + 1, 2):
        if number % divisor == 0:
            print("It's not a prime number.")
            exit()
    print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
