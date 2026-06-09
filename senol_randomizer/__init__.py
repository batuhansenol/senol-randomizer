from .mod_integer  import createint as newint
from .mod_string import createstr as newstr
from .mod_float import createfloat as newfloat   
from .mod_bool import createbool as newbool
from .mod_byte import createbyte as newbyte
from .core import RNG
from .core import compress
from .mod_choice import choice
from .mod_shuffle import shuffle


from importlib.metadata import version

try:
    __version__ = version("senol-randomizer")
except Exception:
    __version__ = "0.0.0"



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
    "newint",
    "newstr",
    "newfloat",
    "newbool",
    "newbyte",
    "RNG",
    "signature",
    "choice",
    "compress",
    "shuffle"
]