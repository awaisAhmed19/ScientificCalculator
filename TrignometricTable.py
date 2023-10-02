import math

    
    
TAN = {
            0: 0,
            30: 1 / math.sqrt(3),
            45: 1,
            60: math.sqrt(3),
            90: None,
            180: 0,
            270: None,
            360: 0
        }

SIN = {
            0: 0,
            30: 1 / 2,
            45: 1 / math.sqrt(2),
            60: math.sqrt(3) / 2,
            90: 1,
            180: 0,
            270: -1,
            360: 0
        }

COS = {
            0: 1,
            30: math.sqrt(3) / 2,
            45: 1 / math.sqrt(2),
            60: 1 / 2,
            90: 0,
            180: -1,
            270: 0,
            360: 1
        }

COT = {
            0: None,
            30: math.sqrt(3),
            45: 1,
            60: 1 / math.sqrt(3),
            90: 0,
            180: None,
            270: 0,
            360: None
        }

COSEC = {
            0: None,
            30: 2,
            45: math.sqrt(2),
            60: 2 / math.sqrt(3),
            90: 1,
            180: None,
            270: -1,
            360: None
        }

SEC = {
            0: 1,
            30: 2 / math.sqrt(3),
            45: math.sqrt(2),
            60: 2,
            90: None,
            180: -1,
            270: None,
            360: -1
        }

    