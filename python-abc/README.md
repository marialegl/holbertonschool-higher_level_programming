1. Abstract Classes

Abstract Classes are used to define a common interface for a group of related classes while ensuring that certain methods must be implemented in those classes.

* Purpose: To create a blueprint for other classes.
* How it works: An abstract class can have abstract methods (methods without implementation) that must be overridden in derived classes.
* Example: If you have an abstract class Animal with an abstract method make_sound(), any subclass like Dog or Cat must provide an implementation for make_sound().


2. Interfaces and Duck Typing

Interfaces define a set of methods that a class must implement without providing the actual implementation. Duck Typing in Python is a way to ensure that an object adheres to a specific protocol or interface based on its behavior rather than its inheritance.

* Purpose: To enforce a contract that certain methods will be available.
* How it works: In languages with strict interfaces, you explicitly declare that a class implements an interface. In Python, you use duck typing, where you check if an object has the necessary methods and properties.
* Example: If it looks like a duck and quacks like a duck, it’s treated as a duck. In Python, you don’t check the type of the object but whether it has the needed methods.


3. Subclassing Standard Base Classes

Subclassing Standard Base Classes means extending built-in Python classes like list, dict, and iterator to create custom classes with specialized behavior.

* Purpose: To enhance or modify the functionality of standard data structures.
* How it works: By creating a new class that inherits from a base class like list or dict, you can add new methods or override existing ones.
* Example: You can create a CustomList class that inherits from list and add a method to get the median of the list.


4. Method Overriding

Method Overriding allows a subclass to provide a specific implementation for a method that is already defined in its superclass.

* Purpose: To alter or enhance the behavior of inherited methods.
* How it works: You define a method in the subclass with the same name as the one in the superclass.
* Example: If a Bird class has a method fly(), a Penguin subclass might override fly() to do nothing because penguins don't fly.


5. Multiple Inheritance

Multiple Inheritance is when a class inherits from more than one base class, combining their behaviors and properties.

* Purpose: To form complex relationships and reuse code across different class hierarchies.
* How it works: You specify multiple base classes in the class definition.
* Example: A FlyingFish class might inherit from both Fish and Bird classes to combine swimming and flying behaviors.


6. Mixins

Mixins are a way to compose behavior across unrelated classes by defining small, reusable classes that provide specific functionality.

* Purpose: To add common behavior to multiple classes without using inheritance.
* How it works: You create a mixin class with methods that can be used by other classes through multiple inheritance.
* Example: A LoggingMixin might provide logging functionality that can be added to any class, like User or Order, without those classes needing to inherit from a common parent class.