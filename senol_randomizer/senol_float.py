from .core import RNG, compress, ms

def createfloat(_min: int = 0, _max: int = 1) -> float:

    if _min >= _max:
        raise ValueError("The _min argument cannot be greater than or equal to the _max argument.")

    inte = compress(a=_min, b=_max, x=RNG())
    flo = compress(a=0, b=100000000000, x=RNG())
    return float(f"{inte}.{flo}")
