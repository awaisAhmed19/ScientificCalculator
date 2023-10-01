from calculations import Calculations
from PostfixConv import PostfixConv
from ExpressionChecker import is_digit, is_function, is_operator

class PostfixEvaluator:
    def __init__(self):
        self.calculator = Calculations()

    def evaluate(self, postfix_expression):
        stack = []

        for token in postfix_expression:
            if is_digit(token):
                stack.append(float(token))
            elif is_function(token):
                value = stack.pop()
                stack.append(self.calculator.trigonometric_eval(token, value))
            elif token == '!':
                op1 = stack.pop()
                stack.append(self.calculator.factorial(op1))
            elif is_operator(token):
                if len(stack)<2:
                    raise ValueError("Insufficient operand for operator '{}'".format(token))
                op1 = stack.pop()
                op2 = stack.pop()
                result = self.calculator.evaluate_operation(op2, op1, token)
                stack.append(result)

        if len(stack) == 1:
            return stack[0]
        else:
            raise ValueError("Invalid postfix expression")

def main():
    expression = "sin(45) + cos(45)"

    postfix_converter = PostfixConv()
    postfix_expression = postfix_converter.postfix(expression)

    evaluator = PostfixEvaluator()
    result = evaluator.evaluate(postfix_expression)

    print("Postfix Expression:", postfix_expression)
    print("Result:", result)

if __name__ == "__main__":
    main()
