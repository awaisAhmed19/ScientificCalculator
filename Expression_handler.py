from Precedence import Precedence
pd=Precedence()
operators=[]
output=[]
def is_digit(char):
        return '0' <= char <= '9' or char=='.' 
class Expression_handler: 
    
    def is_operator(self,char):
        return char in pd.OPERATORS or is_digit(char)
    
    

    def handle_operator(self,char):
        while operators and (
            pd.PRECEDENCE[char]<= pd.PRECEDENCE.get(operators[-1], 0 ) 
        ):
            output.append(operators.pop())
        operators.append(char)

    def handle_open_parenthesis(self):
        operators.append('(')

    def handle_close_parenthesis(self):
        while operators and operators[-1] != '(':
            output.append(operators.pop())

        if operators and operators[-1] == '(':
            operators.pop()
        else:
            raise ValueError("Mismatch parenthesis")
