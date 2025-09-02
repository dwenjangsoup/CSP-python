print("Exercise #1: Even, odd or zero")
# Write a program that asks the user for a number. 
# Report whether that number is even, odd, or zero.

num= int(input("Type a random number : "))
if num == 0 :
    print("Your number is 0.")
elif num % 2 == 0: 
    print("Your number is an even number.")
else : 
    print("Your number is an odd number.")

print(" ")
print("----------")
print(" ")

print("Exercise #2: Table Reservation")
# Write a program that asks the user for their name using input. 
# It should have another string variable that represents the name on a particular table reservation in a restaurant, stored in a variable called reservation_name. 
# The program should print "Right this way!" if the user's name matches the name on the reservation, and "Sorry, we don't have a reservation under that name." otherwise.
reserv_name = ["Miso", "Somi", "Ms.Peteita"]

name = input("What is your name?")
if name == reserv_name:
    print("Right this way!")
else: 
    print("get out")

print("")
print("----------")
print("")

print("Exercise #3: Presidential Eligibility")
# Write a program that reports whether or not someone is eligible to run for president in the US. 
# You should do the following in your program:
#    Ask the user for their age, and store it in a variable
#    Ask the user if they are a citizen of the U.S.
#    Ask the user how long they've been a resident in the U.S.
#    Use an if/else statement with the proper comparison operator to print "You are eligible to run for president!" if they have the following credentials:
#      They are at least 35 years old
#      They were born in the U.S.
#      They have been a resident for at least 14 years

print("Hi, ", name, "!")
age= int(input("How old are you?"))
b=input("Are you a U.S. citizen? (y/n)")

if b == "y":
    b=1
elif b=="n":
    b=0
else:
    "Read the question carefully."
    b=-1

years=int(input("How long have you been in the U.S.? Type 0 if you are not a resident of U.S."))

print(" ")
loading=["L","O","A","D","I","N","G"]
a=0
for i in range(7):
    print(loading[a])
    a+=1
    
print("")
print("")
print('')

p=0

if age>=35:
    p+=1
else:
    print("You are not old enough to run for the U.S. president.")
    
if b==False:
    print("You can't run for the presidency if you are not a citizen of U.S.")
elif b>0:
    p+=1
else:
    print("You didn't answer the question correctly; You don't deserve to be our president.")

if years >= 14 :
    p+=1
else:
    print("You need to wait more while owning a residency so that you can be eligible later.")
    
print("")
print("You have", p, "points.")
print("")
if p<=2:
    print('You are not able to run for the U.S. president.')
else:
    print("You are able to run for the U.S. president. Good luck!")