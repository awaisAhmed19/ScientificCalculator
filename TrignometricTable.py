import math
class TrignometricTable:
    TAN={
        0:0,
        30:1/math.sqrt(3),
        45:1,
        60:math.sqrt(3),
        90:"undefined",
        180: 0,
        270:"undefined",
        360:0
    }
    
    SIN={
        0:0,
        30:1/2,
        45:1/math.sqrt(2),
        60:math.sqrt(3)/2,
        90:1,
        180: 0,
        270:-1,
        360:0
    }
    COS={
        0:1,
        30:math.sqrt(3)/2,
        45:1/math.sqrt(2),
        60:1/2,
        90:0,
        180: -1,
        270:0,
        360:1
    }
    COT={
        0:"undefined",
        30:math.sqrt(3),
        45:1,
        60:1/math.sqrt(3),
        90:0,
        180: "undefined",
        270:0,
        360:"undefined"
    } 
    COSEC={
        0:"undefined",
        30:2,
        45:math.sqrt(2),
        60:2/math.sqrt(3),
        90:1,
        180: "undefined",
        270:-1,
        360:"undefined"
    } 
    SEC={
        0:1,
        30:2/math.sqrt(3),
        45:math.sqrt(2),
        60:2,
        90:"undefined",
        180:-1 ,
        270:"undefined",
        360:-1
    }  