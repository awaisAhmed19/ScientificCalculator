from PostfixConv import PostfixConv
from ExpressionChecker import is_digit,is_operator, is_function, is_letter
from calculations import Calculations

cal=Calculations()
PC=PostfixConv()
#c=calc()

top=-1
class Post_Evaluation():
    def __init__(self):
        self.output=[]
    def evaluate(self,a,b,token):
        if token=='+':
            return self.add(a,b)
        elif token=='-':
            return self.sub(a,b)
        elif token=='*':
            return self.mul(a,b)
        elif token=='/':
            return self.div(a,b)
        elif token=='^':
            return self.power(a,b)
        
    def Post_Evaluation(self,Expression):
        for token in Expression:
            if is_digit(token)or token[0]=='-' and is_digit(token[1:]):
                self.output.append(float(token))
            
            elif is_operator(token):
                op1=self.output.pop()
                op2=self.output.pop()
                self.output.append(self.evaluate(op2,op1,token))
            elif token=='!':
                 ope=self.output.pop()
                 self.output.append(self.Fact(ope))
            elif is_function(token):
                value=int(self.output.pop())
                trigFunc=token
                self.output.append(cal.trigonometric_eval(trigFunc,value))
            result=self.output
        return result


    def add(self,x,y): return x+y
    def sub(self,x,y): return x-y
    def mul(self,x,y): return x*y
    def div(self,x,y): 
        if y==0: raise "cant div by zero"
        else:
            return x/y
    def power(self,x,y):
        if y==0:
            return 1
        else:
            if y%2==0:
                temp=self.power(x,y//2)
                return temp*temp
            else:
                temp=self.power(x,(y-1)//2)
                return temp*temp*x

    def Fact(self,op):
     if op==0:
          return 1
     else :
          return op*self.Fact(op-1)
     

#pst=Post_Evaluation()
#exp= "45 sin 30 cos + 60 tan -"

#result=pst.Post_Evaluation(exp)
#print(result)