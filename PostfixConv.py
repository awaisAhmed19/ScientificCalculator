from ExpressionChecker import *
from Precedence import *
from Tokenization import *

tk = Tokenizer()
pd = Precedence()

class PostfixConv:
    def __init__(self):
        super().__init__()
        self.output = []
        self.operator = []

    def postfix(self, expression):
        tokenList = tk.tokenize(expression)

        for i in tokenList:
            if is_digit(i):
                self.output.append(i)
            elif i == '(':
                self.operator.append(i)
            elif i == ')':
                while self.operator and self.operator[-1] != '(':
                    self.output.append(self.operator.pop())
                self.operator.pop()  # Remove the '('
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
            elif is_function(i):
                self.operator.append(i)
            elif i == '-':
                # Handle unary minus (negative sign)
                if not self.output or self.output[-1] in '([':
                    self.output.append('0')  # Add a '0' to represent the unary minus
                self.operator.append(i)

        while self.operator:
            self.output.append(self.operator.pop())

        result = list(self.output)
        return result

# Example usage
#expression = "-19 + 3"
#calculator = PostfixConv()
#postfix_result = calculator.postfix(expression)
#print("tokenization:", tk.tokenize(expression))
#print("postfix conversion:", postfix_result)
