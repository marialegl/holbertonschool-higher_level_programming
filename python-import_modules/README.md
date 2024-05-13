# Python - import & modules

1. Why Python programming is awesome?

Python is awesome for several reasons. It's a high-level, easy-to-learn programming language, making it ideal for both beginners and professionals. It has a clear and readable syntax that encourages clean and understandable code. Additionally, it has a wide variety of libraries and frameworks that make it very versatile and useful for a wide range of applications, from web development to data analysis and machine learning.


2. How to import functions from another file?

You can import functions from another file in Python using the import statement. For example:
python

from file_name import function_name


3. How to use imported functions?

After importing the function, you can use it just like you would with any other function defined in your own Python file. Simply call it by its name, followed by parentheses if it requires arguments.


4. How to create a module?

A module in Python is simply a file containing Python code. To create a module, write your code in a .py file and save it with the name you want for your module.


5. How to use the built-in function dir()?

The dir() function is used to get a list of names defined in a module or the current namespace. You can use it without arguments to get the names defined in the current scope, or with an object as an argument to get the attributes and methods available for that object.


6. How to prevent code in your script from being executed when imported?

You can prevent code in your script from being executed when imported using the global variable __name__. For example:
python

if __name__ == "__main__":
    # This code will only execute if this file is run directly, not if it's imported as a module.


7. How to use command line arguments with your Python programs?

You can use the sys.argv module to access command line arguments in your Python script. For example:
python

import sys

arguments = sys.argv
# arguments[0] is the name of the script
# arguments[1:] contains the arguments passed on the command line
