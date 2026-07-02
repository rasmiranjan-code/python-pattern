#input two variables 
a = input("Enter the value of the first variabales (a): ")
b = input("Enter the value of the second variabales (b): ")
#display the values of the variables
print(f"original values of a and b are: a = {a}, b = {b}")
#swap the values of the variables
temp = a
a = b
b = temp    
#display the swapped values of the variables
print(f"swapped values of a and b are: a = {a}, b = {b}")