# python-classes

1. What is OOP?
OOP, or Object-Oriented Programming, is a programming paradigm based on the concept of "objects". In OOP, objects are instances of classes that encapsulate related data and behaviors.

2. "First-class everything"
This phrase refers to the concept that in some programming languages, such as Python, everything is an object and can be manipulated as such. This means that functions, classes, and other elements are treated as first-class objects and can be passed as arguments, assigned to variables, etc.

3. What is a class?
A class is a blueprint or template for creating objects. It defines the attributes and methods that objects created from it will have.

4. What is an object and an instance?
An object is an instance of a class. When you create an object using a class, you are instantiating that class, meaning you are creating a specific version of that class.

5. What is the difference between a class and an object or instance?
A class is a blueprint or template for creating objects, whereas an object is a specific instance of that class. An instance is a particular object created from a class.

6. What is an attribute?
An attribute is a variable associated with an object that stores specific data about that object.

7. What are and how to use public, protected, and private attributes?
Public attributes are accessible from outside the class. Protected attributes, denoted with a leading underscore, are accessible only within the class and its subclasses. Private attributes, denoted with double underscores, are accessible only within the class.

8. What is self?
self is a convention in Python used as the first parameter of methods in a class. It represents the current instance of the class and is used to access attributes and methods of that instance within the class.

9. What is a method?
A method is a function defined within a class that operates on instances of that class.

10. What is the special init method and how to use it?
__init__ is a special method in Python that is automatically called when an instance of a class is created. It is used to initialize the attributes of the class.

11. What is Data Abstraction, Data Encapsulation, and Information Hiding?

* Data Abstraction: Process of hiding the implementation details and showing only the relevant functionality to the user.
* Data Encapsulation: Bundling the data and the methods that operate on that data into a single unit.
* Information Hiding: Process of hiding the implementation details of an object and exposing only the necessary details.

12. What is a property?
A property is a special attribute that has getter and setter methods associated with it, allowing control over access and modification of the attribute.

13. What is the difference between an attribute and a property in Python?
An attribute is a variable associated with an object, while a property is a special attribute with getter and setter methods associated with it.

14. What is the Pythonic way to write getters and setters in Python?
The Pythonic way to write getters and setters is by using the ´@property' decorator for the getter and the '@<property_name>.setter' decorator for the setter.

15. How to dynamically create arbitrary new attributes for existing instances of a class?
You can dynamically create new attributes by assigning them a value directly to the object.

16. How to bind attributes to objects and classes?
You can bind attributes to objects by assigning them a value directly to the object, or you can bind attributes to classes by defining them within the class.

17. What is the dict of a class and/or instance of a class and what does it contain?
__dict__ is a dictionary containing the attributes of a class or instance of a class, where the keys are the attribute names and the values are the values of those attributes.

18. How does Python find the attributes of an object or class?
Python searches for attributes first in the object's namespace and then in the class's namespace and its superclasses.

19. How to use the getattr function?
getattr is a function used to retrieve the value of an attribute of an object given its name. It can be used as follows: getattr(object, 'attribute_name').
