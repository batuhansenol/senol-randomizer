

from .mod_string import createstr
from .core import compress, RNG

def create():
    return compress(value=RNG(), min_val=0, max_val=len(alp))

alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~")

def url_safe(
    length:int=10
):
    lst = []
    
    for _ in range(length):
        lst.append(create())
        
    return ''.join(lst)