# Python Fundamentals

This lab introduced the basic building blocks of Python through small programs covering output, numeric data, and strings. I worked from simple `print()` statements to inspecting data types, combining strings, and collecting information from a user.

## What I worked with

- `print()` for program output
- The `type()` function
- Integer, complex, Boolean, and string values
- Variables and reassignment
- String concatenation
- User input with `input()`
- String formatting with `.format()`
- Converting values with `str()`

## How it works

The `hello-world.py` script starts with the traditional first Python program: a `print()` statement that displays `Hello, World`. It provides a simple way to verify that the Python environment can run a program successfully.

The `numeric-data.py` script then explores how Python represents different kinds of values. The variable `myValue` is assigned several different values in turn, and `type()` is used to inspect what Python is storing. The script includes an integer, a complex number, and Boolean values of `True` and `False`. It also uses `str()` to combine the values and their type information into readable output.

The `string-data.py` script focuses on text. It creates a string, checks its data type, and joins two strings together to produce `waterfall`. It then uses `input()` to collect a name, favourite colour, and favourite animal from the user before combining those values into a formatted sentence with `.format()`.

Together, the three scripts build from basic output to working with different data types and accepting information at runtime.

## What I learned

This exercise gave me a foundation for understanding that Python variables can be reassigned to different values and that the `type()` function can be used to inspect the type of the current value.

I also reinforced the difference between values and their representations. For example, `str()` converts a value into a string so it can be combined with other text for output.

The string exercise connected several of these ideas together: the program accepts user input, stores the responses in variables, combines strings, and formats the final result. That made the progression from static output to interactive programs much clearer.

## Source Code

- [hello-world.py](./hello-world.py)
- [numeric-data.py](./numeric-data.py)
- [string-data.py](./string-data.py)

## Skills Demonstrated

- Writing and running basic Python programs
- Creating and reassigning variables
- Inspecting data types with `type()`
- Working with numeric, Boolean, and string values
- Concatenating strings
- Collecting user input with `input()`
- Formatting output with `.format()`
- Converting values with `str()`
