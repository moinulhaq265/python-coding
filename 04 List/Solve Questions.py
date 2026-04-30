# Question 1

#The Index Swap: Create a list of 5 colors. 
# Change the 3rd color to "Yellow" and print the last item using negative indexing.

colors = ["Red", "Green", "Pink", "Indigo", "white"]
colors [3] = "Yellow" # To change the color at 3rd
print (colors) 
print (colors[-1]) # to print last element

#Question 2

#Slicing Challenge: Create a list of numbers from 0 to 10. 
# Extract a sub-list containing only [3, 4, 5, 6] using slicing.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Sub_list = ( nums [3:7])
print ("Sub list = ", Sub_list)

# Question 3

#The Mixer: Create two lists, list_a = [1, 2, 3] and list_b = ["A", "B", "C"]. 
# Combine them into a single list called combined_list without using a loop.

list_a = [1, 2, 3]
list_b = ["A", "B", "C"]
Combined_list = list_a + list_b
print ("Combined List = ", Combined_list)

# Question 4 

# The Guest List:
# Create an empty list called guests.
# Add "Moin", "Sami", and "Zara" using .append().
# Add "Sahil" at the very beginning of the list using .insert().
# Add ["Babar", "Hania"] all at once using .extend().

Guest = []
Guest.append ("Moin")
Guest.append ("Sami")
Guest.append ("Zara")
Guest.insert (0, "Sahil")
guest = ["Babar", "Hania"]
Guest.extend (guest)
print (Guest)

# Question 5
 
# Removing Items:
# From your guests list, remove "Zara" by his name.
# Remove the last person in the list and store their name in a variable called left_early.
# Remove the person at index 1 using the del keyword.

Left_Early = "Zara"
Guest.remove ("Zara")
del Guest [1]
print (Guest)
print ("Left early = ", Left_Early)

# Question 6

# Stats Checker: Given the list prices = [120, 50, 270, 90, 100], 
# find the highest price, the lowest price, and the total sum of all prices using Python's built-in functions.

prices = [120, 50, 270, 90, 100]
highest_price = max(prices)
lowest_price = min(prices)
sum_of_pricec = sum(prices)

print ("Highest price = ", highest_price)
print ("Lowest price = ",lowest_price)
print ("Sum of prices = ", sum_of_pricec)

# Question 7

# Search & Count: Create a list containing several repeated names (e.g., ["Ali", "Zoe", "Ali", "Khan", "Ali"]).
# Find how many times "Ali" appears in the list.
# Find the index of the first "Zoe".

users = ["Ali", "Zoe", "Ali", "Khan", "Ali"]
ali_repeat= users.count("Ali")
position_of_zoe = users.index("Zoe")

print (users)
print ("Ali repeated ", ali_repeat, "times")
print ("Position of zoe spotted at index", position_of_zoe)

