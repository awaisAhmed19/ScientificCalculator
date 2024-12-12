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
        tokenList = None
        tokenList = tk.tokenize(expression)
        # print("token", tokenList)

        for i in tokenList:
            if is_digit(i) or is_floating_point(i):
                self.output.append(i)
                # print("isdigit:", self.output)
            elif i == "(":
                self.operator.append(i)
            elif i == ")":
                while self.operator and self.operator[-1] != "(":
                    self.output.append(self.operator.pop())
                self.operator.pop()
            elif is_operator(i):
                while (
                    self.operator
                    and self.operator[-1] != "("
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
                print("after operator:", self.operator)
            elif i == "-":
                if not self.output or self.output[-1] in "([":
                    self.output.append("0")
                self.operator.append(i)

        while self.operator:
            self.output.append(self.operator.pop())

        result = list(self.output)
        # print("result:", result)
        return result
