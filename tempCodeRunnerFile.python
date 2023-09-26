OPERATORS = {'-', '+', '/', '*', '^','(',')','sin','cos','tan'}

PRECEDENCE = {
    '(': 0,  # Parentheses for grouping
    ')': 0,
    '^': 4,  # Exponentiation (highest precedence)
    '*': 3,  # Multiplication and Division
    '/': 3,
    '+': 2,  # Addition and Subtraction
    '-': 2,
    'sin': 5,  # Example: Trigonometric functions
    'cos': 5,
    'tan': 5,
    'sqrt': 5,  # Example: Square root function
}
def is_digit(char):
        return '0' <= char <= '9' or char=='.'
  

def is_operator(char):
        return char in OPERATORS or is_digit(char)

def handle_operator(char):
        while operators and (
            PRECEDENCE[char]<= PRECEDENCE.get(operators[-1], 0 ) 
        ):
            output.append(operators.pop())
        operators.append(char)

def handle_open_parenthesis():
        operators.append('(')

def handle_close_parenthesis():
        while operators and operators[-1] != '(':
            output.append(operators.pop())

        if operators and operators[-1] == '(':
            operators.pop()
        else:
            raise ValueError("Mismatch parenthesis")

output = []
operators = []
def tokenize_expression(expression):
   

    expression = expression.replace(" ", "")  # Remove spaces

    for i in range (0,len(expression)):
        char=expression[i]
        if is_digit(char):
            num=char
            i=+1
            while i<len(expression) and is_digit(expression[i]):
                num+=expression[i]
                i+=1
            output.append(char)
        elif is_operator(char):
            if char == '(':
                handle_open_parenthesis()
            elif char == ')':
                handle_close_parenthesis()
            else:
                handle_operator(char)

    while operators:
        output.append(operators.pop())

    return " ".join(output)
def Evaluate(x,y,operation):
     symbols={
          '+':x+y,
          '-':x-y,
          '*':x*y,
          '/':x/y,
          '^':x**y,
     }
     return symbols.get(operation,0)
     
def postfix_Eval(Eval_expression):
    expression=Eval_expression
    operand=[]
    for char in expression:
         if is_digit(char):
              operand.append(float(char))
         elif is_operator(char):
              op1=operand.pop()
              op2=operand.pop()
              operand.append(Evaluate(op2,op1,char))
    return operand.pop()


if __name__ == "__main__":
    print("Enter an expression or a string")
    input_expression = input()
    postfix_expression = tokenize_expression(input_expression)
    postfix_Eval(postfix_expression)
    print(postfix_Eval(postfix_expression))
    print(postfix_expression)
