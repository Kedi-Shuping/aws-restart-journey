# Loops

This lab explored how Python can repeat a section of code until a condition changes. I used a `while` loop to build a simple number-guessing game and combined the loop with user input, comparison logic, and a Boolean flag to control when the program stops.

## What I worked with

- `while` loops
- The `random` module
- `random.randint()`
- User input with `input()`
- The `int()` function
- `if` and `else` statements
- Boolean values
- String formatting with `.format()`

## How it works

The script starts by importing the `random` module and generating a random number between 1 and 10 with `random.randint(1, 10)`. That number becomes the value the user needs to guess.

The variable `isGuessRight` starts as `False`. The `while` loop checks this value and continues running while the condition `isGuessRight != True` remains true.

Each time through the loop, the program asks the user for a guess and converts the input from a string to an integer using `int()`. An `if` statement then compares the guess with the randomly generated number.

When the guess is correct, the program prints a winning message and changes `isGuessRight` to `True`. That changes the condition being tested by the `while` loop, so the loop stops. When the guess is incorrect, the program prints a message and the loop runs again, giving the user another attempt.

The important part of the exercise is that the loop does not simply repeat forever. Its continuation depends on a condition, and the program changes that condition when the correct guess is made.

## What I learned

This exercise helped me understand the relationship between a loop and the condition that controls it. The `while` loop repeatedly checks its condition, so something inside the loop must eventually change that condition or the loop will continue indefinitely.

I also saw how a Boolean variable can be used as a simple control flag. In this program, `isGuessRight` represents the state of the game: `False` means keep trying, while `True` means the correct guess has been made and the loop can stop.

The exercise also reinforced that `input()` returns text, which is why the guess is converted with `int()` before it is compared with the randomly generated number.

## Source Code

- [while-loop.py](./while-loop.py)

## Skills Demonstrated

- Repeating program logic with a `while` loop
- Controlling loop execution with a Boolean condition
- Generating random values with Python's `random` module
- Accepting and converting user input
- Combining loops with conditional logic
- Formatting program output with `.format()`
