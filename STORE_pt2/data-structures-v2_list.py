print("Exercise 1: Find max value")
# Write the function max_int_in_list that takes a list of ints 
# and returns the biggest int in the list



my_list=[]

     
def max_int_in_list():
    my_list.sort()
    print("Max value = ", my_list[-1])

def make_list():
    global x
    x=int(input("How many values are you gonna put?"))
    for i in range(x):
        num=int(input("Type a number for your list:"))
        my_list.append(num)
    max_int_in_list()
        
        
make_list()

print(" ")
print("-----------")
print(" ")

print("Exercise #2: Exclamation points")
# Update this function so it replaces all lowercase 'i's in `text` with '!'

# 1. Convert the initial string to a list
# 2. Use a for loop to go through your list element by element
# 3. Whenever you see a lowercase i, replace it with an exclamation point in the list
# 4. Return the stringified version of the list when your for loop is finished

text=(input("Type any text : "))

def exclamation(text):
    # return text
    text.replace('i','!')
    # text1=list(text)
    # text1.replace
    return(text.replace('i','!'))

print(exclamation(text))

print(" ")
print("-----------")
print(" ")

print("Exercise #3: Remove, sort, reverse")
# Complete the remove_sort_reverse function

mylist=input("Type anything")
mylist2=mylist.split()
print (mylist2)

def remove_sort_reverse(mylist2):
    # perform operations on `my_list` to 
    # 1. remove all "eggplant"
    # 2. sort it
    # 3. reverse it!
    mylist2.remove("eggplant")
    mylist2.sort()
    mylist2.reverse()
    return mylist2
    
remove_sort_reverse(mylist2)
print(mylist2)