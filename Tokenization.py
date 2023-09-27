from Precedence import Precedence

pd = Precedence

def is_digit(char):
    return '0' <= char <= '9' or char == '.'

def is_operator(char):
    return char in pd.OPERATORS or char == '.'

class Tokenization:
    def __init__(self):
        self.output = []
        self.operators = []

    def precedence(self, operator):
        return pd.PRECEDENCE.get(operator, 0)

    def tokenize_expression(self, expression):
        expression = expression.replace(" ", "")  # Remove spaces
        i = 0  # Initializing a counter

        while i < len(expression):
            char = expression[i]

            if is_digit(char) or (char == '.' and (i == 0 or not is_digit(expression[i-1]))):
                # Handle numbers and decimals, directly output to postfix
                num = char
                i += 1
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                self.output.append(num)

            elif is_operator(char):
                # Handle operators
                while (
                    self.operators
                    and self.operators[-1] != '('
                    and self.precedence(char) <= self.precedence(self.operators[-1])
                ):
                    self.output.append(self.operators.pop())
                self.operators.append(char)
                i += 1  # Move to the next character

            elif char == '(':
                # Handle opening parentheses
                self.operators.append(char)
                i += 1  # Move to the next character

            elif char == ')':
                # Handle closing parentheses
                while self.operators and self.operators[-1] != '(':
                    self.output.append(self.operators.pop())

                if self.operators and self.operators[-1] == '(':
                    self.operators.pop()
                else:
                    raise ValueError("Mismatched parentheses")
                i += 1  # Move to the next character

        while self.operators:
            self.output.append(self.operators.pop())

        return " ".join(self.output)


