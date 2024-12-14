# Python Object-Oriented Programming (OOP) Deep Dive

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to organize and structure code. It focuses on creating reusable, modular code by representing real-world entities as software objects that have:
- Attributes (data)
- Methods (behaviors)
- The ability to interact with one another

## First-Class Everything

In Python, "first-class everything" means that almost everything in Python can be treated as an object:
- Functions are first-class objects
- Classes are first-class objects
- Integers, strings, lists, etc., are all objects
- You can pass them as arguments, return them from functions, store them in variables, and manipulate them dynamically

## Classes and Objects

### What is a Class?
A class is a blueprint or template for creating objects. It defines a set of attributes and methods that the objects of that class will have. Think of it like a cookie cutter that defines the shape and characteristics of cookies.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says Woof!")
```

### What is an Object/Instance?
An object (or instance) is a specific implementation of a class. It's a concrete entity created from the class blueprint that has its own unique set of attributes.

```python
# Creating objects/instances
my_dog = Dog("Buddy", "Golden Retriever")
another_dog = Dog("Max", "Labrador")
```

### Difference Between Class and Object
- A class is a blueprint/template
- An object is a specific instance created from that blueprint
- You can create multiple objects from a single class, each with its own unique data

## Attributes

### What is an Attribute?
An attribute is a piece of data associated with an object or a class. It represents the state or characteristics of the object.

### Types of Attributes

#### Public Attributes
- Accessible from anywhere
- No naming restrictions
```python
class Person:
    def __init__(self, name):
        self.name = name  # Public attribute
```

#### Protected Attributes
- Conventionally prefixed with a single underscore
- Indicates the attribute should not be accessed directly outside the class
```python
class Person:
    def __init__(self, name):
        self._name = name  # Protected attribute
```

#### Private Attributes
- Prefixed with double underscores
- Name mangling occurs to make it harder to access from outside the class
```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute
```

## Special Methods and Concepts

### The `self` Keyword
`self` refers to the instance of the class. It's used to access the object's attributes and methods from within the class definition.

### Methods
A method is a function defined inside a class that can perform actions on the object's data.

```python
class Calculator:
    def add(self, a, b):  # Method
        return a + b
```

### The `__init__` Method
A special method called when an object is created. It initializes the object's attributes.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## Data Abstraction, Encapsulation, and Information Hiding

### Data Abstraction
- Hiding complex implementation details
- Showing only the necessary features of an object

### Data Encapsulation
- Bundling data and methods that work on that data within a single unit (class)
- Controlling access to some of an object's components

### Information Hiding
- Restricting direct access to some of an object's components
- Achieved through private and protected attributes

## Properties

### What is a Property?
A property allows you to define methods that act like attributes, providing more control over getting, setting, or deleting an attribute.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")
```

### Difference Between Attribute and Property
- An attribute is a direct data storage
- A property is a method that looks like an attribute but can have additional logic for getting, setting, or deleting

### Pythonic Getters and Setters
- Use `@property` decorator
- Create methods that look and feel like direct attribute access
- Allows for validation, computation, or other logic

## Special String Representation Methods

### `__str__` Method
- Used for creating a human-readable string representation
- Called by `str()` and `print()`

### `__repr__` Method
- Used for creating an unambiguous string representation
- Typically used for debugging and development
- Called by `repr()`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point at ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
```

## Class and Object Attributes

### Class Attribute
- Shared by all instances of a class
- Defined directly in the class body

```python
class Dog:
    species = "Canis familiaris"  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Object attribute
```

### Difference Between Object and Class Attributes
- Object attributes are unique to each instance
- Class attributes are shared across all instances

## Class and Static Methods

### Class Method
- Uses `@classmethod` decorator
- First argument is the class itself (typically named `cls`)
- Can modify class-level state

```python
class MyClass:
    count = 0
    
    @classmethod
    def increment_count(cls):
        cls.count += 1
```

### Static Method
- Uses `@staticmethod` decorator
- Doesn't receive automatic first argument
- Used for utility functions related to the class

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
```

## Dynamic Attribute Manipulation

### Creating New Attributes Dynamically
```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
person.age = 30  # Dynamically adding a new attribute
```

### Binding Attributes
```python
# To an instance
person.job = "Engineer"

# To a class
Person.nationality = "Unknown"
```

## `__dict__` Exploration

### Class `__dict__`
- Contains all class-level attributes and methods
- Includes class methods, static methods, etc.

### Instance `__dict__`
- Contains all instance-specific attributes
- Does not include methods defined in the class

## Attribute Lookup

Python looks for attributes in this order:
1. Instance attributes
2. Class attributes
3. Inherited class attributes

## The `getattr()` Function

```python
# Syntax: getattr(object, attribute_name, default_value)
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Bob")
age = getattr(person, 'age', 'Unknown')  # Returns 'Unknown' if 'age' doesn't exist
```

## Conclusion

Object-Oriented Programming in Python provides a powerful way to structure and organize code, making it more modular, reusable, and intuitive. By understanding these concepts, you can write more elegant and maintainable Python code.
