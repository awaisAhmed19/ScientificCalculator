import re

class Tokenizer:
    def __init__(self):
        self.pattern_dict = {
            r'\d+': 'NUMBER',
            r'\+': 'ADD',
            r'\-': 'SUBTRACT',
            r'\*': 'MULTIPLY',
            r'\/': 'DIVIDE',
            r'\(': 'LEFT_PAREN',
            r'\)': 'RIGHT_PAREN',
            r'sin': 'SIN',
            r'cos': 'COS',
            r'tan': 'TAN',
            r'sqrt': 'SQRT',
            r'log10': 'LOG10',
            r'ln': 'LN',
            r'\^': 'POWER',
            r'=': 'ASSIGNMENT',
            r'\.': 'DOT',
            r',': 'COMMA',
            r'!=': 'NOT_EQ',
            r'>': 'GT',
            r'<': 'LT',
            r'>=': 'GEQ',
            r'<=': 'LEQ',
            r'==': 'EQ',
            r'&&|\|\|': 'AND_OR',
            r'!': 'NEGATE',
            r'True': 'TRUE',
            r'False': 'FALSE',
            r'[xabpqy]': 'VARIABLE'
        }

    def tokenize(self, expression):
        pattern = '|'.join(f'({p})' for p in self.pattern_dict.keys())
        matches = re.findall(pattern, expression)
        tokens = [group for match in matches for group in match if group]
        tokens = [self.pattern_dict.get(token.lower(), token) for token in tokens]
        return tokens
