from PostfixConv import is_digit 
from PostfixConv import is_operator 

#from Expression_handler import is_digit

def Evaluate(x,y,operation):
        symbols={
          '+':x+y,
          '-':x-y,
          '*':x*y,
          '/':x/y,
          '^':x**y,
        } 
        return symbols.get(operation,0)
class Postfix_Evaluation:
    def __init__(self):
         self.operand=[]
         
    def postfix_Eval(self,Eval_expression):
        expression=Eval_expression
        for char in expression:
            
            if is_digit(char):
                  self.operand.append(float(char))
                  
            elif is_operator(char):
                op1=self.operand.pop()
                op2=self.operand.pop()
                self.operand.append(Evaluate(op2,op1,char))
        return self.operand.pop()