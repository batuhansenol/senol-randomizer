
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

```python
import senol_randomizer as sr

sr.newstr(num=10)
sr.newint(_min=10, _max=100)
sr.newfloat(_min=1, _max=20)
sr.newbyte(num=100)
sr.RNG() # This is core function
```

[Project Repo Github](https://github.com/batuhansenol/senol-randomizer) •  [Project Repo PyPI](https://pypi.org/project/senol-randomizer/)

[Author Github Profile](https://github.com/batuhansenol) • [Author PyPI Profile](https://pypi.org/user/Batuhan_Senol/)

__*--Batuhan Şenol*__