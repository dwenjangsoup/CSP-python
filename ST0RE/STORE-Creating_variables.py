print("Exercise 1: Initialize and print variables")
print(" ")

# a.Construct and print a variable that stores data of type: int

thing1= int(input('1. type a random number :'))
print (thing1, "=", type(thing1))
print(" ")

# b.Construct and print a variable that stores data of type: float

thing2 = float(input('2. type a decimal :'))
print((thing2),"=", type(thing2))
print(" ")

# c.Construct and print a variable that stores data of type: str

thing3 = input('3. write something random :')
print((thing3),"=", type(thing3))
print(" ")

# d.Construct and print a variable that stores data of type: bool

thing4 = input('4.type something or just press enter :')
print(bool(thing4), "=", type(thing4))
print(" ")

my_things=[thing1,thing2]
print(my_things)
print(sorted(my_things))

print(" ")
print("----------")
print(" ")

print("Exercise 2: Mathemetical operators")
print(" ")

# Using the variables above, have then interact using the following mathematical operators
# +, -, *, /, %, **, //
# Note: what's the difference between / and //


# a. Explore the mathematical operators above on strings. What do you notice?


something = input('5. Choose one sign among those : -  +  - *  /  **  //')
if something == '+':
    print(my_things[1], '+', my_things[0], "=")
    print(float(my_things[0]+my_things[1]))
elif something == '-':
    print(my_things[1], '-', my_things[0], '=')
    print(float(my_things[0]-my_things[1]))
elif something=='*':
    print(my_things[0],'*', my_things[1], '=')
    print(my_things[0]*my_things[1])
elif something =='/':
    print(my_things[1],"/", my_things[0], "=")
    print(my_things[0]/my_things[1])
elif something == '**':
    print(my_things[0], "**", my_things[1], "=")
    print(my_things[0]**my_things[1])
elif something == '//':
    print(my_things[1], "//", my_things[0], '=')
    print(my_things[1]//my_things[0])
else:
    print("follow the instructions")

print("----------")
print("User info")

# b. Write a program that:
# i. stores your name in one variable called name
name= input('type in your name : ')
# ii. stores your age in another variable called age
age = int(input('type in your age :'))
# iii. prints a one-line greeting that includes your name and your age
print(" Hi user!")
print(" ")
print("name = ", name)
print("age =", age)