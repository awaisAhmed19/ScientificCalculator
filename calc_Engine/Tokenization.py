import re


class Tokenizer:
    def __init__(self):

        self.pattern_dict = {
            r"\d+\.\d+": "DNUMBER",
            r"\d+": "NUMBER",
            r"\+": "ADD",
            r"\-": "SUBTRACT",
            r"\*": "MULTIPLY",
            r"\÷|\/": "DIVIDE",
            r"\(": "LEFT_PAREN",
            r"\)": "RIGHT_PAREN",
            r"sin": "SIN",
            r"%": "MOD",
            r"cos": "COS",
            r"tan": "TAN",
            r"√": "SQRT",
            r"log2": "LOG2",
            r"log10": "LOG10",
            r"log": "LOG10",
            r"inv": "INV",
            r"ln": "LN",
            r"\^": "POWER",
            r"=": "ASSIGNMENT",
            # r"\.": "DOT",  # Use \. to match literal dot
            r",": "COMMA",
            r"!=": "NOT_EQ",
            r">": "GT",
            r"<": "LT",
            r">=": "GEQ",
            r"<=": "LEQ",
            r"==": "EQ",
            r"&&|\|\|": "AND_OR",
            r"!": "NEGATE",
            r"True": "TRUE",
            r"False": "FALSE",
            r"[xabpqy]": "VARIABLE",
        }

    def tokenize(self, expression):
        pattern = "|".join(f"({p})" for p in self.pattern_dict.keys())
        matches = re.findall(pattern, expression)
        tokens = [group for match in matches for group in match if group]
        print(tokens)
        return tokens
