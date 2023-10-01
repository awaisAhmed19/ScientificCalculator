import math
from TrignometricTable import *

class Calculations:
    
    def __init__(self) :
        self.x = 0
        self.y = 0
    def evaluate_operation(self,op2, op1, token):
        match token:
            case '+': self.add(op2,op1)
            case '-': self.sub(op2,op1)
            case '*': self.mul(op2,op1)
            case '/': self.div(op2,op1)
            case '^': self.power(op2,op1)
        
    def trigonometric_eval(self, trig_function, value):
        special_angles = {0, 30, 45, 60, 90, 180, 270, 360}
        if value in special_angles:
            return TrignometricTable().get(trig_function.upper(), value)
        else:
            angle = self.radian(value)
            result = 0.0
            sign = 1

            for n in range(0, 20):
                term = angle**(2 * n + 1) / math.factorial(2 * n + 1)
                result += sign * term
                sign *= -1
            return result

    def add(self, x, y):
        if x is None or y is None:
            raise ValueError("One or both operands are None; addition is not possible.")
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x / y

    def power(self, x, y):
        if y == 0:
            return 1
        if y % 2 == 0:
            temp = self.power(x, y // 2)
            return temp * temp
        else:
            temp = self.power(x, (y - 1) // 2)
        return x * temp * temp 

    def factorial(self, x):
        if x == 0:
            return 1
        else:
            return x * self.factorial(x - 1)

    def radian(self, angle):
        return angle * (math.pi / 180)
