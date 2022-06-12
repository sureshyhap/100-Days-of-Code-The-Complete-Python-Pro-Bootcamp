import art, replit

print(art.logo)

def calculate(number1, operation, number2):
  if operation == "+":
    return number1 + number2
  elif operation == "-":
    return number1 + number2
  elif operation == "*":
    return number1 * number2
  elif operation == "/":
    return number1 / number2
  else:
    return

continue_with_result = False
while True:
  if not continue_with_result:
    num1 = float(input("What's the first number?: "))
  print("+")
  print("-")
  print("*")
  print("/")
  operator = input("Pick and operation: ")
  num2 = float(input("What's the next number?: "))
  result = calculate(num1, operator, num2)
  print(f"{num1} {operator} {num2} = {result}")
  choice = input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  num1 = result
  continue_with_result = False if choice == 'n' else True
  if not continue_with_result:
    replit.clear()