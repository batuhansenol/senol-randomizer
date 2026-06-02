from .core import ms, RNG, compress
import string as s
import gmpy2 as g

alp = list(s.ascii_letters + s.digits)

def createstr(
        
        _min: int = 32,
        _max: int = 122,
        num: int = 10,

        charsandnumbers: bool = False

        ):
    
    if _min >= _max:
        raise ValueError("The _min argument cannot be greater than or equal to the _max argument.")
    
    if charsandnumbers == True:

        nums = []
        data = []

        for _ in range(num):
            nums.append(g.mpz(RNG()))

        for i in nums:
            data.append(alp[g.mod(i, len(alp))])

        return ''.join(data)
    
    else:

        nums = []
        data = []

        for _ in range(num):
            nums.append(g.mpz(RNG()))

        for i in nums:
            data.append(chr(compress(x=i, a=_min, b=_max)))

        return ''.join(data)
    

        

        


