import math

# Lookup table for tangent (TAN) values at specific angles
TAN = {
    0: 0,
    30: 1 / math.sqrt(3),
    45: 1,
    60: math.sqrt(3),
    90: None,
    180: 0,
    270: None,
    360: 0,
}

# Lookup table for sine (SIN) values at specific angles
SIN = {
    0: 0,
    30: 1 / 2,
    45: 1 / math.sqrt(2),
    60: math.sqrt(3) / 2,
    90: 1,
    180: 0,
    270: -1,
    360: 0,
}

# Lookup table for cosine (COS) values at specific angles
COS = {
    0: 1,
    30: math.sqrt(3) / 2,
    45: 1 / math.sqrt(2),
    60: 1 / 2,
    90: 0,
    180: -1,
    270: 0,
    360: 1,
}
