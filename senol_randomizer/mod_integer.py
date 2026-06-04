import gmpy2 as g
from .core import RNG, ms, compress

def createint(
        _min:int = 0,
        _max:int = 100
):
    
    if _min >= _max:
        raise ValueError("The _min argument cannot be greater than or equal to the _max argument.")

    return compress(x=RNG(), a=_min, b=_max)
