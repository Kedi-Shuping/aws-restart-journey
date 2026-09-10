# Composite Data Types

This lab explored how Python combines data types into larger structures. I worked with lists, tuples, and dictionaries, then used a CSV file to build a list of vehicle records.

## What I worked with

- Lists, tuples, and dictionaries
- Composite and nested data structures
- `for` loops and `if` statements
- File handling with `with open(...)`
- The `csv` module and `csv.reader`
- `copy.deepcopy()`
- The `car_fleet.csv` data file

## How it works

The `collections_lab.py` script starts with a list of fruit and demonstrates that list elements can be changed. It then creates a tuple and accesses each item by position, followed by a dictionary that stores fruit using names as keys. Together, these examples show how different collection types organise and expose data.

The `composite-data.py` script takes the same idea further by working with structured vehicle data. A template dictionary called `myVehicle` defines the fields for a vehicle record, while `myInventoryList` starts as an empty list.

The script opens `car_fleet.csv` and uses `csv.reader` to read the file one row at a time. The first row is treated as the column header. For each vehicle record, the script makes a deep copy of the template dictionary, fills its fields with values from the CSV row, and appends the completed dictionary to `myInventoryList`.

A second set of `for` loops then goes through the completed vehicle records and prints each key and value. This creates a larger structure: a list containing dictionaries, with each dictionary containing the details for one vehicle.

## What I learned

This exercise showed me how Python's basic data types can be combined into structures that represent more useful real-world data. I also worked with data coming from a CSV file rather than defining every vehicle directly in the Python code.

Using `copy.deepcopy()` was important when creating each vehicle record from the template dictionary, because each record needs to be its own dictionary before it is added to the inventory list.

The lab also reinforced how control flow, collection types, file handling, and imported modules can work together in one program.

## Source Code

- [collections_lab.py](./collections_lab.py)
- [composite-data.py](./composite-data.py)
- [car_fleet.csv](./car_fleet.csv)

## Skills Demonstrated

- Creating and modifying lists
- Working with tuples and dictionaries
- Building nested data structures
- Reading structured data from a CSV file
- Using `for` loops and `if` statements
- Using Python modules such as `csv` and `copy`
- Creating independent records with `copy.deepcopy()`
- Iterating through dictionary key-value pairs
