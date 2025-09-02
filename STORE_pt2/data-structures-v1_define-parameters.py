print("Exercise #1: Area of a Square")
# Write a program that will calculate and print the area of a square.
# Its side length should be given by the user.
# To compute the area, write a function named calculate_area that takes a single parameter, side_length. 
# The parameter should be given a default value of 10.
# If the user enters a length value of 0 or less, call calculate_area and use the default value. 
# Otherwise, use the length value given as the parameter value.

tp = input('Decimal / integer : ')


if tp.lower() == 'decimal':
    sl = float(input("Enter side length : "))
elif tp.lower() == 'integer':
    sl=int(input("Enter side length : "))
else :
    print("Follow the instructions.")
    
    
def calculate_area(sl=10):
    if sl<=0:
        sl=10
    print("Area of a square is", sl*sl)
    
calculate_area(sl)

print(" ")
print("----------")
print(" ")

print("Exercise #2: add, subtract, multiply")
# Write a program that asks the user for two numbers. 
# Then ask them if they would like to add, subtract, or multiply these numbers.
# Use .lower() to accept any capitalization format
# Perform the chosen operation on the values, showing the operation being performed 
# Use numbers in order even if a negative value is produced!

# Write three functions, one for each mathematical operation.
n1=int(input("Choose your first number : "))
n2=int(input("Choose your second number : "))
f = input("Would you like to add, subtract or multiply ? (+/-/*)")

if f == '+':
    print(n1,'+',n2,'=',n1+n2)
elif f== '-':
    print(n1,'-',n2,"=",n1-n2)
elif f== '*':
    print(n1,' x ', n2,'=', n1*n2)
else:
    print("Follow the format.")
    

print("----------")
print("Exercise #3: sum of two numbers")
# Write a function that takes two arguments and returns their sum.
# Call your function to test it out.

numl=[float(input("Type your first number : ")), float(input("Type your second number : "))]

def sum(numl):
    print(numl[0]+numl[1])
    
sum(numl)print("Exercise #1: Area of a Square")
# Write a program that will calculate and print the area of a square.
# Its side length should be given by the user.
# To compute the area, write a function named calculate_area that takes a single parameter, side_length. 
# The parameter should be given a default value of 10.
# If the user enters a length value of 0 or less, call calculate_area and use the default value. 
# Otherwise, use the length value given as the parameter value.

tp = input('Decimal / integer : ')

if tp.lower() == 'decimal':
    sl = float(input("Enter side length : "))
elif tp.lower() == 'integer':
    sl = int(input("Enter side length : "))
else:
    print("Follow the instructions.")

def calculate_area(sl=10):
    if sl <= 0:
        sl = 10
    print("Area of a square is", sl * sl)

calculate_area(sl)

print(" ")
print("----------")
print(" ")

print("Exercise #2: add, subtract, multiply")
# Write a program that asks the user for two numbers. 
# Then ask them if they would like to add, subtract, or multiply these numbers.
# Use .lower() to accept any capitalization format
# Perform the chosen operation on the values, showing the operation being performed 
# Use numbers in order even if a negative value is produced!

# Write three functions, one for each mathematical operation.
n1 = int(input("Choose your first number : "))
n2 = int(input("Choose your second number : "))
f = input("Would you like to add, subtract or multiply ? (+/-/*)")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

if f == '+':
    print(n1, '+', n2, '=', add(n1, n2))
elif f == '-':
    print(n1, '-', n2, "=", subtract(n1, n2))
elif f == '*':
    print(n1, 'x', n2, '=', multiply(n1, n2))
else:
    print("Follow the format.")

print("----------")
print("Exercise #3: sum of two numbers")
# Write a function that takes two arguments and returns their sum.
# Call your function to test it out.

def sum_two_numbers(a, b):
    return a + b

num1 = float(input("Type your first number : "))
num2 = float(input("Type your second number : "))
print("Sum:",