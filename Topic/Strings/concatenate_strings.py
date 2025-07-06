# String Concatenation
# Concatenation is the process of joining two or more strings together.
# This is often used to create longer strings or to combine different pieces
# of information into a single string.

# 1. Combine Two Strings
x = "Hello"
y = "World"
z = x + " " + y  # Using the + operator
print(z)  # Output: Hello World
# Add Space or Punctuation
z = x + ", " + y + "!"  # Adding punctuation and space
print(z)  # Output: Hello, World!

# 2. Combine String with Variable
name = "Alice"
greeting = "Hello, " + name + "!"  # Using variable in concatenation
print(greeting)  # Output: Hello, Alice!

# Combine String with Number
age = 30
age_message = "I am " + str(age) + " years old."  # Convert number to string
print(age_message)  # Output: I am 30 years old.

# Basic error
# Error : Cannot concatenate str and int
# age_message = "I am " + age + " years old."  # This will raise an error
# print(age_message)  # Uncommenting this line will raise TypeError

# Solution: Convert the number to a string using str()
# age_message = "I am " + str(age) + " years old."  # Correct way
# print(age_message)  # Output: I am 30 years old.


