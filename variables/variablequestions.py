#Create variables for your name, age, and city. Print them all.
name = "moin ul haq"
age = 23
city = "Kohistan"
print ("my name is :", name)
print ("I am ",age ,"years old")
print ("I am from ", city)

#  Store a = 5 and b = 10, then swap their values and print both.
a = 5
b = 10
temp = b
b = a
a = temp
print ("a = :",a)
print ("b = :",b)  

# Assign x = y = z = 100 and print all three. What do you notice?
x = y = z = 100
print(x)
print (y)
print (z)

# Start with score = 0, then add 10 to it three times and print after each step.
score = 0
print ("Starting score:", score)

score += 10        # same as score = score + 10
print ("After step 1:", score)

score += 10
print ("After step 2:", score)

score += 10
print ("After step 3:", score)

# Simple Interest — Store principal, rate, and time as variables. Calculate:
principal = 10000
rate = 8          # 8% interest rate (just a simple number)
time = 1          # 1 year

# formula -> interest = (principal * rate * time) / 100
interest = (principal * rate * time) / 100

print ("Principal:", principal)
print ("Rate:", rate, "%")
print ("Time:", time, "year")
print ("Simple Interest:", interest) 

# Start with x = "hello", print it, then change it to x = 99, print again. Notice how Python allows changing the type!
x = "Hello"
print ("x starts as:", x)

temp = x          # temp stores "Hello"
x = 99            # x is now reassigned to 99
print ("x after reassign:", x)
print ("temp still holds:", temp)

#  Store the value of PI = 3.14159 and radius r = 7. Calculate the area of a circle:
pi = 3.14
radius = 7
area = pi * radius * radius
print ("Area of the circle is :", area)

# Store a number, double it, subtract 5, divide by 3, and print the final result — all using one variable n.
n = 10
print ("originally n hpldes :", n)
n = n * 2
print ("n after double :", n)
n = n - 5
print ("n after subtracted by 5 :", n)
n = n / 3
print ("n after divided by 3 :", n)


# Ask the user to enter their name and birth year. Store them in variables, calculate their age, and print:
name = (input ("Enter your name :"))
age = (int (input ("Enter your birth year :")))
age = 2026 - age
print ("Hello ", name,"! you are ", age, "years old")

# Temp Converter — Store a Celsius value in a variable and convert it to Fahrenheit:
temp_in_celsis = 37
temp_in_fahrenhite = (temp_in_celsis * 9/5) + 32
print ("37 degree celsis =",temp_in_fahrenhite,"F")