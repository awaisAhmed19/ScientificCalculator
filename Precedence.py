class Precedence:
    OPERATORS = {

    '^',  # Exponentiation
    '*',  # Multiplication and Division
    '/',
    '+',  # Addition and Subtraction
    '-',
    '!'  # Factorial
    }
    PRECEDENCE = {
    '(': 0,  # Parentheses for grouping (highest precedence)
    ')': 0,
    '^': 4,  # Exponentiation
    '*': 3,  # Multiplication and Division
    '/': 3,
    '+': 2,  # Addition and Subtraction
    '-': 2,
    'sin': 1,  # Trigonometric functions
    'cos': 1,
    'tan': 1,
    'Sqrt': 1,  # Square root function
    'log': 1,  # Logarithm
    'abs': 1,  # Absolute value
    'floor': 1,  # Floor function
    'ceil': 1,  # Ceiling function
    'max': 1,  # Maximum
    'min': 1,  # Minimum
    'round': 1,  # Round to the nearest integer
    '!': 1  # Factorial
    }


