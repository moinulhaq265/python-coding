# Slicing -> to access part of string through indexing.

text = "Python"
print(text[0:3])    # Pyt  → index 0,1,2
print(text[2:])     # thon → from index 2 to end
print(text[:4])     # Pyth → from start to index 3


# Length -> it will returns the length of string, in terms of index it will gives the last index of string.


print(len("Hello"))   # 5


# Upper & Lower

text = "Hello"
print(text.upper())   # HELLO
print(text.lower())   # hello

# Concatenation (joining) -> addition of two or more strings.

first = "moin ul"
last = "haq"
full = first+ " " +last
print(full)

# Repetition -> you can repeate same thing again and again.

print ("Ha" * 3)

# Find & Replace

text = "I love Python"
print(text.find("Python"))      # 7  → starting index
print(text.replace("Python", "coding"))  # I love coding

# Strip (remove spaces)

text = "  Hello  "
print(text.strip())    # "Hello"
print(text.lstrip())   # "Hello  "
print(text.rstrip())   # "  Hello"

# Split

text = "apple,banana,mango"
print(text.split(","))   # ['apple', 'banana', 'mango']

# Check Content

print("hello".isalpha())    # True  → only letters
print("123".isdigit())      # True  → only digits
print("hello".startswith("he"))  # True
print("hello".endswith("lo"))    # True

# String Formatting 

name = "Moin Ul Haq"
age  = 23

# f-string (most modern way)
print(f"My name is {name} and I am {age} years old.")

# .format() method
print("My name is {} and I am {} years old.".format(name, age))