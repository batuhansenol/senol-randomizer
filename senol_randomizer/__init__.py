from .senol_integer  import createint as newint
from .senol_string import createstr as newstr
from .senol_float import createfloat as newfloat   
from .senol_bool import createbool as newbool
from .senol_byte import createbyte as newbyte
from .core import RNG
from importlib.metadata import version


__version__ = version("senol-randomizer")

def signature(show=False):
    data = (
        f"senol-randomizer v{__version__}\n"
        "Experimental Toolkit\n"
        "Author: Batuhan Şenol\n"
        "-- Batuhan Şenol"
    )

    if show:
        print(data)

    return data

__all__ = [
    "createint",
    "createstr",
    "createfloat",
    "createbool",
    "createbyte",
    "RNG",
    "signature"
]