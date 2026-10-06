# PLP Python Week 6

## Files

- `safe_tools.py` - Contains safe functions that use try/except to handle errors.
- `unbreakable.py` - Demonstrates how to keep a program running when a user enters invalid input.
- `README.md` - Describes the assignment files and explains why an if check cannot catch `abc`.

## Why can the if check not catch abc on its own?

An if check can test conditions, but `int("abc")` raises a ValueError when Python tries to convert the text. The try/except block catches that error and lets the program continue instead of crashing.
