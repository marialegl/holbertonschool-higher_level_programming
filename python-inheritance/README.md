# Python inheritance

1. What is a superclass, base class, or parent class?

A superclass (also called a base class or parent class) is a class that is inherited by another class. It provides methods and attributes that can be used or overridden by the subclass (or child class). This promotes code reuse and a hierarchical class structure.

2. What is a subclass?

A subclass (or child class) is a class that inherits from another class, known as the superclass or base class. The subclass can inherit attributes and methods from the superclass and can also have additional attributes and methods of its own. It can also override methods and attributes from the superclass.

3. How to list all attributes and methods of a class or instance?

You can use the built-in dir() function to list all attributes and methods of a class or instance. For example:
python

class MyClass:
    def __init__(self):
        self.attribute = 1
    def method(self):
        pass

obj = MyClass()
print(dir(MyClass))  # Lists attributes and methods of the class
print(dir(obj))      # Lists attributes and methods of the instance

4. When can an instance have new attributes?

An instance can have new attributes anytime after it is created, typically through the __init__ method or by directly assigning a value to a new attribute. For example:
python

class MyClass:
    def __init__(self):
        self.initial_attr = 10

obj = MyClass()
obj.new_attr = 20  # Adding a new attribute to the instance

5. How to inherit a class from another?

To inherit a class from another, you define the subclass and specify the superclass in parentheses. For example:
python

class SuperClass:
    pass

class SubClass(SuperClass):
    pass

6. How to define a class with multiple base classes?

You can define a class with multiple base classes by listing all the base classes in parentheses, separated by commas. This is known as multiple inheritance. For example:
python

class Base1:
    pass

class Base2:
    pass

class Derived(Base1, Base2):
    pass

7. What is the default class every class inherits from?

In Python, every class implicitly inherits from the object class if no other superclass is specified. This is the base class for all new-style classes.
python

class MyClass:
    pass

# MyClass implicitly inherits from object

8. How to override a method or attribute inherited from the base class?

To override a method or attribute inherited from the base class, you simply define a method or attribute with the same name in the subclass. For example:
python

class SuperClass:
    def method(self):
        print("Superclass method")

class SubClass(SuperClass):
    def method(self):
        print("Subclass method")

obj = SubClass()
obj.method()  # Outputs: Subclass method

9. Which attributes or methods are available by inheritance to subclasses?

All public and protected attributes and methods of the superclass are available to the subclass by inheritance. Private attributes (those prefixed with double underscores) are not directly accessible but can be accessed using name mangling.

10. What is the purpose of inheritance?

The purpose of inheritance is to promote code reuse and logical hierarchy in object-oriented programming. It allows a new class to use the properties and behavior of an existing class without duplicating code, thus making the code more modular and easier to maintain.

11. What are, when and how to use isinstance, issubclass, type, and super built-in functions?

* isinstance(object, classinfo): Checks if an object is an instance of a class or a tuple of classes. Useful for type checking.

python

isinstance(5, int)  # True

* issubclass(subclass, superclass): Checks if a class is a subclass of another class or a tuple of classes.

python

issubclass(bool, int)  # True
type(object): Returns the type of an object. Can be used to get the class of an instance.

python

type(5)  # <class 'int'>

* super(): Returns a temporary object of the superclass used to call its methods. Commonly used in method overriding to call the superclass’s method.

python

class SuperClass:
    def method(self):
        print("Superclass method")

class SubClass(SuperClass):
    def method(self):
        super().method()
        print("Subclass method")

obj = SubClass()
obj.method()
# Outputs:
# Superclass method
# Subclass method