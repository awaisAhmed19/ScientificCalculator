import re


def Tokenize(expression):
    # Define regular expressions for different token types
    regex_patterns = [
        (r'\d+(\.\d+)?', 'NUMBER'),                # Match numbers (e.g., 3, 3.14)
        (r'[+\-*/^]', 'OPERATOR'),                # Match operators (+, -, *, /, ^)
        (r'[()]', 'PARENTHESIS'),                # Match parentheses ( and )
        (r'(sin|cos|tan|sqrt|log2|log10|abs|floor|ceil|max|min|round)', 'FUNCTION'),  # Match functions
        (r'[a-zA-Z_]\w*', 'IDENTIFIER'),          # Match identifiers (e.g., variables)
    ]

    tokens = []
    while expression:
        for pattern, token_type in regex_patterns:
            match = re.match(pattern, expression)
            if match:
                matched_text = match.group(0)
                tokens.append((token_type, matched_text))
                expression = expression[len(matched_text):].strip()
                break
        else:
            raise ValueError(f"Cannot tokenize: {expression}")
    
    return [token[1] for token in tokens]

#Example usage:
#expression = "sin(45) + cos(45)"
#tokens = Tokenize(expression)
# print(tokens)
