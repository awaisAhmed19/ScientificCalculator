from Expression_handler import Expression_handler 
from Expression_handler import is_digit


exp=Expression_handler



class Tokenization:
    def __init__(self):
        self.output = []
        self.operators = []
    def tokenize_expression(self,expression):
        expression = expression.replace(" ", "")  # Remove spaces
        i=0
        while i< len(expression):
            char=expression[i]

            if is_digit(char):
                num=char
                i=+1
                while i<len(expression) and is_digit(expression[i] or expression[i]=='.'):
                    num+=expression[i]
                    i+=1
                self.output.append(char)

            elif exp.is_operator(char):
                if char == '(':
                    exp.handle_open_parenthesis()
                elif char == ')':
                    exp.handle_close_parenthesis()
                else:
                    exp.handle_operator(char)
            i+=1
        while self.operators:
            self.output.append(self.operators.pop())

        return " ".join(self.output)
