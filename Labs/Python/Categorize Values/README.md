# Categorize Values

This lab explored how Python handles different data types within the same list. I created a mixed-type list and used a `for` loop to examine each item and report its data type.

## What I worked with

- Numeric values (`int` and `float`)
- Boolean values (`bool`)
- Strings (`str`)
- Lists
- `for` loops
- The `type()` function
- `print()` and string formatting with `.format()`

## How it works

The script stores six values in `myMixedTypeList`, including integers, a floating-point value, a Boolean, a sentence, and the string `"45"`.

A `for` loop visits each item in the list one at a time. The `type()` function identifies the type of the current item, and `.format()` is used to produce readable output.

One useful detail in this exercise is the difference between `45` and `"45"`. They look similar, but Python treats the first as an integer and the second as a string.

## What I learned

This exercise reinforced that a Python list can contain values of different data types. It also showed how a loop can be used to inspect each element in a collection and how `type()` can be used to understand what Python is actually storing.

The code is short, but it combines several fundamental Python concepts in one working example.

## Source Code

[categorize-values.py](./categorize-values.py)

## Skills Demonstrated

- Creating and working with lists
- Identifying Python data types
- Iterating through a collection with a `for` loop
- Producing readable program output
