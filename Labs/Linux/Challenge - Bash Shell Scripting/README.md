# Lab 253 — Challenge: Bash Shell Scripting

## Overview

This lab focused on building a Bash script that dynamically creates a sequence of numbered files while adapting to the files that already exist in the working directory.

Rather than hard-coding the starting number, the script discovers the highest existing `kedi<number>` filename, calculates the next available number, and creates 25 sequential files.

## What I Built

I created an executable Bash script named `createfiles.sh` that:

1. Identifies existing filenames using the `kedi` prefix.
2. Uses a regular expression to restrict matches to filenames containing a numeric suffix.
3. Extracts the numeric portion of matching filenames.
4. Tracks the highest existing number.
5. Calculates the next starting number.
6. Uses a C-style `for` loop to create 25 sequential files.
7. Increments the number after each iteration.

The core generation loop is:

```bash
for ((i=0; i<25; i++))
do
    touch "$NAME$NUMBER"
    ((NUMBER++))
done
```

## Verification

A controlled test started at `kedi28` and produced the sequence through `kedi52`, demonstrating 25 iterations.

During the final execution, the script detected that `kedi28` already existed, calculated `START=29`, and created files through `kedi53`.

The resulting numbered files were verified with:

```bash
ls -1 kedi[0-9]* | wc -l
```

The command returned `31`.

The script was also validated with:

```bash
bash -n createfiles.sh
```

with no syntax errors, and its executable permissions were verified before finalizing the lab.

## Key Bash Concepts

- Variables and variable expansion
- Filename globbing
- Regular-expression matching with `=~`
- Parameter expansion
- Arithmetic expansion
- Conditional logic
- C-style `for` loops
- Increment operators
- Filesystem state discovery
- Script permissions
- Command-line verification

## What I Learned

The most important lesson from this lab was that Bash scripts can make decisions based on the current state of the filesystem instead of relying on fixed assumptions. The script therefore behaves as a small state-aware automation tool: it discovers where the existing sequence ends and continues from there.

This also reinforced the difference between writing a command that works once and writing automation that can safely adapt to an environment that has already changed.

## Screenshots

Selected evidence is kept intentionally limited to the strongest technical results.

1. `04-file-creation-sequence.png` — controlled 25-iteration generation from `kedi28` through `kedi52`.
2. `05-final-execution-and-verification.png` — final script execution, resulting files through `kedi53`, and the 31-file verification.
3. `06-script-executable-permissions.png` — executable permission verification for `createfiles.sh`.
