
# senol-randomizer

An RNG-core-based random data generator written in a cryptographic style, but lacking any cryptographic proof, which creates an information asymmetry between the program and urandom.

### How does it work?

- First, it takes 256-bit numbers from __/dev/urandom__.
- Second, it processes these numbers using the powmod() function from the gmpy library, applying the operation a
b
modn, and does this for each __*n*__.
- The list of n values consists of 256-bit *prime* numbers.
- This output is also used in the generation of other data types.

[Project Repo Github](https://github.com/batuhansenol/pyfastfile) - [Author Profile](https://github.com/batuhansenol)

__*--Batuhan Şenol*__