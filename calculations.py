import math
from TrignometricTable import *
Trig=TrignometricTable()
class calculation:
    
     def __init__(self) :
          self.x=0
          self.y=0
     def Tignometric_Eval(self,TrigFunction,value):
            match TrigFunction:
                case 'sin': return self.sine(value)
                case 'cos': return self.cosine(value)
                case 'tan': return self.tan(value)
                case 'cosec': return self.cosecant(value)
                case 'sec': return self.secant(value)
                case 'cot': return self.cotangent(value)
         
            
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
             
         return  x*temp*temp 
     

     def factorial(self,x):
          if(x==0):
           return 1
          else:
               return x*self.factorial(x-1)
          

     def radian(self,angle):
         return angle*(math.pi/180)
     


     def sine(self,angle):
        int(angle)
        if(angle in {0,30,45,60,90,180,270,360}):
            result= Trig.SIN.get(angle,0)
            return result
        else:    
            angle=self.radian(angle)
            result=0.0
            sign=1

            for n in range(0,20):
                term=angle**(2*n+1)/math.factorial(2*n+1)
                result+=sign*term
                sign*=-1
            return (result) 
    
        
     def cosine(self,angle):
        int (angle)
        if(angle in {0,30,45,60,90,180,270,360}):
            result= Trig.COS.get(angle,0)
            return result
        else:
         angle=self.radian(angle)
         result=0.0
         sign=1

         for n in range(0,20):
             term=(self.power(angle,(2*n))/self.factorial(2*n))
             result+=sign*term
             sign*=-1
          
         return (result)
     
     def tan(self,angle):
         int(angle)
         if(angle in {0,30,45,60,90,180,270,360}):
            result= Trig.TAN.get(angle,0)
            return result
         result=self.sine(angle)/self.cosine(angle)
         return (result)

     def secant(self,angle):
         int(angle)
         if(angle in {0,30,45,60,90,180,270,360}):
            result= Trig.SEC.get(angle,0)
            return result
         return (1/self.cosine(angle))
     
     def cotangent(self,angle):
         int(angle)
         if(angle in {0,30,45,60,90,180,270,360}):
            result= Trig.COT.get(angle,0)
            return result
         return (1/self.tan(angle))
     
     def cosecant(self,angle):
         int(angle)
         if(angle in {0,30,45,60,90,180,270,360}):
            result= Trig.COSEC.get(angle,0)
            return result
         return (1/self.sine(angle))
     
#test snippet
#angle=int(input())
#cal=calculation()
#print(cal.tan(angle))
#print(cal.cosine(angle))
#print(cal.cotangent(angle))
#print(cal.secant(angle))
#print(cal.cosecant(angle))
#print(cal.sine(angle))
