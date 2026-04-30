                                               
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