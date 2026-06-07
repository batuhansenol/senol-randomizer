
from .core import RNG, compress, ms

def choice(
        lst:list=None
):
    if lst is None:
        raise ValueError("lst value i cannot None.")
    
    return lst[compress(value=RNG(), min_val=0, max_val=(len(lst)-1))]