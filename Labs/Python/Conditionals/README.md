# Conditionals

This lab explored how Python can make decisions by comparing a value against different conditions. I started with a simple `if` statement and then extended the program with `elif` and `else` branches to handle multiple possible responses.

## What I worked with

- The `input()` function
- `if`, `elif`, and `else` statements
- The `==` comparison operator
- Conditional branches
- String formatting with `.format()`
- Python indentation for control flow

## How it works

The script asks the user which service they would like to use and stores the response in `userReply`.

The `if` statement checks whether the user entered `"stamps"`. If that condition is true, Python prints a response about stamp designs. If it is not true, the program moves to the next `elif` condition and checks for `"envelope"`, then `"copy"`.

The `copy` branch also asks for the number of copies and uses `.format()` to include that value in the response.

The final `else` branch handles any response that did not match the expected choices. This means the program has a defined path for both recognised and unrecognised input.

Only one branch runs for each execution. Once Python finds a condition that evaluates to true, it runs that block and skips the remaining `elif` and `else` branches.

## What I learned

This exercise showed me how conditional statements control the path a program takes based on user input. I also saw how `if`, `elif`, and `else` work together as a decision structure rather than as separate checks that all run independently.

The lab reinforced the importance of indentation in Python. The statements belonging to each condition must be indented so Python can identify which code belongs to that branch.

It also reinforced the role of comparison operators such as `==`. The program is not simply storing the user's response; it is comparing that response with specific values and using the result of those comparisons to decide what to do next.

## Source Code

- [conditionals.py](./conditionals.py)

## Skills Demonstrated

- Collecting user input with `input()`
- Comparing values with `==`
- Building decision logic with `if`, `elif`, and `else`
- Controlling program flow through conditional branches
- Using indentation to define Python code blocks
- Formatting output with `.format()`
