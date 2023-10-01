

from Postfix_Evaluation import PostfixEvaluator
from PostfixConv import PostfixConv
PC=PostfixConv()
Pst=PostfixEvaluator()

if __name__ == "__main__":
    print("Enter an expression or a string")
    input_expression = input()

    postfix_expression = PC.postfix(input_expression)
    print(" ".join(postfix_expression))

    print(Pst.evaluate(" ".join(postfix_expression)))

   
    
     