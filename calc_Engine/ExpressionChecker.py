from Precedence import *
from Tokenization import Tokenizer

# Initialize a Tokenizer instance
tk = Tokenizer()

# Initialize a Precedence instance
pd = Precedence()

# Function to check if a token is a digit
def is_digit(token):
    return token.isdigit()

# Function to check if a token is an operator
def is_operator(token):
    return token in pd.OPERATORS

# Function to check if a token is a letter
def is_letter(token):
    return token.isalpha()

# Function to check if a token is a recognized function
def is_function(token):
    # List of recognized functions
    functions = ['sin', 'cos', 'tan', 'sqrt', 'log2', 'log10', 'log', 'alog']
    
    # Check if the lowercase version of the token is in the list of functions
    return token.lower() in functions
