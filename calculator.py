
import math

from Postfix_Evaluation import Post_Evaluation
from PostfixConv import PostfixConv
from Tokenization import Tokenizer

PC=PostfixConv()
Pst=Post_Evaluation()
tk=Tokenizer()

if __name__ == "__main__":
    #print("Enter an expression or a string")
    input_expression = "-1-10-3"

    #print(math.pow(10,2))
    print(list(tk.tokenize(input_expression)))
    postfix_expression = PC.postfix(input_expression)
    print(postfix_expression)
    print(Pst.Post_Evaluation((postfix_expression)))

