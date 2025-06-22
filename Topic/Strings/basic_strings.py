#1. Basic of make a string
s1 = "Hello, World!"  # Using double quotes
print(s1)  # Output: Hello, World!
s2 = 'Hello, World!'  # Using single quotes
print(s2)  # Output: Hello, World!

#Quotes inside quotes
s3 = "She said, 'Hello!'"  # Double quotes with single quotes inside
s4 = 'She said, "Hello!"'  # Single quotes with double quotes inside
print(s3)  # Output: She said, 'Hello!'
print(s4)  # Output: She said, "Hello!"
# Basic mistake
#s5 = "Hello, World!  # Missing closing quote
# print(s5)  # This will cause a syntax error
s6 = 'She said, "python is great!"' #this is correct
print(s6)  # Output: She said, "python is great!"

#2. Penugasan String to Variable
name = "Alice"  # Assigning a string to a variable
greeting = f"Welcome, {name}!"  # Using f-string for formatting
print(greeting)  # Output: Welcome, Alice!

#3. Multiline Strings
# Using triple quotes for multiline strings
song = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky."""
print(song)

#Multiple lines with single quotes
address = '''123 Main St,
Suite 100,
Springfield,
IL 62701'''
print(address)