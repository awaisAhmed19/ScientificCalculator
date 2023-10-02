

from Postfix_Evaluation import Post_Evaluation
from PostfixConv import PostfixConv
from Tokenization import Tokenize
PC=PostfixConv()
Pst=Post_Evaluation()


if __name__ == "__main__":
    print("Enter an expression or a string")
    input_expression = "((sin(45) + cos(30)) - tan(60))"
    print(Tokenize(input_expression))
    postfix_expression = PC.postfix(input_expression)
    print(postfix_expression)
    print(Pst.Post_Evaluation(" ".join(postfix_expression)))

   
    
     