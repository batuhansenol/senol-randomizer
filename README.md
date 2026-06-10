
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

###  Installation

```bash
pip install senol-randomizer
```

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
|`shuffle()`|Shuffles the given list and returns it. O(n)|`lst`:`list`|`list`|


## RNG Function Tests

Statistical test results based on [NIST SP 800-22 Rev. 1a](https://github.com/dj-on-github/sp800_22_tests) test suite.

| Test | P-Value | Result |
| :--- | :--- | :--- |
| `monobit_test` | 0.046613138703915244 | ✅ <span style="color:green">PASS</span> |
| `frequency_within_block_test` | 0.6787903492122158 | ✅ <span style="color:green">PASS</span> |
| `runs_test` | 0.33232036052397196 | ✅ <span style="color:green">PASS</span> |
| `longest_run_ones_in_a_block_test` | 0.21020703185565603 | ✅ <span style="color:green">PASS</span> |
| `binary_matrix_rank_test` | 0.2571877713800565 | ✅ <span style="color:green">PASS</span> |
| `dft_test` | 0.8685773273998374 | ✅ <span style="color:green">PASS</span> |
| `non_overlapping_template_matching_test` | 0.893926430778068 | ✅ <span style="color:green">PASS</span> |
| `overlapping_template_matching_test` | 0.7796009868841686 | ✅ <span style="color:green">PASS</span> |
| `maurers_universal_test` | 0.9802530560443485 | ✅ <span style="color:green">PASS</span> |
| `linear_complexity_test` | 0.4685290247356243 | ✅ <span style="color:green">PASS</span> |
| `serial_test` | 0.5630465232357214 | ✅ <span style="color:green">PASS</span> |
| `approximate_entropy_test` | 0.5631130245829565 | ✅ <span style="color:green">PASS</span> |
| `cumulative_sums_test` | 0.039939937090386124 | ✅ <span style="color:green">PASS</span> |
| `random_excursion_test` | 0.5178616373360564 | ✅ <span style="color:green">PASS</span> |
| `random_excursion_variant_test` | 0.14694060874229203 | ✅ <span style="color:green">PASS</span> |

> Tests performed with 1 Mibibit (33,554,432 bits) of output data.  
> 15/15 PASS — Work in progress.


----

[Project Repo Github](https://github.com/batuhansenol/senol-randomizer) •  [Project Repo PyPI](https://pypi.org/project/senol-randomizer/)

[Author Github Profile](https://github.com/batuhansenol) • [Author PyPI Profile](https://pypi.org/user/Batuhan_Senol/)



__*--Batuhan Şenol*__