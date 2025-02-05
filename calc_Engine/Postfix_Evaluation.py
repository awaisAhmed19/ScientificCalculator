from calculations import Calculations
from ExpressionChecker import (
    is_digit,
    is_function,
    is_letter,
    is_operator,
    is_floating_point,
)
from PostfixConv import PostfixConv
import math

cal = Calculations()
PC = PostfixConv()

top = -1


class Post_Evaluation:
    def __init__(self):
        self.output = []
        self.expression = ""

    def Post_Evaluation(self, exp):

        self.expression = PC.postfix(exp)
        # print("exp", self.expression)
        for token in self.expression:
            if (
                is_digit(token)
                or is_floating_point(token)
                or (token[0] == "-" and is_digit(token[1:]))
            ):
                self.output.append(float(token))
                # print(self.output)
            elif is_operator(token):
                if token == "-" and len(self.output) >= 2:
                    op1 = self.output.pop()
                    op2 = self.output.pop()
                    self.output.append(self.evaluate(op2, op1, token))
                elif token == "-" and len(self.output) == 1:
                    op = self.output.pop()
                    self.output.append(self.negation(op))
                elif token == "!":
                    op = self.output.pop()
                    # print("fact is being called")
                    self.output.append(self.Fact(op))
                else:
                    op1 = self.output.pop()
                    op2 = self.output.pop()
                    self.output.append(self.evaluate(op2, op1, token))

            elif is_function(token):
                value = int(self.output.pop())
                trigFunc = token
                self.output.append(cal.function_eval(trigFunc, value))

        result = self.output.pop()
        return result

    def evaluate(self, a, b, token):
        if token == "+":
            return self.add(a, b)
        elif token == "-":
            return self.sub(a, b)
        elif token == "*":
            return self.mul(a, b)
        elif token == "÷" or token == "/":
            return self.div(a, b)
        elif token == "^":
            return self.power(a, b)
        elif token == "%":
            return self.mod(a, b)

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def mod(self, x, y):
        result = math.floor(self.div(x, y))
        # print("aftre abs", result)
        newy = self.mul(result, y)
        fresult = self.sub(x, newy)
        # print(x % y)
        return fresult

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
        return x * (-1)

    def Fact(self, op):
        if op < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        if op.is_integer():
            op = int(op)
            if op == 0 or op == 1:
                return 1

            fact = 1
            for i in range(2, op + 1):
                fact *= i
            return fact
        else:  # For non-integers, use the Gamma function
            return math.gamma(op + 1)


# p = Post_Evaluation()
# print(p.Post_Evaluation("√(7)"))
