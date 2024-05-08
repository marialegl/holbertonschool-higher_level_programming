# Python - if/else, loops, functions

Learning Objectives

1. Why is indentation so important in Python?
Indentation in Python is crucial because it defines the block of code. Instead of using braces or keywords like "begin" and "end" as in other languages, Python uses indentation to structure its code. This makes the code more readable and easy to understand.

2. How to use if, if ... else statements?
if statements are used to execute a block of code if a condition is true. The basic form is:
python

if condition:
    # code to execute if the condition is true
if ... else is used to execute one block of code if the condition is true and another block if the condition is false:
python

if condition:
    # code to execute if the condition is true
else:
    # code to execute if the condition is false

3. How to use comments?
In Python, comments are created using the # symbol. Anything following # on a line is considered a comment and is ignored during program execution.

4. How to assign values to variables?
In Python, you can assign values to variables using the assignment operator =. For example:
python

variable = value

5. How to use while and for loops?
while is used to repeatedly execute a block of code as long as a condition is true.
for is used to iterate over a sequence (such as a list, tuple, range, etc.) and execute a block of code for each element in the sequence.

6. How to use break and continue statements?
break is used to exit a loop before its completion.
continue is used to skip the rest of the code in an iteration and move to the next iteration of the loop.

7. How to use else clauses on loops?
In Python, you can use the else clause in a loop to execute a block of code after the loop completes without being interrupted by a break.

8. What does the pass statement do, and when to use it?
The pass statement does nothing. It is used when the syntax requires a statement but no operation is needed. It's useful as a placeholder when writing provisional code or to create incomplete classes and functions.

9. How to use range?
range() is used to generate a sequence of numbers. You can specify the start, end, and step of the sequence. It's commonly used in for loops. For example:
python

for i in range(1, 10, 2):
    print(i)
This will print numbers from 1 to 9, stepping by two.

10. What is a function and how do you use functions?
A function is a reusable block of code that performs a specific task. It's defined using the def keyword, followed by the function name and parentheses that may contain arguments. For example:
python

def my_function(argument):
    # function code
    return result
The function is called simply using its name and passing any necessary arguments.

11. What does a function return that does not use any return statement?
If a function doesn't use a 'return' statement, it automatically returns 'None'.

12. Scope of variables
The scope of a variable is the part of the code where the variable is accessible. In Python, variables can have local, global, or function scope, determining where the variable can be accessed and where it cannot.

13. What’s a traceback?
A traceback is an error report that shows the call stack of functions that led to the error. It contains useful information for diagnosing and troubleshooting issues in the code.

14. What are the arithmetic operators and how to use them?
The arithmetic operators in Python are +, -, *, /, // (integer division), % (modulo), and ** (exponentiation). They are used to perform basic mathematical operations between operands. For example:
python

sum = 2 + 3
difference = 5 - 2
product = 2 * 4
division = 10 / 2