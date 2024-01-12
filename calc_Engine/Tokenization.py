import re


class Tokenizer:
    def __init__(self):
        # Define a dictionary with regular expressions and corresponding token names
        self.pattern_dict = {
            r'\d+': 'NUMBER',          # Match one or more digits
            r'\+': 'ADD',              # Match the plus sign
            r'\-': 'SUBTRACT',         # Match the minus sign
            r'\*': 'MULTIPLY',         # Match the asterisk (multiplication)
            r'\/': 'DIVIDE',           # Match the forward slash (division)
            r'\(': 'LEFT_PAREN',       # Match the left parenthesis
            r'\)': 'RIGHT_PAREN',      # Match the right parenthesis
            r'sin': 'SIN',             # Match the sin function
            r'cos': 'COS',             # Match the cos function
            r'tan': 'TAN',             # Match the tan function
            r'sqrt': 'SQRT',           # Match the sqrt function
            r'log2': 'LOG2',           # Match the log2 function
            r'log10': 'LOG10',         # Match the log10 function
            r'log': 'LOG10',           # Match the log function (treated as log10)
            r'ln': 'LN',               # Match the natural logarithm (ln) function
            r'\^': 'POWER',            # Match the caret symbol (power/exponentiation)
            r'=': 'ASSIGNMENT',        # Match the equals sign (assignment)
            r'\.': 'DOT',              # Match the period (dot)
            r',': 'COMMA',             # Match the comma
            r'!=': 'NOT_EQ',           # Match the not equals operator
            r'>': 'GT',                # Match the greater than operator
            r'<': 'LT',                # Match the less than operator
            r'>=': 'GEQ',              # Match the greater than or equal to operator
            r'<=': 'LEQ',              # Match the less than or equal to operator
            r'==': 'EQ',               # Match the equals equals operator
            r'&&|\|\|': 'AND_OR',      # Match logical AND or logical OR
            r'!': 'NEGATE',            # Match the exclamation mark (negation)
            r'True': 'TRUE',           # Match the boolean value True
            r'False': 'FALSE',         # Match the boolean value False
            r'[xabpqy]': 'VARIABLE'    # Match single letters as variables (x, a, b, p, q, y)
        }

    def tokenize(self, expression):
        # Create a pattern by joining the regular expressions with the '|' (or) operator
        pattern = '|'.join(f'({p})' for p in self.pattern_dict.keys())
        
        # Use re.findall to find all matches in the input expression based on the pattern
        matches = re.findall(pattern, expression)
        
        # Flatten the matches list to get individual tokens
        tokens = [group for match in matches for group in match if group]
        
        # Return the list of tokens
        return tokens
