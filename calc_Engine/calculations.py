import math

from TrignometricTable import *

PI = 3.14159265358979323846

class Calculations:

    def __init__(self):
        self.x = 0
        self.y = 0

    def _rad(self, value):
        # returns pi/180 multiplied by value
        return (PI/180) * value

    def _deg(self, value):
        # returns 180 divided by pi multiplied by value
        return (180/PI) * value

    def _sin(self, value):
        # Convert the angle to radians
        angle = self._rad(value)

        # Initialize variables
        result = 0.0
        sign = 1

        # Loop through 20 terms of the Taylor series expansion
        for n in range(0, 20):
            # Calculate each term using the formula: angle^(2n+1)/(2n+1)!
            term = angle**(2 * n + 1) / math.factorial(2 * n + 1)

            # Add the term to the result with the current sign (positive or negative)
            result += sign * term

            # Alternate the sign for the next term in the series
            sign *= -1

        return result

    def _cos(self, value):
        # Convert the angle to radians
        angle = self._rad(value)

        # Initialize variables
        result = 0.0
        sign = 1

        # Loop through 20 terms of the Taylor series expansion
        for n in range(0, 20):
            # Calculate each term using the formula: angle^(2n)/(2n)!
            term = angle**(2 * n) / math.factorial(2 * n)

            # Add the term to the result with the current sign (positive or negative)
            result += sign * term

            # Alternate the sign for the next term in the series
            sign *= -1

        return result

    def _tan(self, value):
        # Converting the value into radians
        # angle-90/angle+90 assigning it to x
        # sqrt of(1-x)(1+x)/2
        angle = self._rad(value)
        x = (angle - 90) / (angle + 90)
        y = math.sqrt((1 - x) * (1 + x)) / 2
        return round(y, 10)

    def _sqrt(self, value):
        # Square root of a number
        # Getting the square of 1/2
        return value**0.5

    def _log2(self, value, precision=0.000000000000001):
        # Checking if value is less than or equal to 0 or if it is exactly 1
        if value <= 0:
            return None
        if value == 1:
            return 0

        # Initializing low and high variables for binary search
        low = 0
        high = value
        result = -1

        # While loop continues until low is less than or equal to high
        while low <= high:
            # Calculate the midpoint
            mid = low + (high - low) / 2

            # Check if the absolute difference between 2^mid and the target value is less than the specified precision
            if abs(2**mid - value) < precision:
                # If the condition is met, set the result to the current midpoint and break out of the loop
                result = mid
                break
            elif 2**mid < value:
                # If 2^mid is less than the target value, update low and result accordingly
                low = mid + precision
                result = mid
            else:
                # If 2^mid is greater than the target value, update high
                high = mid - precision

        # Return the result of the binary search
        return result

    def _alog(self, value):
        # Just returning a 10^value
        return 10**value

    def _log10(self, value, precision=0.000000000000001):
        # Checking if value is less than or equal to 0 or if it is exactly 1
        if value <= 0:
            return None
        if value == 1:
            return 0

        # Initializing low and high variables for binary search
        low = 0
        high = value
        result = -1

        # While loop continues until low is less than or equal to high
        while low <= high:
            # Calculate the midpoint
            mid = low + (high - low) / 2

            # Check if the absolute difference between 10^mid and the target value is less than the specified precision
            if abs(10**mid - value) < precision:
                # If the condition is met, set the result to the current midpoint and break out of the loop
                result = mid
                break
            elif 10**mid < value:
                # If 10^mid is less than the target value, update low and result accordingly
                low = mid + precision
                result = mid
            else:
                # If 10^mid is greater than the target value, update high
                high = mid - precision

        # Return the result of the binary search
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
