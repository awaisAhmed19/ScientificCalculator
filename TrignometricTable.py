import math

class TrignometricTable:
    
    def __init__(self):
        self.TAN = {
            0: 0,
            30: 1 / math.sqrt(3),
            45: 1,
            60: math.sqrt(3),
            90: None,
            180: 0,
            270: None,
            360: 0
        }

        self.SIN = {
            0: 0,
            30: 1 / 2,
            45: 1 / math.sqrt(2),
            60: math.sqrt(3) / 2,
            90: 1,
            180: 0,
            270: -1,
            360: 0
        }

        self.COS = {
            0: 1,
            30: math.sqrt(3) / 2,
            45: 1 / math.sqrt(2),
            60: 1 / 2,
            90: 0,
            180: -1,
            270: 0,
            360: 1
        }

        self.COT = {
            0: None,
            30: math.sqrt(3),
            45: 1,
            60: 1 / math.sqrt(3),
            90: 0,
            180: None,
            270: 0,
            360: None
        }

        self.COSEC = {
            0: None,
            30: 2,
            45: math.sqrt(2),
            60: 2 / math.sqrt(3),
            90: 1,
            180: None,
            270: -1,
            360: None
        }

        self.SEC = {
            0: 1,
            30: 2 / math.sqrt(3),
            45: math.sqrt(2),
            60: 2,
            90: None,
            180: -1,
            270: None,
            360: -1
        }

    def get(self, trig_function, angle):
        if angle in self.TAN:
            return self.TAN[angle] if trig_function == 'tan' else self.default_value(trig_function)
        elif angle in self.SIN:
            return self.SIN[angle] if trig_function == 'sin' else self.default_value(trig_function)
        elif angle in self.COS:
            return self.COS[angle] if trig_function == 'cos' else self.default_value(trig_function)
        elif angle in self.COT:
            return self.COT[angle] if trig_function == 'cot' else self.default_value(trig_function)
        elif angle in self.COSEC:
            return self.COSEC[angle] if trig_function == 'cosec' else self.default_value(trig_function)
        elif angle in self.SEC:
            return self.SEC[angle] if trig_function == 'sec' else self.default_value(trig_function)
        else:
            return self.default_value(trig_function)
    
    def default_value(self, trig_function):
        if trig_function == 'tan':
            return float('inf')  # Represent undefined as positive infinity for tan
        elif trig_function in ['sin', 'cos', 'cot', 'cosec', 'sec']:
            return None  # Default value for other trig functions can be None
        else:
            raise ValueError("Unknown trigonometric function: {}".format(trig_function))
