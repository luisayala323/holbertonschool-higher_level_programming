General

    What is a superclass, baseclass or parentclass
    What is a subclass
    How to list all attributes and methods of a class or instance
    When can an instance have new attributes
    How to inherit class from another
    How to define a class with multiple base classes
    What is the default class every class inherit from
    How to override a method or attribute inherited from the base class
    Which attributes or methods are available by heritage to subclasses
    What is the purpose of inheritance
    What are, when and how to use isinstance, issubclass, type and super built-in functions

1. A superclass, base class, or parent class is a class that other classes inherit from. It provides common attributes and behaviors that subclasses can reuse and customize. Subclasses gain access to the superclass's members and can add their own unique functionality. This promotes code reuse and modularity in object-oriented programming.

2. A subclass is a class that inherits properties and behaviors from a superclass. It extends the functionality of the superclass by adding or modifying its attributes and methods. Subclassing allows for specialization and customization of classes based on a common template.

3. To list all attributes and methods of a class or instance in Python, use the dir() function. The dir() function returns a list of names representing the class or instance members, including inherited ones.

4. In Python, instances can have new attributes assigned to them dynamically at any time during the program's execution. This flexibility allows for customization and storing additional data specific to each instance.

5. To inherit a class from another class in Python, use the following syntax:

class SubclassName(SuperclassName): # subclass-specific attributes and methods
...

6. To define a class with multiple base classes in Python, use the following syntax:

class SubclassName(BaseClass1, BaseClass2, ...): ...

7. In Python, every class implicitly inherits from the object class by default.

8. To override a method or attribute inherited from a base class in Python, define the same method or attribute in the subclass with the desired implementation. The subclass's version will take precedence over the base class's version.

9. Subclasses in Python inherit all the public and protected attributes and methods from their superclass(es). They also inherit special methods. Private attributes and methods are not directly inherited by subclasses.

10. The purpose of inheritance in object-oriented programming is to promote code reuse, modularity, and polymorphism. It allows classes to inherit and reuse code from existing classes, organize classes into a hierarchical structure, and enable objects of different classes to be treated uniformly. It also facilitates specialization and customization of classes based on a common template.

11. Here's a short explanation:

    isinstance() is used to check if an object is an instance of a class or subclass.
    issubclass() is used to check if a class is a subclass of another class.
    type() is used to determine the type of an object or compare types.
    super() is used to call methods from a superclass within a subclass.
