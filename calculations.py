import math
from TrignometricTable import *

class Calculations:
    
    def __init__(self) :
        self.x = 0
        self.y = 0

        
    def trigonometric_eval(self, trig, value):
        special_angles = {0, 30, 45, 60, 90, 180, 270, 360}
        if value in special_angles:
            if trig=='sin':
                return SIN.get(value)
            elif trig=='cos':
               return COS.get(value)
            elif trig=='tan':
               return TAN.get(value)
            elif trig=='cot':
               return COT.get(value)
            elif trig=='sec':
               return SEC.get(value)
            elif trig=='cosec':
               return COSEC.get(value)
        else:
           if(trig=='sin' and value not in special_angles):
            angle = self.radian(value)
            result = 0.0
            sign = 1

            for n in range(0, 20):
                term = angle**(2 * n + 1) / math.factorial(2 * n + 1)
                result += sign * term
                sign *= -1
            return result
           elif  (trig=='cos' and value not in special_angles):
            angle = self.radian(value)
            result = 0.0
            sign = 1

            for n in range(0, 20):
                term = angle**(2 * n ) / math.factorial(2 * n )
                result += sign * term
                sign *= -1
            return result

 