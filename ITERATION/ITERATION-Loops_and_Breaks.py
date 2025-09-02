print("Exercise #1: Even values")
# # Write a program that prints even numbers 2 through 20 using a while loop.
for i in range(20):
    i+=1
    if i%2==0:
        print(i)

print("----------")
print("Exercise #2: Divisibility")

denominator = int(input("Enter denominator: "))
numerator = int(input("Enter a numerator: "))

# Use a while loop here to repeatedly ask the user for
# a denominator for as long as the denominator is 0
# (or, put another way, until the denominator is not
# equal to 0).

while denominator == 0:
    denominator = int(input("Enter denominator: "))
    

print("----------")
print("Exercise #3: Average test score")

# Write a program that asks the user for three test scores. 
# The program should then report the average of these three scores.
# Solve this exercise using a for loop.

test_list=[100]
for i in range(3):
    test=float(input("What is your test score?"))
    test_list.append(test)
test_list.remove(100)

print("Your test score is ", sum(test_list)/3)


print("----------")
print("Exercise #4: How many names?")


# Some people have just a first name and a last name. 
# Some people also have a middle name. 
# Some people have five middle names.

# Write a program that asks the user how many names they have. 
# If they have a first name, two middle names, and a last name, for example, they would type 4. 
# Using a for loop, ask the user for each of their names. 
# Finally, print their full name.

rptnum = int(input("How many names do you have?"))
namelist = [" "]
for i in range(rptnum):
    name=input("What is your name?")
    namelist.append(name)
namelist.remove(" ")
print([namelist])


print("----------")
print("Exercise #5: Magic Number")
# Write a program that makes the user guess a particular number between 1 and 100. 
# Save the number to be guessed in a variable called magic_number.
# If the user guesses a number higher than the secret number, print "Too high!"". 
# If they guess a number lower than the secret number, print "Too low! " 
# Once they guess the number, say Correct!


num=84
trynum=int(input("What is your guess?"))

while trynum!=num:
    if num>trynum:
        print("Bigger.")
    elif num<trynum:
        print("Smaller.")
    else:
        print("Correct!")
        break