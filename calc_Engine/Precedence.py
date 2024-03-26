import math

class Precedence:
    OPERATORS = {
        '^',  
        '*',  
        '/',
        '+',  
        '-'
    }

    PRECEDENCE = {
        '(': 0,  
        ')': 0,
        '^': 4,    
        '*': 3,    
        '/': 3,
        '+': 2,    
        '-': 2,
        'sin': 4,  
        'cos': 4,  
        'tan': 4,  
        'Sqrt': 4, 
        'log': 4,  
        'abs': 4,  
        'floor': 4, 
        'ceil': 4,  
        'max': 4,   
        'min': 4,   
        'round': 4, 
        '!': 5     
    }

    LEFT_ASSOCIATIVE = {
        '^': False,  
        '*': True,  
        '/': True,  
        '+': True,   
        '-': True,  
        '!': False  
    }

    