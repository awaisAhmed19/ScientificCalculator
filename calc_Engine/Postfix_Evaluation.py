from calculations import Calculations
from ExpressionChecker import is_digit, is_function, is_letter, is_operator
from PostfixConv import PostfixConv

cal = Calculations()
PC = PostfixConv()

top = -1

class Post_Evaluation():
    def __init__(self):
        self.output = []
    def Post_Evaluation(self, exp):
        Expression = PC.postfix(exp)
        
        for token in Expression:
            if is_digit(token) or (token[0] == '-' and is_digit(token[1:])):
                self.output.append(float(token))
            elif is_operator(token):
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
            elif token == '!':
                op = self.output.pop()
                self.output.append(self.Fact(op))
            elif is_function(token):
                value = int(self.output.pop())
                trigFunc = token
                self.output.append(cal.function_eval(trigFunc, value))
        
        result = self.output.pop()
        return result

    def evaluate(self, a, b, token):
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
        if y == 0:
            raise Exception("Cannot divide by zero")
        else:
            return x / y

    def power(self, x, y):
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
        return x*(-1)

    def Fact(self, op):
        if op == 0:
            return 1
        else:
            return op * self.Fact(op - 1)
        
pe=Post_Evaluation()
print(pe.Post_Evaluation("inv(7)"))