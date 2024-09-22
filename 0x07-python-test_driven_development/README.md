# Testing Guide

This guide covers essential concepts related to interactive testing, the importance of tests, writing docstrings for tests, documenting modules and functions, basic test option flags, and finding edge cases.

## Table of Contents
1. [What's an Interactive Test?](#whats-an-interactive-test)
2. [Why Tests are Important](#why-tests-are-important)
3. [Writing Docstrings to Create Tests](#writing-docstrings-to-create-tests)
4. [Documenting Modules and Functions](#documenting-modules-and-functions)
5. [Basic Option Flags for Testing](#basic-option-flags-for-testing)
6. [Finding Edge Cases](#finding-edge-cases)

## What's an Interactive Test?

An interactive test is a type of software testing where the tester manually interacts with the application or system being tested. This approach allows for real-time exploration of the software's functionality, user interface, and overall user experience.

Key characteristics of interactive tests include:
- Manual execution by a human tester
- Real-time feedback and observation
- Flexibility to adapt the testing process on the fly
- Ability to uncover unexpected issues or usability problems

## Why Tests are Important

Tests play a crucial role in software development for several reasons:

1. **Quality Assurance**: Tests help ensure that the software meets its requirements and functions as expected.
2. **Bug Detection**: Tests can identify errors and bugs early in the development process, reducing the cost of fixes.
3. **Refactoring Confidence**: A good test suite allows developers to refactor code with confidence, knowing that existing functionality remains intact.
4. **Documentation**: Tests serve as executable documentation, demonstrating how the code should behave.
5. **Design Improvement**: Writing tests often leads to better software design, as it encourages modular and testable code.
6. **Regression Prevention**: Tests help catch regressions, ensuring that new changes don't break existing functionality.

## Writing Docstrings to Create Tests

Docstrings can be used to create tests, especially when using testing frameworks that support doctest. Here's an example of how to write a docstring that includes a test:

```python
def add_numbers(a, b):
    """
    Add two numbers and return the result.

    Args:
        a (int): The first number
        b (int): The second number

    Returns:
        int: The sum of a and b

    Example:
    >>> add_numbers(2, 3)
    5
    >>> add_numbers(-1, 1)
    0
    """
    return a + b
```

In this example, the docstring includes examples of how the function should be used and what results are expected. These examples can be automatically run as tests using the `doctest` module.

## Documenting Modules and Functions

Proper documentation is essential for maintaining and understanding code. Here are some best practices for documenting modules and functions:

### Module Documentation

Place module-level documentation at the top of the file:

```python
"""
This module provides utility functions for mathematical operations.

It includes functions for basic arithmetic, as well as more complex
calculations like factorial and fibonacci sequences.
"""

# Module code goes here
```

### Function Documentation

Use docstrings to document individual functions:

```python
def calculate_factorial(n):
    """
    Calculate the factorial of a given number.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.

    Example:
        >>> calculate_factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)
```

## Basic Option Flags for Testing

When running tests, various option flags can be used to control the testing process. Here are some common flags used with popular testing frameworks like pytest:

- `-v` or `--verbose`: Increase verbosity of the output
- `-q` or `--quiet`: Decrease verbosity of the output
- `-k EXPRESSION`: Only run tests which match the given substring expression
- `-x` or `--exitfirst`: Stop the test run on the first failure
- `--pdb`: Start the Python debugger on errors or failures
- `--cov`: Measure code coverage during test execution

Example usage:
```
pytest -v --cov=myproject tests/
```

## Finding Edge Cases

Identifying and testing edge cases is crucial for robust software. Here are some strategies to find edge cases:

1. **Boundary Values**: Test at the extremes of input ranges (e.g., minimum and maximum values).
2. **Special Values**: Consider special values like zero, empty strings, or null values.
3. **Invalid Inputs**: Test how the system handles invalid or unexpected inputs.
4. **Timing and Order**: Test scenarios involving timing issues or specific order of operations.
5. **Resource Limitations**: Test behavior under low resource conditions (e.g., low memory, disk space).
6. **Load Testing**: Test the system under high load or stress conditions.
7. **Compatibility**: Test with different environments, platforms, or data formats.
8. **Security Scenarios**: Consider potential security vulnerabilities or attack vectors.

By systematically considering these aspects, you can identify and test important edge cases in your software.

Remember, thorough testing, including edge cases, helps create more robust and reliable software.
