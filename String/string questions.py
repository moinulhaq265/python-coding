# Question 1:
# Store "Python" in a variable. Print the first, third, and last character.

text = "python"
print (text[0])
print (text[2])
print (text[5])
print (len(text))

# Question 2:
# Take "Hello World" and print it in all uppercase and all lowercase.

word = "Hello World"
print(word.upper())
print(word.lower())

# Question 3:
#  Store your first name and last name in two variables. Join them with a space and print.

first = "moin" 
last = "sahil"
full = first+ " " +last
print (full)

# Question 4
# Replace — Take "I love Java" and replace "Java" with "Python". Print the result.

text = "I love java"
print (text.replace("java","python"))

# Question 5
# f-string — Ask the user for their name, age, and city. Print:

name = input("Enter your name :")
age = int(input("Enter your age :"))
city = input("Enter your city :")
print (f"I am {name} I am {age} year old. I live in {city}")

# Question 6
# Palindrome Check — Ask the user to enter a word. Check if it reads the same forwards and backwards:

word = input("Enter a palindromic word :")
reversed_word = word[::-1]
if word == reversed_word:
    print("{} is palindrome".format(word))
else:
    print ("{} is not palindrome".format(word))

# Question 7
# Count Vowels — Write a program that counts how many vowels (a, e, i, o, u) are in a string.

text = input("Enter a sentence: ")
count = 0    # start counting from 0
vowels = "aeiou"

for letter in text:         # loop through each character
    if letter in vowels:    # check if letter is a vowel
        count = count + 1   # increase count by 1

print("Total vowels:", count)