from .core import logic, ms, rbyte

def createbyte(num:int=10):

    a = rbyte(num)
    b = rbyte(num)
    c = rbyte(num)

    for _ in range(30):
        
        a = logic(a, b, c)
        b = logic(b, c, a)
        c = logic(c, a, b)

    return a



