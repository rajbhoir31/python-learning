# Day 3: Function Practice

def greet(name="Analyst"):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
