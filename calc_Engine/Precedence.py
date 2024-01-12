import math

class Precedence:
    OPERATORS = {
        '^',  # Exponentiation
        '*',  # Multiplication and Division
        '/',
        '+',  # Addition and Subtraction
        '-'
    }

    PRECEDENCE = {
        '(': 0,  # Parentheses for grouping (highest precedence)
        ')': 0,
        '^': 4,    # Exponentiation
        '*': 3,    # Multiplication and Division
        '/': 3,
        '+': 2,    # Addition and Subtraction
        '-': 2,
        'sin': 4,  # Trigonometric functions (Corrected precedence level)
        'cos': 4,  # Trigonometric functions (Corrected precedence level)
        'tan': 4,  # Trigonometric functions (Corrected precedence level)
        'Sqrt': 4, # Square root function (Corrected precedence level)
        'log': 4,  # Logarithm (Corrected precedence level)
        'abs': 4,  # Absolute value (Corrected precedence level)
        'floor': 4, # Floor function (Corrected precedence level)
        'ceil': 4,  # Ceiling function (Corrected precedence level)
        'max': 4,   # Maximum (Corrected precedence level)
        'min': 4,   # Minimum (Corrected precedence level)
        'round': 4, # Round to the nearest integer (Corrected precedence level)
        '!': 5     # Factorial
    }

    LEFT_ASSOCIATIVE = {
        '^': False,  # Exponentiation is right-associative
        '*': True,   # Multiplication is left-associative
        '/': True,   # Division is left-associative
        '+': True,   # Addition is left-associative
        '-': True,   # Subtraction is left-associative
        '!': False   # Factorial is right-associative
    }

    