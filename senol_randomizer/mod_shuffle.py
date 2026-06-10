





from .core import RNG, compress

def shuffle(lst: list = None) -> list:
    if lst is None:
        raise ValueError("lst cannot be None.")
    
    result = lst.copy()
    n = len(result)
    
    for i in range(n - 1, 0, -1):
        j = compress(value=RNG(), min_val=0, max_val=n - 1)  
        result[i], result[j] = result[j], result[i]
    
    return result


