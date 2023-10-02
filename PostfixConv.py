from Precedence import *
from ExpressionChecker import *
from Tokenization import *
pd=Precedence

class PostfixConv():
    def __init__(self):
        super().__init__()
        self.output = []
        self.operator = []

    def postfix(self, expression):
        tokenList = Tokenize(expression)

        for i in tokenList:
            if is_digit(i) :
                self.output.append(i)
            elif i == '(':
                self.operator.append(i)
            elif i == ')':
                while self.operator and self.operator[-1] != '(':
                    self.output.append(self.operator.pop())

                if self.operator and self.operator[-1] == '(':
                    self.operator.pop()
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

        while self.operator:
            self.output.append(self.operator.pop())

        result = list(self.output)
        return result

# Test snippet
#expression = "3+4+45*4"
#post = PostfixConv()
#print(post.postfix(expression))
