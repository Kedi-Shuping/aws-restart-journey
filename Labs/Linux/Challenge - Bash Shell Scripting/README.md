# Bash Shell Scripting: Dynamic File Creation

## Overview

This project focused on using Bash to create a sequence of numbered files while adapting to files that already existed in the directory.

Instead of choosing a starting number manually, I built the script so it could inspect the existing `kedi<number>` files, find the highest number, and continue the sequence from there.

## What I Built

I created an executable Bash script called `createfiles.sh`.

The script:

1. Looks through the existing `kedi` files.
2. Checks that each relevant filename ends in a number.
3. Tracks the highest number found.
4. Starts at the next number.
5. Creates 25 files in sequence using `touch`.

The number is incremented after each file is created, allowing the script to build on the state already present in the directory.

## Technical Context

The key design choice was to make the script state-aware rather than hard-code a starting value. This means the script can be run in a directory that already contains part of the sequence and determine where the next sequence should begin.

That introduces a useful scripting pattern: **inspect the current state first, then make a change based on what was discovered**.

## Verification

Before the final run, I tested the loop with `START=28`. It created the sequence from `kedi28` through `kedi52`, producing 25 files.

For the final run, the script detected the existing sequence and continued from the next available number, creating files through `kedi53`.

I verified the resulting files with:

```bash
ls -1 kedi[0-9]* | wc -l
```

The command returned `31`.

I also checked the script syntax with:

```bash
bash -n createfiles.sh
```

No syntax errors were reported. The script's executable permissions were also verified before finishing the project.

## Screenshots

### File Creation Sequence

The controlled test created 25 files from `kedi28` through `kedi52`.

![File creation sequence](screenshots/04-file-creation-sequence.png)

### Final Execution and Verification

The final run continued the sequence through `kedi53`, and the resulting directory contained 31 numbered files.

![Final execution and verification](screenshots/05-final-execution-and-verification.png)

### Script Permissions

The script's executable permissions were verified before completion.

![Script executable permissions](screenshots/06-script-executable-permissions.png)

## Skills Demonstrated

- Wrote and executed Bash scripts
- Used loops and conditional logic
- Parsed existing filenames to determine the current sequence state
- Used `touch` to create files programmatically
- Managed executable file permissions
- Tested Bash syntax with `bash -n`
- Verified script behaviour from the command line
- Designed a script that adapts to existing filesystem state

## Key Lessons Learned

The most useful part of this project was making the script respond to what was already in the directory. The starting number was not simply hard-coded; the script had to discover the current state and calculate where the next sequence should begin.

That reinforced the difference between writing a command that works once and writing automation that can adapt when the environment has already changed.
