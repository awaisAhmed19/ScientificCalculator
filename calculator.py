

from Postfix_Evaluation import Postfix_Evaluation
from PostfixConv import PostfixConv
PC=PostfixConv()
Pst=Postfix_Evaluation()

if __name__ == "__main__":
    print("Enter an expression or a string")
    input_expression = input()

    postfix_expression = PC.postfix(input_expression)

    Pst.postfix_Eval(" ".join(postfix_expression))

    print(Pst.postfix_Eval(postfix_expression))
    print(" ".join(postfix_expression))
     