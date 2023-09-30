from Precedence import Precedence
pd=Precedence()
from ExpressionChecker import *

from Tokenization import Tokenization
    
class PostfixConv (Tokenization):
    def __init__(self) :
        super().__init__()
        self.output=[]
        self.operator=[]
    
    def postfix(self,expression):

        tokenList=self.Tokenize(expression)
        #index=0

        for i in tokenList:
            #i=tokenList[index]
            if is_digit(i) or is_letter(i):
                self.output.append(i)
            elif is_function(i):
                self.operator.append(i)
            
            elif i=='(':
                self.operator.append(i)

            elif i==')':
                while self.operator and self.operator[-1]!='(':
                    self.output.append(self.operator.pop())

                if self.operator and self.operator[-1]=='(':
                    self.operator.pop() #Remove the '('
                #index+=1
                if len(self.operator)>0 and is_function(self.operator[-1]):
                    self.output.append(self.operator.pop())
                    
            elif is_operator(i):
                while (
                    self.operator
                    and self.operator[-1]!='('
                    and (
                        pd.PRECEDENCE[i]<=pd.PRECEDENCE.get(self.operator[-1],0)
                    or (
                        pd.PRECEDENCE[i]==pd.PRECEDENCE.get(self.operator[-1],0)
                        and pd.LEFT_ASSOCIATIVE.get(i,True)
                    )
                    )
                ):
                    self.output.append(self.operator.pop())
                self.operator.append(i)

        while self.operator:
            self.output.append(self.operator.pop())    
        return " ".join(self.output)





#test snippet

#expression = "(3+3)*10/9-5"
#expression = "['(', '1234567890', '+', '987654321', ')', '*', '1000000', '/', '9999', '-', '555555']"
#post = PostfixConv()
#token= Tokenization()
#print(token.Tokenize(expression))
#print("".join(post.postfix(expression)))


