#write A python program to do arithmetic operations addition and subtraction of two numbers
#Adddition
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

#subtarction
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sub_result = num1 - num2
print(f"sub: {num1} - {num2} = {sub_result}")

#Division
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num2 != 0:
    div_result = num1 / num2
    print(f"div: {num1} / {num2} = {div_result}")
else:
    print("Error: Division by zero is not allowed.")