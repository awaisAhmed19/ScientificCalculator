import math
class calculation:
    
     def __init__(self) :
          self.x=0
          self.y=0
     def Tignometric_Eval(self,TrigFunction,value):
          if TrigFunction=="sin":
             self.sine(value)
          #elif TrigFunction=="cos" :
           #  cosine(value)
          #elif TrigFunction=="tan":
           #  tan(value)
          
          
         
          return 
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
     def radian(self,angle):
         return angle*(math.pi/180)

     def sine(self,angle):
         angle=self.radian(angle)
         result=0.0
         sign=1

         for n in range(0,20):
             term=(self.power(angle,(2*n+1))/self.factorial(2*n+1))
             result+=sign*term
             sign*=-1
         return (result) 
     def cosine(self,angle):
         angle=self.radian(angle)
         result=0.0
         sign=1

         for n in range(0,20):
             term=(self.power(angle,(2*n))/self.factorial(2*n))
             result+=sign*term
             sign*=-1
          
         return (result)
     
     def tan(self,angle):
         result=self.sine(angle)/self.cosine(angle)
         if(result<=-1000000000):
             result=0
         return (result)

     def secant(self,angle):
         return (1/self.cosine(angle))
     
     def cotangent(self,angle):
         return (1/self.tan(angle))
     
     def cosecant(self,angle):
         return (1/self.sine(angle))
#angle=int(input())
#cal=calculation()
#print(cal.tan(angle))
#print(cal.cosine(angle))
#print(cal.cotangent(angle))
#print(cal.secant(angle))
#print(cal.cosecant(angle))
#print(cal.sine(angle))
