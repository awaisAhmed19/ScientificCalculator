

from Precedence import *
from Tokenization import Tokenizer

tk=Tokenizer()
pd=Precedence()

def is_digit(token):
        return token.isdigit()

def is_operator(token):
        return token in pd.OPERATORS
def is_letter(token):
        return token.isalpha()
def is_function(token):
        function=['sin', 'cos', 'tan', 'sqrt', 'log2','log10','log','alog']
        return token.lower() in function