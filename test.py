from ExpressionChecker import *
from calculations import calculation
from PostfixConv import *
from Tokenization import *

cal = calculation()

def Evaluate(x, y, operation):
    symbols = {
        '+': cal.add(x, y),
        '-': cal.sub(x, y),
        '*': cal.mul(x, y),
        '/': cal.div(x, y),
        '^': cal.power(x, y),
    }
    return symbols.get(operation)

class Postfix_Evaluation:
    def __init__(self):
        self.operand = []

    def postfix_Eval(self, Eval_expression):
        expression = Eval_expression
        for char in expression:
            if is_digit(char):
                self.operand.append(float(char))
            elif is_function(char):
                TrigFunction = char
                if len(self.operand) < 1:
                    # Handle the case where there are not enough operands for the function
                    raise ValueError(f"Not enough operands for {TrigFunction}")
                value = self.operand.pop()
                self.operand.append(cal.Tignometric_Eval(TrigFunction, value))
            elif char == '!':
                if len(self.operand) < 1:
                    # Handle the case where there are not enough operands for factorial
                    raise ValueError("Not enough operands for factorial")
                op1 = self.operand.pop()
                self.operand.append(cal.factorial(op1))
            elif is_operator(char):
                if len(self.operand) < 2:
                    # Handle the case where there are not enough operands for the operator
                    raise ValueError(f"Not enough operands for {char}")
                op1 = self.operand.pop()
                op2 = self.operand.pop()
                self.operand.append(Evaluate(op2, op1, char))
        
        if len(self.operand) != 1:
            # Handle the case where there are too few or too many operands
            raise ValueError("Invalid expression")
        
        return self.operand.pop()

# Test code
expression = "sin(45)+cos(45)"

Pc = PostfixConv()
Pe = Postfix_Evaluation()

expression_postfix = Pc.postfix(expression)
print(expression_postfix)

result = Pe.postfix_Eval(expression_postfix)
print(result)
