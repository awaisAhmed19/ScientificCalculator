from Precedence import *
pd=Precedence()
def is_digit(token):
        return '0'<=token<='9' 

def is_operator(token):
        return token in pd.OPERATORS 
def is_letter(token):
        return token.isalpha()

def is_function(token):
        function={'log','sin','cos','tan','sqrt'}
        return token.lower() in function