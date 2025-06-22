#Practice from our lesson in Variables
#1. Simple Calculator
angka1 = 10
angka2 = 5
def plus():
    return angka1 + angka2
def minus():
    return angka1 - angka2
def times():
    return angka1 * angka2
def divide():
    return angka1 / angka2
print("Summation Result:", plus())
print("Subtraction Result:", minus())
print("Nultiplication Result:", times())
print("Dividing Result:", divide())

#2 Personal Information
Name = "John"
Age = 30
City = "New York"
Job = "Software Engineer"

def personal_info():
    return f"Name: {Name}, Age: {Age}, City: {City}, Job: {Job}"
print("Personal Information:", personal_info())

#Try to change one of the variables and see how it affects the output
Age = 31
print(f"Now i turn {Age} years old")

#3 Conversion Units 
# Temperature Conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
#return f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit"
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")

#Distance Conversion
def kilometers_to_miles(kilometers):
    return kilometers * 0.621371
kilometers = 10
miles = kilometers_to_miles(kilometers)
print(f"{kilometers} Kilometers is equal to {miles} Miles")

# Weight Conversion
def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462
kilograms = 70
pounds = kilograms_to_pounds(kilograms)
print(f"{kilograms} Kilograms is equal to {pounds} Pounds")

#Volume Conversion
def liters_to_gallons(liters):
    return liters * 0.264172
liters = 5
gallons = liters_to_gallons(liters)
print(f"{liters} Liters is equal to {gallons} Gallons")

#4 Simple Calculating the area of a flat shape

def area_of_square(side):
    return side ** 2
side = 6
def area_of_rectangle(length, width):
    return length * width
def area_of_circle(radius):
    import math
    return math.pi * (radius ** 2)
def area_of_triangle(base, height):
    return 0.5 * base * height
length = 10
width = 5
radius = 7
base = 8
height = 4
print(f"Area of Rectangle: {area_of_rectangle(length, width)}")
print(f"Area of Circle: {area_of_circle(radius)}")
print(f"Area of Triangle: {area_of_triangle(base, height)}")
print(f"Area of Square: {area_of_square(side)}")

#5 Simple Interest Calculator
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
principal = 1000
rate = 5
time = 3
interest = simple_interest(principal, rate, time)
print(f"Simple Interest for Principal: {principal}, Rate: {rate}%, Time: {time} years is {interest}")
#6 Simple Voting Eligibility Check
def is_eligible_to_vote(age):
    return age >= 18
age = 20
if is_eligible_to_vote(age):
    print(f"At age {age}, you are eligible to vote.")
else:
    print(f"At age {age}, you are not eligible to vote.")
#7 Simple BMI Calculator
def calculate_bmi(weight, height):
    return weight / (height ** 2)
weight = 52  # in kilograms
height = 1.70  # in meters
bmi = calculate_bmi(weight, height)
print(f"Your BMI is {bmi:.2f}.")

