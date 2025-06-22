#Global Variables
#This is a global variable
x = "awesome"

def myfunc():
    #This is a local variable
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
print("Python is " + x)

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside that function.
#Local variables have a local scope, which means that they can only be accessed inside the function where they are declared.
#This is a global variable
x = "awesome"
def myfunc():
    #This is a local variable
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

#Global Keyword
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#The global keyword makes the variable x available outside of the function, so it can be used as a global variable. 
#If you use the global keyword, the variable will be available outside the function, and it will be a global variable.
#If you do not use the global keyword, the variable will be a local variable, and it will not be available outside the function.
#This is a global variable
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#The global keyword is used to create a global variable inside a function.
#Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
