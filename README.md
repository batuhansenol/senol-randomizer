
# senol-randomizer

An RNG-core-based random data generator written in a cryptographic style, but lacking any cryptographic proof, which creates an information asymmetry between the program and urandom.

----

![logo](logo.png)

![python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Type](https://img.shields.io/badge/API-File%20Operations-informational)
![Github]( https://img.shields.io/badge/github-repo-blue?logo=github)
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="20"/>

### How does it work?

- First, it takes 256-bit numbers from __/dev/urandom__.
- Second, it processes these numbers using the powmod() function from the gmpy library, applying the operation a
b
modn, and does this for each __*n*__.
- The list of n values consists of 256-bit *prime* numbers.
- This output is also used in the generation of other data types.

### How To Use?


|Function Name|Description|Arguments|Returns|
|-------------|-----------|---------|-------|
|`newstr()`|Create random string with unicode range.|`num`:`int`, `min_val`:`int`, `max_val`:`int`|`str`|
|`newint()`|Create random integer with range.|`min_val`:`int`, `max_val`:`int`|`int`|
|`newfloat()`|Create random float with range.|`min_val`:`int`, `max_val`:`int`|`float`|
|`newbyte()`|Create random bytes.|`num`:`int`|`bytes`|
|`newbool()`|Create random bool.|No Argument|`bool`|
|`RNG()`|Core of library, create random big integer without range.|No argument|`int`|
|`choice()`|Selects a random element from the list.|`lst`:`list`|`any`|
|`compress()`|Maps the given number into the range between min and max in a way that minimizes modulo bias.|`value`,`min_val`:`int`,`max_val`:`int`| `int`|

----

[Project Repo Github](https://github.com/batuhansenol/senol-randomizer) •  [Project Repo PyPI](https://pypi.org/project/senol-randomizer/)

[Author Github Profile](https://github.com/batuhansenol) • [Author PyPI Profile](https://pypi.org/user/Batuhan_Senol/)



__*--Batuhan Şenol*__