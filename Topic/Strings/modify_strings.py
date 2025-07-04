# 1. Upper Case
x = "hello world"
y = x.upper()
print(y)

# 2. Lower Case
x = "HELLO WORLD"
y = x.lower()
print(y)

# 3. Strip Whitespace
x = "   hello world   "
y = x.strip()
print(y)

# 4. Split a String
x = "hello,world"
y = x.split(",")
print(y)

# 5. Join a List of Strings
x = ["hello", "world"]
y = ",".join(x)
print(y)

# 6. Replace a String
x = "hello world"
y = x.replace("world", "universe")
print(y)

# 7. Find the Index of a String
x = "hello world"
y = x.index("world")
print(y)

# 8. Check if a String Contains a Substring
x = "hello world"
y = "world" in x
print(y)