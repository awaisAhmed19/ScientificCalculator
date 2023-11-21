import math

from TrignometricTable import *


class Calculations:
    
    def __init__(self) :
        self.x = 0
        self.y = 0

    def _sin(self,value):
        angle = math.radians(value)
        result = 0.0
        sign = 1

        for n in range(0, 20):
                term = angle**(2 * n + 1) / math.factorial(2 * n + 1)
                result += sign * term
                sign *= -1
        return result
    
    def _cos(self,value):
        angle = math.radians(value)
        result = 0.0
        sign = 1

        for n in range(0, 20):
                term = angle**(2 * n ) / math.factorial(2 * n )
                result += sign * term
                sign *= -1
        return result
    
    def _tan(self,value):
        angle=math.radians(value)
        x=(angle-90)/(angle+90)
        y=math.sqrt((1-x)*(1+x))/2
        return round(y, 10)
    
    def _sqrt(self,value):
        return value**0.5

    def function_eval(self, func, value):
        special_angles = {0, 30, 45, 60, 90, 180, 270, 360}
        if value in special_angles:
            match func:
                case 'sin':
                    return SIN.get(value)
                case 'cos':
                    return COS.get(value)
                case 'tan':
                    return TAN.get(value)
                case 'cot':
                    return COT.get(value)
                case 'sec':
                    return SEC.get(value)
                case 'cosec':
                    return COSEC.get(value)
        else:
            match func:
                case 'sin':
                    return self._sin(value)
                case 'cos':
                    return self._cos(value)
                case 'tan':
                    return self._tan(value)
                case 'sqrt':
                    return self._sqrt(value)
              

 