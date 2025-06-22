#Tyoe Casting
# Casting is the process of converting one data type to another.
# This is often necessary when you want to perform operations that require specific data types.
# 1. Int - Change integer to float or string
# from float
x = int(3.14)
y = int(5.99)

# from string
z = int("137")
w = int("242", 2)  # Base 2 (binary)

# Wrong casting example
# from string with non-numeric characters
try:
    int("137abc")
except ValueError:
    print("Cannot convert '137abc' to int")

#2. float - Chaange integer, float, or string to decimal
# from integer
a = float(7)
n = float(-14)

#from string
v = float("3.14")
s = float("343")

# Wrong casting example : String with non-numeric characters
try:
    float("3.14abc")
except ValueError:
    print("Cannot convert '3.14abc' to float")

#3. str() - Change to string
# from integer
q = str(213)
w = str(-42)

# from float
e = str(3.14)

# from boolean
f = str(True)
g = str(False)
b = str(None)

# from kompleks
