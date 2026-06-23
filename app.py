"""
Simple Calculator Application
This app is used to demonstrate a professional Git branching workflow.
Each feature (add, subtract, multiply, divide) is added via a separate
feature branch and merged into 'develop', then released to 'main'.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division of two numbers. Raises ValueError on divide by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("=== Simple Calculator ===")
    print(f"Add(5, 3) = {add(5, 3)}")
    print(f"Subtract(5, 3) = {subtract(5, 3)}")
    print(f"Multiply(5, 3) = {multiply(5, 3)}")
    print(f"Divide(6, 3) = {divide(6, 3)}")


if __name__ == "__main__":
    main()