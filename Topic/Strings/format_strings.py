# Format-Strings
# Format strings are a powerful feature in Python that allow you to create strings with dynamic content. They can be used to format numbers, dates, and other data types into a readable string format.
# They are especially useful for creating user-friendly output in applications, such as games or financial calculators

#1. F-Strings
# F-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces `{}`. They are prefixed with the letter `f` or `F`.
# Example:
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)  # Output: Hello, Alice! You are 30 years old.
# Example with Math Operations
height = 1.75
weight = 70
bmi = weight / (height ** 2)
bmi_message = f"{name}, your BMI is {bmi:.2f}."
print(bmi_message)  # Output: Alice, your BMI is 22.86.
#Example with functions
def calculate_area(radius):
    return 3.14 * radius ** 2
radius = 5
area_message = f"The area of a circle with radius {radius} is {calculate_area(radius):.2f}."
print(area_message)  # Output: The area of a circle with radius 5 is 78.50.

#2. Format Modifier
# Format modifiers are used to control how values are displayed in strings. They can specify number of decimal places, padding, alignment, and more.
# Example with Decimal Places
pi = 3.141592653589793
formatted_pi = f"Pi to 3 decimal places: {pi:.3f}"
print(formatted_pi)  # Output: Pi to 3 decimal places: 3.142
# Example with Padding and Alignment
name = "Bob"
age = 25
formatted_string = f"{name:<10} is {age:>3} years old."
print(formatted_string)  # Output: Bob        is  25 years old.
# Example with Multiple Format Modifiers
price = 19.99
formatted_price = f"Price: ${price:,.2f}"  # Comma as thousand separator, 2 decimal places
print(formatted_price)  # Output: Price: $19.99

#3. Methode .format()
# The `.format()` method is another way to format strings, allowing for more complex formatting options
# Example with Positional and Keyword Arguments
name = "Charlie"
age = 28
formatted_string = "Hello, {}! You are {} years old.".format(name, age)
print(formatted_string)  # Output: Hello, Charlie! You are 28 years old
# Example placehorders with index
formatted_string = "Hello, {0}! You are {1} years old. {0} is a great name!".format(name, age)
print(formatted_string)  # Output: Hello, Charlie! You are 28 years old
# Example Placeholder with name :
formatted_string = "Hello, {name}! You are {age} years old. {name} is a great name!".format(name=name, age=age)
print(formatted_string)  # Output: Hello, Charlie! You are 28 years old. Charlie is a great name!
# Example with modifiers
formatted_string = "Price: ${price:,.2f}".format(price=19.99)  # Comma as thousand separator, 2 decimal places
print(formatted_string)  # Output: Price: $19.99

# Additional Examples
# F-Strings with modifiers
value = 1234.56789
formatted_value = f"Formatted value: {value:,.2f}"  # Comma as thousand separator, 2 decimal places
print(formatted_value)  # Output: Formatted value: 1,234.57
# format() with placeholders
formatted_value = "Formatted value: {:,.2f}".format(value)  # Comma as thousand separator, 2 decimal places
print(formatted_value)  # Output: Formatted value: 1,234.57
# Combine number and text
number = 42
text = "The meaning of life"
formatted_combination = f"{text} is {number}."
print(formatted_combination)  # Output: The meaning of life is 42.
