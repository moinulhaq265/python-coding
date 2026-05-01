                                               
                                                    #------ Easy Questions------


# Question 1

prices = [10, 20, 30]
double_prices = [prices[0]*2, prices[1]*2, prices[2]*2]
print (f"Original prices = {prices}")
print ("Doubled prices = ", double_prices)

# Question 2

alphabets = ["A", "B", "C", "D"]
alphabets [0] = "D"
alphabets [3] = "A"
print (alphabets)

# Question 3

colors = ["Red", "Blue", "Green"]
user_color = input("Enter a color : ")
if user_color in colors :
    print ("found")
else:
    colors.append(user_color)   
    print (f"{user_color} was not in the list, so I added ")
    print ("Updated list = ", colors)

# Question 4

food = ["Biryani", "Burger", 'Pizza', "Chines rice", "Palao"]
print (food)  # whole list
print (food[0])  # 1st element
print (food[-1])  # Last element

# Question 5

colors = ["red", "green", "blue", "yellow", "white"]
print (colors [2])
print (colors [3])
print (colors [-1])

# Question 6

countries = ["Pakistan", "UAE", "Canada", "China", "Iran", "Russia"]
print (len(countries))

# Question 7

# Add Items — Start with an empty list items = []. 
# Add 4 items to it using .append() and print the final list.
item = []
item.append("Fan")
item.append("Glass")
item.append("pen")
item.append("campus")

print (item)

# Question 8

numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print (numbers)


                                                          #------ Medium Questions ------


# Question 1

nums = [1, 2, 3, 4, 5]
print (nums[1:4])

# Question 2

# The fastest way to find unique items is to convert your list into a Set. 
# When you do this, Python automatically "throws away" all duplicates.

names = ["Ali", "Sara", "Ali", "Zoha", "Sara"]
unique_name = set(names) # type casting
unique_count = len(unique_name)
print("Original List:", names)
print("Unique Names Count:", unique_count)

# Question 3

data = [1, None, 3, None, 5]
data.remove(None)
data.remove(None)
print ("Cleared data ", data)

# Question 4

letters = ["a", "b", "c", "d", "e", "f", "g"]
first_3 = letters[0:3]
last_3 = letters[4:7]
Items_from_index_2_to_5 = letters[2:6]
print (first_3)
print (last_3)
print (Items_from_index_2_to_5)

# Question 5

num = [1,2,3,4,5]
num [2] = 99
print (num)

# Question 6

scores = [85, 42, 91, 67, 55, 78]
scores.sort()
print ("Ascending ", scores)
scores.sort (reverse=True)
print ("Descending ", scores)

# Question 7

# Check Item — Ask the user to enter a fruit name. Check if it exists in your fruits list and print:
fruit = ["mango", "apple", "cherry", "banana"]
user_fruit = input("Enter a fruit name :")
if user_fruit in fruit:
    print (f"{user_fruit} found in fruit")
else:
    print (f"{user_fruit} not found in fruit")

# Question 8

a = [1, 2, 3]
b = [4, 5, 6]
conc = a+b
print (conc)
print (a*3)



                                                          #----- Hard Questions -----



# Question 1

matrix = [[1, 2], [3, 4], [5, 6]]
matrix [1][1] = 40
extrected_row = matrix [1]
print (f"Updated matrix = {matrix}")
print (f"Extrecdet row = {extrected_row}")

# Question 2

letters = ['r', 'a', 'd', 'a', 'r']
palindrom = letters[::-1]
if letters == palindrom:
    print ("palindromic letters ",letters)
else:
    print (letters ," are not palindromic.")

# Question 3

numeric = [5,10,50,70,90]
addition = (sum(numeric))
average = (sum(numeric)/len(numeric))
print("sum = ", addition)
print ("average = ",average)

# Question 4

temps = [32, 45, 28, 61, 39, 55]
highest = max(temps)
print ("highest temprature is ",highest )
lowest = min(temps)
print ("Lowest temprature is ",lowest)

# Question 5

nums = [1, 2, 3, 2, 4, 2, 5]
count = nums.count(2)
print("List:", nums)
print("2 appears:", count, "times")

# Question 6

# Normal way (long)
squares = []
for x in range(1, 11):
    squares.append(x ** 2)
print("Normal way:", squares)

# List comprehension (short)
squares = [x ** 2 for x in range(1, 11)]
print("Comprehension:", squares)

