# Python - More Classes and Objects

1. Why Python programming is awesome
Python is awesome for several reasons:

Readability and simplicity: Python's syntax is clear and easy to understand, making it an ideal language for beginners.
Versatility: It is used in various domains, such as web development, data science, artificial intelligence, automation, and more.
Large standard library: Python comes with a vast standard library that supports many common programming tasks.
Community support: A large and active community means plenty of resources, tutorials, and third-party packages available.
Interpreted language: Python is interpreted, meaning it executes code line by line, which is useful for debugging and development.

2. What is OOP
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data and code that manipulates that data. Key principles of OOP include:

Encapsulation: Bundling the data (attributes) and methods (functions) that operate on the data into a single unit or class.
Inheritance: Creating new classes from existing ones, allowing for hierarchical classification.
Polymorphism: The ability to use a single interface to represent different underlying forms (data types).
Abstraction: Hiding the complex implementation details and showing only the necessary features.

3. “First-class everything”
In Python, "first-class everything" means that all elements (functions, classes, modules, etc.) are first-class objects. This implies that they can be:

Assigned to a variable
Passed as an argument to a function
Returned from a function
Stored in data structures

4. What is a class
A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. For example:

python

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

5. What is an object and an instance
An object is an instance of a class. When a class is defined, no memory is allocated until an object is created from it. For example:

python

my_dog = Dog("Fido")
Here, my_dog is an instance (object) of the Dog class.

6. What is the difference between a class and an object or instance
A class is a blueprint or template for creating objects. An object (or instance) is a concrete occurrence of a class. For example:

Class: Dog
Object: my_dog = Dog("Fido")

7. What is an attribute
An attribute is a variable that is bound to an instance or class. Attributes can hold data or functions. For example, in the Dog class, name is an attribute.

8. What are and how to use public, protected and private attributes
Public attributes: Accessible from anywhere.
Protected attributes: Indicated by a single underscore (_), intended for internal use or subclass access.
Private attributes: Indicated by a double underscore (__), intended to prevent access from outside the class.
Example:

python

class MyClass:
    public_attr = "Public"
    _protected_attr = "Protected"
    __private_attr = "Private"

9. What is self
self is a reference to the current instance of the class and is used to access variables and methods associated with the class. It must be the first parameter of any method in the class.

10. What is a method
A method is a function that is defined within a class and is associated with an object. Methods typically operate on data contained within the instance.

11. What is the special init method and how to use it
__init__ is a special method called a constructor. It is called when an instance of the class is created, and it initializes the object's attributes.

python

class MyClass:
    def __init__(self, value):
        self.value = value

12. What is Data Abstraction, Data Encapsulation, and Information Hiding
Data Abstraction: Simplifying complex reality by modeling classes appropriate to the problem.
Data Encapsulation: Bundling data with methods that operate on that data.
Information Hiding: Restricting access to some of the object's components, which is achieved using private and protected attributes.

13. What is a property
A property in Python is a special kind of attribute that allows you to customize access methods (getters and setters) without changing the attribute access syntax.

python

class MyClass:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

14. What is the difference between an attribute and a property in Python
An attribute is a variable bound to an instance, while a property is a special attribute with getter and setter methods that provide controlled access.

15. What is the Pythonic way to write getters and setters in Python
Using the @property decorator for getters and the @property_name.setter decorator for setters.

python

class MyClass:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

16. What are the special str and repr methods and how to use them
__str__: Returns a readable, informal string representation of an object, used by print().
__repr__: Returns an official string representation of an object, used by repr() and the interactive interpreter.
python

class MyClass:
    def __str__(self):
        return "Readable String"
    
    def __repr__(self):
        return "Official String"

17. What is the difference between str and repr
__str__ is meant to be readable and user-friendly, while __repr__ is meant to be unambiguous and useful for developers.

18. What is a class attribute
A class attribute is a variable that is shared across all instances of a class. It is defined within the class but outside any instance methods.

python

class MyClass:
    class_attr = "Class Attribute"

19. What is the difference between an object attribute and a class attribute
Object attribute: Defined within methods and unique to each instance.
Class attribute: Shared among all instances of the class.

20. What is a class method
A class method is a method that is bound to the class and not the instance. It is defined using the @classmethod decorator and takes cls as its first parameter.

python

class MyClass:
    @classmethod
    def class_method(cls):
        pass

21. What is a static method
A static method is a method that does not receive an implicit first argument (like self or cls). It is defined using the @staticmethod decorator.

python

class MyClass:
    @staticmethod
    def static_method():
        pass

22. How to dynamically create arbitrary new attributes for existing instances of a class
You can dynamically add new attributes to an instance using dot notation.

python

instance = MyClass()
instance.new_attr = "New Attribute"

23. How to bind attributes to objects and classes
Attributes can be bound directly by assigning values to them.

python

# For an instance
instance.attr = "Instance Attribute"

# For a class
MyClass.class_attr = "Class Attribute"

24. What is and what does contain dict of a class and of an instance of a class
__dict__ is a dictionary or other mapping object used to store an object's (writable) attributes. For classes and instances, it contains all their attributes and methods.

python

instance.__dict__
MyClass.__dict__

25. How does Python find the attributes of an object or class
Python uses the method resolution order (MRO) to find attributes. It first looks in the instance’s __dict__, then in the class’s __dict__, and then in the base classes.

26. How to use the getattr function
getattr is used to retrieve the value of an attribute of an object.

python

value = getattr(instance, 'attribute_name', default_value)
