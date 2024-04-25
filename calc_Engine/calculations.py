import math

from TrignometricTable import *

PI = 3.14159265358979323846

class Calculations:

    def __init__(self):
        self.x = 0
        self.y = 0

    def _rad(self, value):
        return (PI/180) * value

    def _deg(self, value):
        return (180/PI) * value

    def _sin(self, value):
        angle = self._rad(value)
        result = 0.0
        sign = 1

        for n in range(0, 20):
            # Calculate each term using the formula: angle^(2n+1)/(2n+1)!
            term = angle**(2 * n + 1) / math.factorial(2 * n + 1)
            result += sign * term
            sign *= -1

        return result

    def _cos(self, value):
        angle = self._rad(value)
        result = 0.0
        sign = 1
        for n in range(0, 20):
            # Calculate each term using the formula: angle^(2n)/(2n)!
            term = angle**(2 * n) / math.factorial(2 * n)
            result += sign * term
            sign *= -1

        return result

    def _tan(self, value):
        # angle-90/angle+90 assigning it to x
        # sqrt of(1-x)(1+x)/2
        angle = self._rad(value)
        x = (angle - 90) / (angle + 90)
        y = math.sqrt((1 - x) * (1 + x)) / 2
        return round(y, 10)

    def _sqrt(self, value):
        return value**0.5

    def _log2(self, value, precision=0.000000000000001):
        if value <= 0:
            return None
        if value == 1:
            return 0

        low = 0
        high = value
        result = -1
        while low <= high:
            mid = low + (high - low) / 2

            if abs(2**mid - value) < precision:
                result = mid
                break
            elif 2**mid < value:
                low = mid + precision
                result = mid
            else:
                high = mid - precision

        return result

    def _alog(self, value):
        return 10**value
    def _inv(self,value):
        return 1/value
    def _log10(self, value, precision=0.000000000000001):
        if value <= 0:
            return None
        if value == 1:
            return 0

        low = 0
        high = value
        result = -1

        while low <= high:
            mid = low + (high - low) / 2

            if abs(10**mid - value) < precision:
                result = mid
                break
            elif 10**mid < value:
                low = mid + precision
                result = mid
            else:
                high = mid - precision

        return result

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
                case 'log2':
                    return self._log2(value)
                case 'log10':
                    return self._log10(value)
                case 'log':
                    return self._log10(value)
                case 'alog':
                    return self._alog(value)
                case 'inv':
                    return self._inv(value)
