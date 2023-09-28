class calculation:
    def __init__(self) :
          self.x=0
          self.y=0
    def add(self,x,y):
         return x+y
    def sub(self,x,y):
         return x-y
    def mul(self,x,y):
         return x*y
    def div(self,x,y):
         return x/y
    def power(self,x,y):
         if(y==0):
              return 1
         if y%2==0:
              temp=self.power(x,y//2)
              return temp*temp
         else:
              temp=self.power(x,(y-1)//2)
              result=x*temp*temp 
         return result
    def factorial(self,x):
     if(x==0):
          return 1
     else:
          return x*self.factorial(x-1)