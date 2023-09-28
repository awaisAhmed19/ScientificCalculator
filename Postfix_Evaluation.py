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
            
            if is_digit(char):
                  self.operand.append(float(char))
            elif char=='!':
                     op1=self.operand.pop()
                     self.operand.append(cal.factorial(op1))
            elif is_operator(char):
                op1=self.operand.pop()
                op2=self.operand.pop()
                self.operand.append(Evaluate(op2,op1,char))
        return self.operand.pop()


#test snippet
#expression = "2! + 3! - 4!"
#post = Postfix_Evaluation()
#token= PostfixConv()
#expression=" ".join(token.postfix(expression))
#print(expression)
#print(post.postfix_Eval(expression))