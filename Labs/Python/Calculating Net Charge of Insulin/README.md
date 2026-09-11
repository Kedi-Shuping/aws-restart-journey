# Calculating Net Charge of Insulin

This lab explored how Python can be used to calculate the estimated net charge of insulin across different pH values. I worked with dictionaries, `count()`, dictionary comprehensions, `for` loops, `while` loops, and basic mathematical expressions to calculate the positive and negative charge contributions of selected amino acids.

## What I worked with

- Insulin amino-acid sequences
- Dictionaries and key-based lookup
- `count()`
- Dictionary comprehensions
- `for` loops
- `while` loops
- `sum()`
- pH and pKa-related values
- Formatted output with `.format()`

## How it works

The script combines the B and A chains to create the mature insulin sequence. A `pKR` dictionary stores the pKa-related value for each amino acid that contributes to the charge calculation.

A dictionary comprehension uses `insulin.count()` to count the relevant amino acids and stores those counts in `seqCount`. The charge calculation then uses the amino-acid counts, their pKa-related values, and the current pH to calculate positive and negative charge contributions.

A `while` loop repeats the calculation for each whole-number pH from 0 through 14. The positive contributions from `K`, `H`, and `R` are summed separately from the negative contributions of `Y`, `C`, `D`, and `E`. The two totals are then used to calculate the net charge.

## What I learned

This exercise reinforced how dictionaries can be used to connect related values through a common key. I also reused `count()` and dictionary comprehensions from the previous insulin exercise, while applying them inside a larger calculation.

The `while` loop showed how the same calculation can be repeated while changing a variable such as pH. The result changes from positive to negative as the pH increases, with the calculated net charge at pH 7 being approximately `-2.19`.

The exercise brought together several Python concepts I had already worked with and used them to model a real calculation rather than treating each concept as an isolated exercise.

## Source Code

[net-charge-insulin.py](./net-charge-insulin.py)

## Skills Demonstrated

- Working with dictionaries and key-value lookups
- Counting values within a sequence
- Creating dictionaries with comprehensions
- Using `for` and `while` loops
- Performing calculations with variables and dictionary values
- Using `sum()` to combine calculated values
- Formatting numerical output
