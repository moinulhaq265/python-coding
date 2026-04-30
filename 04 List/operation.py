# 1. Indexing (Accessing Items)

# Lists are ordered, and every item has a specific "address" called an index.
# Positive Indexing: Starts from 0 (left to right).
# Negative Indexing: Starts from -1 (right to left).

Fruits = ["mango", "banana", "cherry"]
print (Fruits)
print (Fruits[0]) #mango
print (Fruits[-1]) #cherry

# 2. Slicing (Grabbing a Range)

# Just like with strings, you can pull out a "sub-list" using the syntax [start : stop : step].
# Start: The index where the slice begins (inclusive).
# Stop: The index where the slice ends (exclusive—it doesn't include this item).

nums = [0, 10, 20, 30, 40]
print (nums) # original list
print (nums [0:4]) # [0, 10, 20, 30] (indices 1,2 and 3)
print (nums [:3]) # [0, 10, 20] (from 0 2)
print (nums [::2]) # [0, 20, 40] (every second item)

# 3. Concatenation and Repetition

# You can use math operators to join or multiply lists.
# + (Concatenation): Glues two lists together into a new one.
# * (Repetition): Repeats the list a certain number of times.

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print (list_a + list_b)
print (list_a * 3)

# 4. Membership Testing

# This is a very "English-like" feature of Python. 
# You can check if an item exists inside a list using in or not in. It returns a Boolean (True or False).

users = ["moin", "sami", "naveed"]
print ("moin" in users)
print ("zara" in users)

# 5. Updating an Item (Assignment)

# Because lists are mutable, you can use the index to swap an item out for a new one.

colors = ["Red", "Blue", "Green"]
colors [0] = "Yellow"
print (colors) # Output: ["Yellow", "Blue", "Green"]
