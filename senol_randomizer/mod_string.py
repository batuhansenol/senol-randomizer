from .core import ms, RNG, compress
import string as s
import gmpy2 as g

alp = list(s.ascii_letters + s.digits)

def createstr(
        
        min_val: int = 32,
        max_val: int = 122,
        num: int = 10,

        charsandnumbers: bool = False

        ):
    
    if min_val >= max_val:
        raise ValueError("The min_val argument cannot be greater than or equal to the max_val argument.")
    
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
            data.append(chr(compress(value=i, min_val=min_val, max_val=max_val)))

        return ''.join(data)
    

        

        


