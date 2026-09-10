# Categorize Values

This lab explored how Python handles different data types within the same list. I created a mixed-type list and used a `for` loop to inspect each item and report its data type.

## What I worked with

- Numeric values (`int` and `float`)
- Boolean values (`bool`)
- Strings (`str`)
- Lists containing different data types
- `for` loops
- The `type()` function
- String formatting with `.format()`

## How it works

The script stores six values in `myMixedTypeList`: two integers, a floating-point value, a Boolean, a sentence, and the string `"45"`.

A `for` loop visits each item in the list one at a time. For each item, the `type()` function identifies the data type, and `.format()` is used to include that information in the output.

One thing I noticed during the exercise was the difference between `45` and `"45"`. The first is an integer because it is written as a numeric value. The second is a string because it is enclosed in quotation marks. Python therefore treats them as different data types even though they look similar when displayed.

## What I learned

This exercise reinforced that a Python list does not have to contain values of only one data type. Different kinds of values can exist together in the same list, and a loop can process each element in turn.

It also showed me how `type()` can be used to inspect what Python is actually storing. That makes the difference between similar-looking values much easier to see in a running program.

The exercise is small, but it brings together lists, loops, data types, and formatted output in one working example.

## Source Code

[categorize-values.py](./categorize-values.py)

## Skills Demonstrated

- Creating and working with lists
- Storing different data types in the same list
- Identifying Python data types with `type()`
- Iterating through a collection with a `for` loop
- Formatting program output with `.format()`
