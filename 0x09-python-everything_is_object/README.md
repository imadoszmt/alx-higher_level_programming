This README file intended for understanding Python fundamentals! In this guide, we'll cover essential concepts that form the backbone of Python programming. Whether you're a beginner or looking to brush up on your Python skills, this document will provide a concise overview of key concepts.

## What is an object?

In Python, everything is an object. An object is a collection of data (variables) and methods (functions) that operate on the data. Objects are instances of classes and can represent real-world entities or abstract concepts.

## Difference between a class and an object or instance

A class is a blueprint or template for creating objects. It defines the properties and behaviors that objects of the class will have. An object, also known as an instance, is a concrete realization of a class.

## Difference between immutable object and mutable object

Immutable objects cannot be modified after creation, while mutable objects can be changed. Immutable objects include integers, floats, strings, and tuples, whereas mutable objects include lists, dictionaries, and sets.

## What is a reference?

A reference is a value that refers to an object in memory. Variables in Python hold references to objects rather than the objects themselves.

## What is an assignment?

Assignment is the process of binding a value to a variable. It associates a name (the variable) with an object in memory.

## What is an alias?

An alias refers to the situation where two or more variables refer to the same object in memory. Changes made through one variable will be reflected in the others.

## How to know if two variables are identical

Two variables are identical if they reference the same object in memory. This can be checked using the is operator.

## How to know if two variables are linked to the same object

You can check if two variables reference the same object using the is operator or by comparing their memory addresses.

## How to display the variable identifier (memory address)

The id() function can be used to retrieve the memory address of an object in the CPython implementation.

## Mutable and immutable

Mutable objects can be modified after creation, while immutable objects cannot.

## Built-in mutable types

Built-in mutable types include lists, dictionaries, and sets.

## Built-in immutable types

Built-in immutable types include integers, floats, strings, tuples, and frozensets.

## How Python passes variables to functions

Python passes variables to functions by passing references to objects. Any changes made to mutable objects within a function will affect the original objects outside the function. Immutable objects are passed by value.

