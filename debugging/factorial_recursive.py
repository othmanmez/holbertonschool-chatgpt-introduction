#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) < 2:
    print("Error: Please provide a number.")
else:
    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            f = factorial(n)
            print(f)
    except ValueError:
        print("Error: Please provide a valid integer.")

