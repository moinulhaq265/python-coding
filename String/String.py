# A string is a sequence of characters enclosed in quotes. It can contain letters, numbers, spaces, and symbols.

name = "Moin ul haq"           # double quotes
city = 'Kohistan'       # single quotes
msg  = """Hello
World"""               # multi-line string
print (name)
print (city)
print (msg)

# String is a Sequence 🔍
# Every character in a string has an index (position) starting from 0:

# H  e  l  l  o
# 0  1  2  3  4 
word = "Hello"
print(word[0])    # H
print(word[1])    # e
print(word[4])    # o


# Negative Indexing
#  H   e   l   l   o
# -5  -4  -3  -2  -1
word = "Hello"
print(word[-1])   # o  → last character
print(word[-2])   # l  → second last