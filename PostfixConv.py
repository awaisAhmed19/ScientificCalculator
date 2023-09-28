from Precedence import Precedence
pd=Precedence()

def is_digit(token):
    return '0'<=token<='9' 

def is_operator(token):
    return token in pd.OPERATORS 
def is_letter(token):
    return token.isalpha()

def is_function(token):
    function={'log','sin','cos','tan','sqrt'}
    return token.lower() in function

class Tokenization:
    def __init__(self) :
        self.tokens=[]
        self.buffer=""
        self.in_parenthesis=False
    
    def Tokenize(self, expression):
        for token in expression:
            if self.in_parenthesis:
                if token==')':
                    self.buffer+=token
                    self.tokens.append(self.buffer)
                    self.buffer=""
                    self.in_parenthesis=False
                else:
                    self.buffer +=token
            elif is_digit(token) or token=='.':

                self.buffer+=token 

            elif is_letter(token):

                self.buffer+=token

            elif is_operator(token):

                if self.buffer:

                    self.tokens.append(self.buffer)
                    self.buffer=""
                self.tokens.append(token)
            elif token in'()':
                if self.buffer:
                    self.tokens.append(self.buffer)
                    self.buffer=""
                self.tokens.append(token)
            elif token =='(':
                if self.buffer:
                    self.tokens.append(self.buffer)
                    self.buffer=""
                self.tokens.append(token)
                self.in_parenthesis=True
            elif token==' ':
                continue
            else:
                pass
        if self.buffer:
            self.tokens.append(self.buffer)
        return self.tokens
        
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
                    and pd.PRECEDENCE[i]<=pd.PRECEDENCE.get(self.operator[-1],0)
                    
                ):
                    self.output.append(self.operator.pop())
                self.operator.append(i)
            
            elif is_function(i):
                self.operator.append(i)
            #index += 1


        while self.operator:
            self.output.append(self.operator.pop())    
        return self.output







expression = "(3 * x^2 + 5 * x - 8) / (2 * x + 1)"
post = PostfixConv()
token= Tokenization()
print(token.Tokenize(expression))
print(" ".join(post.postfix(expression)))


