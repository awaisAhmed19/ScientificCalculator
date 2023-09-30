from ExpressionChecker import *
from calculations import calculation

cal=calculation()  
def Evaluate(x,y,operation):
        symbols={
          '+':cal.add(x,y),
          '-':cal.sub(x,y),
          '*':cal.mul(x,y),
          '/':cal.div(x,y),
          '^':cal.power(x,y),
        } 
        return symbols.get(operation)

class Postfix_Evaluation:
    def __init__(self):
         self.operand=[]
         
    def postfix_Eval(self,Eval_expression):
        expression=Eval_expression
        for char in expression:
            print(char)
            if is_digit(char):
                  self.operand.append(float(char))
            elif is_function(char) :
                  TrigFunction=char
                  value=self.operand.pop()
                  self.operand(cal.Tignometric_Eval(TrigFunction,value))
            elif char=='!':
                     op1=self.operand.pop()
                     self.operand.append(cal.factorial(op1))
            elif is_operator(char):
                op1=self.operand.pop()
                op2=self.operand.pop()
                self.operand.append(Evaluate(op2,op1,char))
        return self.operand.pop()
#test code
#ex="1234567890 987654321 + 1000000 * 9999 / 555555 -"
#Pe=Postfix_Evaluation()
#print(Pe.postfix_Eval(ex))