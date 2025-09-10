#!/usr/bin/env python3
"""
Simple Python script demonstrating basic functionality
"""

def greet_user(name):
    return f"Hello, {name}! Welcome to Python programming."

def calculate_factorial(n):
    if n <= 1:
        return 1
    return n * calculate_factorial(n - 1)

if __name__ == "__main__":
    user_name = "World"
    print(greet_user(user_name))
    
    number = 5
    result = calculate_factorial(number)
    print(f"Factorial of {number} is: {result}")
    
    # Simple list comprehension example
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares of 1-5: {squares}")
