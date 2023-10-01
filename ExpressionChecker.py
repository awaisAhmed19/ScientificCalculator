from Precedence import *
pd=Precedence()
def is_digit(token):
        return token.isdigit()

def is_operator(token):
        return token in pd.OPERATORS 
def is_letter(token):
        return token.isalpha()
def Functions():
        return ['sin', 'cos', 'tan', 'sqrt', 'log', 'abs', 'floor', 'ceil', 'max', 'min', 'round']

def is_function(token):
        function=['log','sin','cos','tan','sqrt']
        return token.lower() in function