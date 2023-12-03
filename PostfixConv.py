from ExpressionChecker import *
from Precedence import *
from Tokenization import *

# Initialize instances of Tokenizer, Precedence, and PostfixConv
tk = Tokenizer()
pd = Precedence()

class PostfixConv:
    def __init__(self):
        super().__init__()
        # Initialize lists to store the output and operators during postfix conversion
        self.output = []
        self.operator = []

    def postfix(self, expression):
        # Tokenize the input expression using the Tokenizer instance
        tokenList = tk.tokenize(expression)

        # Process each token in the tokenized expression
        for i in tokenList:
            # If the token is a digit, append it to the output
            if is_digit(i):
                self.output.append(i)
            # If the token is '(', push it onto the operator stack
            elif i == '(':
                self.operator.append(i)
            # If the token is ')', pop operators from the stack until '(' is encountered
            elif i == ')':
                while self.operator and self.operator[-1] != '(':
                    self.output.append(self.operator.pop())
                self.operator.pop()  # Remove the '('
            # If the token is an operator, handle operator precedence and associativity
            elif is_operator(i):
                while (
                    self.operator
                    and self.operator[-1] != '('
                    and (
                        pd.PRECEDENCE[i] < pd.PRECEDENCE.get(self.operator[-1], 0)
                        or (
                            pd.PRECEDENCE[i] == pd.PRECEDENCE.get(self.operator[-1], 0)
                            and pd.LEFT_ASSOCIATIVE.get(i, True)
                        )
                    )
                ):
                    self.output.append(self.operator.pop())
                self.operator.append(i)
            # If the token is a recognized function, push it onto the operator stack
            elif is_function(i):
                self.operator.append(i)
            # If the token is '-', handle unary minus (negative sign)
            elif i == '-':
                # Handle unary minus (negative sign)
                if not self.output or self.output[-1] in '([':
                    self.output.append('0')  # Add a '0' to represent the unary minus
                self.operator.append(i)

        # Pop any remaining operators from the stack and append them to the output
        while self.operator:
            self.output.append(self.operator.pop())

        # The final result is a list representing the postfix expression
        result = list(self.output)
        return result

# Example usage
#expression = "-19 + 3"
#calculator = PostfixConv()
#postfix_result = calculator.postfix(expression)
#print("tokenization:", tk.tokenize(expression))
#print("postfix conversion:", postfix_result)
