import gmpy2 as g
from .core import RNG, ms, compress

def createint(
        min_val:int = 0,
        max_val:int = 100
):
    
    if min_val >= max_val:
        raise ValueError("The _min argument cannot be greater than or equal to the _max argument.")

    return compress(value=RNG(), min_val=min_val, max_val=max_val)
