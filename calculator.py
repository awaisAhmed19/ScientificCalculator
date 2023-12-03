
from Postfix_Evaluation import Post_Evaluation

Pst=Post_Evaluation()


if __name__ == "__main__":
    print("Enter an expression or a string")
    input_expression = input()
    print(Pst.Post_Evaluation((input_expression)))

