import math
def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))
def asin(x):
    return math.degrees(math.asin(x))
def acos(x):
    return math.degrees(math.acos(x))
def atan(x):
    return math.degrees(math.atan(x))
def get_uni(unicode):
    x=int(unicode,16)
    return f'{x:c}'
