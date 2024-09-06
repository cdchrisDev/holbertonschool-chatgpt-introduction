#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Args:
        n (int): The non-negative integer for which to compute the factorial.

    Returns:
        int: The factorial of the input integer n.

    Raises:
        ValueError: If n is a negative integer.

    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """
    Main function to compute the factorial of a number provided as a command-line argument.

    The script expects a single command-line argument, which should be a non-negative integer. 
    It calculates the factorial of the input number and prints the result.

    Usage:
        python script_name.py <non-negative-integer>

    Example:
        python script_name.py 5
        This will output: 120
    """
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <non-negative-integer>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("The argument must be an integer.")
        sys.exit(1)

    if number < 0:
        print("The number must be non-negative.")
        sys.exit(1)

    f = factorial(number)
    print(f)

if __name__ == "__main__":
    main()
