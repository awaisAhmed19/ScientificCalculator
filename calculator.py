from Postfix_Evaluation import Postfix_Evaluation
from Tokenization import Tokenization
Tk=Tokenization()
Pst=Postfix_Evaluation()

if __name__ == "__main__":
    print("Enter an expression or a string")
    input_expression = input()
    postfix_expression = Tk.tokenize_expression(input_expression)
    Pst.postfix_Eval(postfix_expression)
    print(Pst.postfix_Eval(postfix_expression))
    print(postfix_expression)
