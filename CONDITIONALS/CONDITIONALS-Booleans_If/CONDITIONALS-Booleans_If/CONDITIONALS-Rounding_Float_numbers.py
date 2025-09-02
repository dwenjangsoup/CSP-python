print("Exercise #1: Correct portion")
# This program computes how many tons of food each person in a group should take based on how many total tons of food the group has and how many people are in the group. It then asks the user how much food they took.

# Fix this program by making it compare rounded versions of the two floats. 
# Round to five decimal places in each case.

# Amount of food and number of people
tons_of_food = 0.07
num_people = 25
print("Amount of food(tons) :", tons_of_food)
print("Number of people :", num_people)

# Determine how much food each person gets
tons_of_food_per_person = tons_of_food / num_people
tofpp=round(tons_of_food_per_person,5)
print("=", tons_of_food_per_person,"=>",tofpp)

# Ask the user how much food they took
tons_taken = float(input("How many tons of food did you take? "))
if tons_taken == tofpp:
    print("Good job, you took the right amount of food!")
else:
    print("You took the wrong amount of food!")