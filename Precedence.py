class Precedence:
         OPERATORS = {'-', '+', '/', '*', '^','(',')','sin','cos','tan'}
         PRECEDENCE = {
            '(': 0,  # Parentheses for grouping
            ')': 0,
            '^': 4,  # Exponentiation (highest precedence)
            '*': 3,  # Multiplication and Division
            '/': 3,
            '+': 2,  # Addition and Subtraction
            '-': 2,
            'sin': 5,  # Example: Trigonometric functions
            'cos': 5,
            'tan': 5,
            'sqrt': 5,  # Example: Square root function
        }