
import math

from Postfix_Evaluation import Post_Evaluation
from PostfixConv import PostfixConv
from Tokenization import Tokenize

PC=PostfixConv()
Pst=Post_Evaluation()


if __name__ == "__main__":
    #print("Enter an expression or a string")
    input_expression = "-1+1+1+1"
    #print(math.pow(10,2))
    print(Tokenize(input_expression))
    postfix_expression = PC.postfix(input_expression)
    print(postfix_expression)
    print(Pst.Post_Evaluation((postfix_expression)))

