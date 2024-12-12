from Precedence import *
from Tokenization import Tokenizer
import re

tk = Tokenizer()
pd = Precedence()


def is_floating_point(num):
    # print(num)
    # print(re.match(r"\d+\.\d+$", num) is not None)
    return re.match(r"\d+\.\d+$", num) is not None


def is_digit(token):
    return token.isdigit()


def is_operator(token):
    return token in pd.OPERATORS


def is_letter(token):
    return token.isalpha()


def is_function(token):
    functions = ["sin", "cos", "tan", "√", "log2", "log10", "log", "alog", "inv"]
    t = token.lower() in functions
    print("t", t)
    return token.lower() in functions
