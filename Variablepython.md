Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.


Variable names with more than one word can be difficult to read.
There are several techniques you can use to make them more readable:

Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"


Python allows you to assign values to multiple variables in one line:
Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.



Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
Example
Create a variable outside of a function, and use it inside the function

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was, global and with the original value
To create a global variable inside a function, you can use the global keyword.



