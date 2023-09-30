from ExpressionChecker import *

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
        #self.tokens=list(self.tokens)
        return self.tokens




#test snippet
#expression = "(1234567890 + 987654321) * 1000000 / 9999 - 555555"
#post = Postfix_Evaluation()
#token= Tokenization()
#result=(token.Tokenize(expression))
#print(result)
#print(post.postfix_Eval(expression))