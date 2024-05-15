# Python - More Data Structures: Set, Dictionary


1. Why Python programming is awesome?
Python is awesome because of its clean and readable syntax, extensive library support, and versatility. It's easy to learn and use, making it ideal for both beginners and professionals.

2. What are sets and how to use them?
Sets in Python are unordered collections of unique elements. You can create a set using curly braces {} or the set() function. For example:

python

my_set = {1, 2, 3}

3. What are the most common methods of sets and how to use them?
Some common methods include add(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), and symmetric_difference(). For example:
python

my_set.add(4)
my_set.remove(2)

4. When to use sets versus lists?
Use sets when you need to store unique elements and don't care about order. Use lists when you need an ordered sequence of elements and duplicates are possible.

5. How to iterate into a set?
You can iterate over a set using a for loop. For example:

python

for item in my_set:
    print(item)

6. What are dictionaries and how to use them?
Dictionaries are collections of key-value pairs. You can create a dictionary using curly braces {} or the dict() function. For example:
python

my_dict = {'a': 1, 'b': 2, 'c': 3}

7. When to use dictionaries versus lists or sets?
Use dictionaries when you need to associate values with unique keys. Use lists when you only need an ordered collection of elements and don't need keys. Use sets when you only need to store unique elements without keys.

8. What is a key in a dictionary?
A key in a dictionary is a unique identifier used to access a specific value in the dictionary.

9. How to iterate over a dictionary?
You can iterate over a dictionary using a for loop over the keys or the key-value pairs. For example:

python

for key in my_dict:
    print(key, my_dict[key])

10. What is a lambda function?
A lambda function is an anonymous, small function defined without a name using the lambda keyword. They are mainly used for simple operations and can be used in places where a function is required.

11. What are the map, reduce, and filter functions?

*map(): Applies a function to each item in a sequence and returns a list of the results.
*reduce(): Applies a function to pairs of items in a sequence to reduce them to a single value.
*filter(): Filters elements of a sequence based on a test function and returns a list of the elements that pass the test.
