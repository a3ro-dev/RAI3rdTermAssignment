# Return Statements in Python

The Python `return` statement is a special statement that you can use inside a function or method to send the function's result back to the caller. A `return` statement consists of the `return` keyword, followed by an optional return value. The return value of a Python function can be any Python object.

## ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Explicit Return Statements

An explicit `return` statement immediately terminates a function's execution and sends the return value back to the caller code. To add an explicit `return` statement to a Python function, you need to use `return` followed by an optional return value.

Here's an example of an explicit return statement in a simple calculator function:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```
### Output
```
8
```

In this example, the `add` function explicitly returns the sum of `A` and `B`, which is then printed to the console.

## ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Implicit Return Statements

In Python, every function will always have a return value. Unlike other programming languages, there is no concept of a procedure or routine environment. If you don't explicitly use a `return` statement or specify a `return` value, Python will implicitly return a default value, which is always `None`.

Here's an example of an implicit return statement:
```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Akshat")
print(result)
```

### Output
```
Hello, Akshat!
None
```

In this example, the `greet` function does not have a `return` statement, so it returns `None` by default. This is demonstrated by the `print(result)` statement, which prints `None`.

## ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# END