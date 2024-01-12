from calculations import Calculations
from ExpressionChecker import is_digit, is_function, is_letter, is_operator
from PostfixConv import PostfixConv

# Initialize an instance of the Calculations class
cal = Calculations()

# Initialize an instance of the PostfixConv class
PC = PostfixConv()

# Global variable to keep track of the top of the stack
top = -1

class Post_Evaluation():
    def __init__(self):
        # Initialize an empty list to store the output of the postfix evaluation
        self.output = []
    def Post_Evaluation(self, exp):
        # Convert the infix expression to postfix
        Expression = PC.postfix(exp)
        
        # Iterate through each token in the postfix expression
        for token in Expression:
            # Check if the token is a digit or a negative number
            if is_digit(token) or (token[0] == '-' and is_digit(token[1:])):
                self.output.append(float(token))
            # Check if the token is an operator
            elif is_operator(token):
                # Handle the unary negation operator '-'
                if token == '-' and len(self.output) >= 2:
                    op1 = self.output.pop()
                    op2 = self.output.pop()
                    self.output.append(self.evaluate(op2, op1, token))
                elif token == '-' and len(self.output) == 1:
                    op = self.output.pop()
                    self.output.append(self.negation(op))
                else:
                    op1 = self.output.pop()
                    op2 = self.output.pop()
                    self.output.append(self.evaluate(op2, op1, token))
            # Check if the token is the factorial operator '!'
            elif token == '!':
                op = self.output.pop()
                self.output.append(self.Fact(op))
            # Check if the token is a recognized function
            elif is_function(token):
                value = int(self.output.pop())
                trigFunc = token
                self.output.append(cal.function_eval(trigFunc, value))
        
        # The final result is the last item in the output list
        result = self.output.pop()
        return result

    def evaluate(self, a, b, token):
        # Evaluate the expression based on the operator token
        if token == '+':
            return self.add(a, b)
        elif token == '-':
            return self.sub(a, b)
        elif token == '*':
            return self.mul(a, b)
        elif token == '/':
            return self.div(a, b)
        elif token == '^':
            return self.power(a, b)

    def add(self, x, y): 
        return x + y

    def sub(self, x, y): 
        return x - y

    def mul(self, x, y): 
        return x * y

    def div(self, x, y):
        # Check for division by zero
        if y == 0:
            raise Exception("Cannot divide by zero")
        else:
            return x / y

    def power(self, x, y):
        # Recursive function to calculate x^y
        if y == 0:
            return 1
        else:
            if y % 2 == 0:
                temp = self.power(x, y // 2)
                return temp * temp
            else:
                temp = self.power(x, (y - 1) // 2)
                return temp * temp * x

    def negation(self, x):
        # Negate the value x
        return -x

    def Fact(self, op):
        # Recursive function to calculate the factorial of op
        if op == 0:
            return 1
        else:
            return op * self.Fact(op - 1)

 