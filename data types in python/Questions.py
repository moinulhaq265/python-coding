#  Take a string "42" and convert it to an integer, then multiply it by 5.
num_string = "42"
num_string = int(num_string)
print(num_string * 5)

# Ask the user to enter a decimal number (like 3.99), convert it to an integer, and print the result. What do you notice?
num_decimal = float(input("Enter a decimal number: "))
num_decimal = int(num_decimal)
print(num_decimal)
print(type(num_decimal))

#  Take two numbers a = 10 and b = 20, convert them to strings, and concatenate them (join them). What's the output vs adding them as integers?
a = 10
b = 20
a = str(a)
b = str(b)
print(a + b)
print(type(a + b)) # 1020 is the output as string

# doing same thing again but this time as integer to check the defferance btween these two operations
a = int(a)
b = int(b)
print (a + b)
print (type(a + b)) # 30 is the output as integer

#  Convert 0, 1, -5, and 100 to boolean. Print all results and explain the pattern.
print (bool (0))  # false
print (bool (1))  #True
print (bool (-5)) #True
print (bool (100)) #True

# Take "3.14" and convert it to a float, then compute its square.
pi_string = "3.14"
pi_float = float(pi_string)
square = pi_float**2
print ("original :", pi_string)
print ("float number after typecasting :", pi_float)
print (type(pi_float))
print ("square :", square)