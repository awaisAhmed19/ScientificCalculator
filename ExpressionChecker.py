from Precedence import *

pd=Precedence()
def is_digit(token):
        return token.isdigit()

def is_operator(token):
        return token in pd.OPERATORS 
def is_letter(token):
        return token.isalpha()
def Functions():
        return ['sin', 'cos', 'tan', 'sqrt', 'log2','log10', 'abs', 'floor', 'ceil', 'max', 'min', 'round']

def is_function(token):
        function=['sin', 'cos', 'tan', 'sqrt', 'log2','log10', 'abs', 'floor', 'ceil', 'max', 'min', 'round']
        return token.lower() in function