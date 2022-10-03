def add(x: int, y: int) -> int: 
    return x + y

def substract(x: int, y: int) -> int: 
    return x - y

def multiply(x: int, y: int) -> int: 
    return x * y

def divide(x: int, y: int) -> int | float:
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x / y

def power(x: int, y: int) -> int: 
    return x ** y