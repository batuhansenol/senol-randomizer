

from .mod_choice import choice

def shuffle(
        lst:list=None
) -> list :
    
    if lst is None:
        raise ValueError("lst value i cannot None.")
    
    shuffle_lst = []

    while len(lst) != 0:

        select = choice(lst=lst)

        shuffle_lst.append(select)
        lst.remove(select)

    return shuffle_lst







