
# senol-randomizer

An RNG-core-based random data generator written in a cryptographic style, but lacking any cryptographic proof, which creates an information asymmetry between the program and urandom.

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
|`newstr()`|Create random string with unicode range.|`num`:`int`, `_min`:`int`, `_max`:`int`|`str`|
|`newint()`|Create random integer with range.|`_min`:`int`, `_max`:`int`|`int`|
|`newfloat()`|Create random float with range.|`_min`:`int`, `_max`:`int`|`float`
|`newbyte()`|Create random bytes.|`num`:`int`|`bytes`|
|`newbool()`|Create random bool.|No Argument|`bool`|
|`RNG()`|Core of library, create random big integer without range.|No argument|`int`


[Project Repo Github](https://github.com/batuhansenol/senol-randomizer) •  [Project Repo PyPI](https://pypi.org/project/senol-randomizer/)

[Author Github Profile](https://github.com/batuhansenol) • [Author PyPI Profile](https://pypi.org/user/Batuhan_Senol/)

__*--Batuhan Şenol*__