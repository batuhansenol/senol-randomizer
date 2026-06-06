from .core import RNG, compress, ms

def createfloat(min_val: int = 0, max_val: int = 1) -> float:

    if min_val >= max_val:
        raise ValueError("The _min argument cannot be greater than or equal to the _max argument.")

    inte = compress(min_val=min_val, max_val=(max_val-1), value=RNG())
    flo = compress(min_val=0, max_val=100000000000, value=RNG())
    return float(f"{inte}.{flo}")
