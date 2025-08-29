print("Exercise #1: Rolling Dice")
print(" ")

# Write a program that will print out all combinations that can be made when 2 dice are rolled.
dice1=1
dice2=1
print(dice1,dice2)

for i in range(6):
    for i in range(5):
        dice2+=1
        print(dice1, dice2)
    if dice1 == 6 and dice2 == 6:
        break
    dice1+=1
    dice2=1
    print(dice1,dice2)
    

print(" ")
print("----------")
print(" ")

print("Exercise #2: Categories")
# Write a program that asks the user for three categories
# For each category, ask the user for three things in that category
# Print something for each category that states the category and the three things in that category
print(" ")

ct1=input("Type in category one : ")
ct11= input("Item #1 : ")
ct12= input("Item #2 : ")
ct13= input("Item #3 : ")

print(" ")

ct2=input("Type in category two : ")
ct21= input("Item #1 : ")
ct22= input("Item #2 : ")
ct23= input("Item #3 : ")
print(" ")

ct3=input("Type in category three : ")
ct31= input("Item #1 : ")
ct32= input("Item #2 : ")
ct33= input("Item #3 : ")

print(" ")

print("Category one : ", ct1)
print(" 1. ", ct11)
print(" 2. ", ct12)
print(" 3. ", ct13)

print(" ")

print("Category two : ", ct2)
print(" 1. ", ct21)
print(" 2. ", ct22)
print(" 3. ", ct23)

print(" ")

print("Category three : ",  ct3)
print(" 1. ", ct31)
print(" 2. ", ct32)
print(" 3. ", ct33)