# Global Variables
In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.

```python
x = "global"

def foo():
    print("x inside:", x)

foo()
print("x outside:", x)
```

## Output
```
x inside: global
x outside: global
```

In this code, we created `x` as a global variable and defined a `foo()` function to print the global variable `x`. Finally, we call the `foo()` function and print the value of `x`.

## ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Local Variables
A variable declared inside the function's body or in the local scope is known as a local variable.

```python
def foo():
    y = "local"
    print(y)

foo()
```

## Output
```
local
```

In this code, `y` is a local variable that only exists within the `foo()` function.

## ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Accessing Local Variable Outside the Scope
The local variable can be accessed from a function within the function only and not from outside the function.

```python
def foo():
    y = "local"

foo()
print(y)
```

## Output
```
NameError: name 'y' is not defined
```

In this code, we get an error when we try to access a local variable `y` in a global scope.

## ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Global and Local Variables in the Same Code
If we create a local variable with the same name as a global variable, the local variable will only be used inside the function. The global variable remains unchanged.

```python
x = "global"

def foo():
    x = x * 2
    print(x)

foo()
print(x)
```

## Output
```
globalglobal
global
```

In this code, we used the `x` variable as a global variable as well as a local variable. The local `x` is used inside the `foo()` function, and the global `x` is used outside the function.

## ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# END

