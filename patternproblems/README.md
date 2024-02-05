# Patterns

This Python script allows you to print various patterns to the console. The patterns are generated based on a size input provided by the user. The patterns include a right-angled triangle, a pyramid, and a number pyramid.

## Classes

### Patterns

This class is responsible for generating and printing the patterns. It has the following methods:

- `triangle()`: Prints a right-angled triangle pattern of '*' with height of n.
- `pyramid()`: Prints a pyramid pattern of '*' with height of n.
- `numberPyramid()`: Prints a pyramid pattern of numbers with height of n.

### main()

This is the main function that runs the program. It prompts the user to enter the size of the pattern and the type of pattern they want to print. The function keeps running until the user chooses to exit.

## How to Run

To run the script, you can use the following command in your terminal:

```bash
python patterns.py
```

You will then be prompted to enter the size of the pattern and the type of pattern you want to print. You can choose from the following options:

Triangle Pattern
Pyramid Pattern
Number Pyramid Pattern
Exit
After choosing an option, the selected pattern will be printed to the console. You can continue choosing options until you choose to exit.

Requirements
Python 3.x
threading module
os module
Note
This script uses threading to print the patterns. Each pattern is printed in a separate thread. After a pattern is printed, the console is cleared before the next pattern is printed.

