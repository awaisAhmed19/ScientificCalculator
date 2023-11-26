
from Postfix_Evaluation import Post_Evaluation
from PostfixConv import PostfixConv
from Tokenization import Tokenizer

PC=PostfixConv()
Pst=Post_Evaluation()
tk=Tokenizer()

if __name__ == "__main__":
    print("Enter an expression or a string")
    input_expression = input()
    print(Pst.Post_Evaluation((input_expression)))

