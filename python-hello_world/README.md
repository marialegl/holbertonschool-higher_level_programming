Python - Hello, World

Learning Objectives

1. How to use the Python interpreter: 
To use the Python interpreter, simply open a terminal or command line and type python. This will take you to the interactive Python interpreter where you can write and execute Python code directly.

2. How to print text and variables using print: 
You can print text and variables in Python using the print() function. For example:
python

text = "Hello, world!"
number = 42
print(text)
print("The number is:", number)

3. How to use strings: 
Strings are sequences of characters in Python and can be defined using single or double quotes. You can concatenate strings using the + operator, and you can also access individual characters using indexing. For example:
python

string = "Python"
print(string[0])  # Prints 'P'
print(string[1:4])  # Prints 'yth'

4. What are indexing and slicing in Python:
 Indexing refers to accessing individual elements within a sequence, such as a string or list, using a numerical index. Slicing refers to obtaining subsets of a sequence using the notation [start:end:step].


5. What is the official Python coding style and how to check your code with pycodestyle: 
The official Python coding style is described in PEP 8. Pycodestyle is a tool you can use to check if your code follows the PEP 8 style conventions. You can install it via pip (pip install pycodestyle) and then run it on your Python code to check the style. For example:

pycodestyle my_script.py