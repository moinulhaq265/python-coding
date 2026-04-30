# 1. Adding Items (Growing the List)
# There are three main ways to add data, depending on where and how you want to add it.

# .append(value): Adds a single item to the very end of the list.

cart = ["Bread", "Eggs"]
cart.append ("Sugar")
print (cart)

# .insert (index, value)

cart.insert(1, "Butter") 
print (cart) # Result: ["Bread", Butter", "Eggs", "Sugar"]

# .extend (another list)

snacks = ["Chips", "Soda"]
cart.extend (snacks)
print (cart) # Result : ["Bread", "Butter", "Eggs", "Sugar", "Chips", "Soda"]

# 2. Removing Items (Shrinking the List)

# Python provides different tools depending on whether you know the value you want to remove or the position (index) it's in.

# .remove(value): Searches for the first occurrence of a value and deletes it.
cart.remove ("Eggs")
print (cart)

# .pop(index): Removes the item at a specific index and returns it (so you can save it to a variable). 
# If you don't provide an index, it removes the last item.

last_item = cart.pop(6) # Remove "Soda"
first_item = cart.pop(0) # Remove "Bread"
print (cart)

# del keyword: A powerful way to delete a specific item or a whole slice.

del cart[0]
print (cart)

# .clear(): Wipes the entire list clean, leaving you with an empty [].

cart.clear()
print (cart)

# 3. Modifying by Assignment

# As we touched on in basic operations, you can use the = sign to replace items directly.

task = ["Clean", "Cook", "Sleep"]
task [1] = "Code"
print (task)