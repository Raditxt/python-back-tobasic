#Data Types
#Built-in Data Types
# 1 Text Type
# String
name = "Karin"
message = f"Halo, {name}! Welcome."
print(message)
# Reversing a String
name_input = input("Enter your name: ")
print("Reverse Name:", name_input[::-1])
# 2 Numeric Types
# Integer, Float, Complex
x = 10       # int
y = 3.14     # float
z = 1 + 2j   # complex

print("Summation:", x + y)
print("Float to int conversion:", int(y))
print("Complex Number:", z.real, z.imag)

# Circle area calculation
radius = float(input("Insert the radius of the circle : "))
area = 3.14159 * (radius ** 2)
print("Circle area:", area)

# 3 Sequence Types
# List, Tuple, Range
fruits = ["apple", "banana", "cherry"] # list
numbers = (1, 2, 3) # tuple
range_numbers = range(2,10) # range

print("List:", fruits)
print("Tuple:", numbers)
print("Range:", list(range_numbers))

#List 1-10 and print even number use range
even_numbers = list(range(2, 11, 2))
print("Even Numbers from 1 to 10:", even_numbers)

# 4 Mapping Types
students = {"name": "Karin", "age": 20, "Major": "Math", "Grade": 3.9}  # dict
print("name:", students["name"], "age:", students["age"], "Major:", students["Major"], "Grade:", students["Grade"])

#Dictionary to store test scores and calculate the average
test_scores = {"Math": 85, "Science": 90, "English": 78}
average_score = sum(test_scores.values()) / len(test_scores)
print("Test Scores:", test_scores)

# 5 Set Types
# Set, Frozen Set
set1 = {1, 2, 3, 4, 5}  # set
set2 = frozenset([6, 7, 8, 9, 10])  # frozenset (immutable set)
print("Set:", set1)
print("Frozen Set:", set2)
# Find the intersection of two sets
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Intersection:", set(list1).intersection(list2))

# 6 Boolean Type (bool)
x = 10
y = 20
print ("x > y?", x > y) 
print("bool(0):", bool(0))  # False

#Check for even or odd number
number = int(input("Enter a number: "))
print("Is the number even?", number % 2 == 0) 

#7 Binary Types
# Bytes, Bytearray, Memoryview
byte_data = b"Hello, World!"  # bytes
bytearray_data = bytearray(b"Hello, World!")  # bytearray
print("Bytes:", byte_data)
print("Bytearray:", bytearray_data)

# Change string to bytes
text = "Python"
byte_text = text.encode()
print("String to Bytes:", byte_text)
print("Bytes to String:", byte_text.decode())

#8 None Type (None)
def search_data(id):
    if id == 0:
        return {"name": "Karin", "age": 20}
    else:
        return None
print("Search Result:", search_data(0))  # Returns a dictionary

