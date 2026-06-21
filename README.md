# senol-randomizer

An RNG-core-based random data generator written in a cryptographic style — but lacking any cryptographic proof — which creates an information asymmetry between the program and `/dev/urandom`.

---

![logo](logo.png)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)]()
[![GitHub](https://img.shields.io/badge/github-repo-blue?logo=github)](https://github.com/batuhansenol/senol-randomizer)
[![PyPI](https://img.shields.io/pypi/v/senol-randomizer?color=orange&label=PyPI)](https://pypi.org/project/senol-randomizer/)

---

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [API Reference](#api-reference)
- [Statistical Test Results](#statistical-test-results)
- [Links](#links)

---

## Overview

`senol-randomizer` is a Python library that wraps `/dev/urandom` entropy with a modular exponentiation layer using large 256-bit prime numbers. The result is a pseudorandom stream that passes all 15 NIST SP 800-22 Rev. 1a statistical tests, while deliberately **not** claiming cryptographic security — the transformation adds complexity at the cost of provable properties.

---

## Installation

```bash
pip install senol-randomizer
```

---

## How It Works

1. **Entropy source:** Reads 256-bit raw values from `/dev/urandom`.
2. **Transformation:** Applies `powmod(a, b, n)` via the `gmpy2` library — performing modular exponentiation for each value of *n*.
3. **Prime moduli:** The set of *n* values consists exclusively of 256-bit prime numbers.
4. **Derived types:** All higher-level data types (`str`, `float`, `bool`, etc.) are derived from this core output.

The design intentionally introduces an asymmetry: the consumer of the output has less information about the internal state than `/dev/urandom` alone would expose, but this property is structural, not mathematically proven.

---

## API Reference

| Function | Description | Arguments | Returns |
|---|---|---|---|
| `RNG()` | Core function. Generates a random large integer with no range constraint. | — | `int` |
| `newint()` | Random integer within a given range. | `min_val: int`, `max_val: int` | `int` |
| `newfloat()` | Random float within a given range. | `min_val: int`, `max_val: int` | `float` |
| `newbool()` | Random boolean. | — | `bool` |
| `newbyte()` | Random bytes of a given length. | `num: int` | `bytes` |
| `newstr()` | Random string sampled from the full Unicode range. | `num: int`, `min_val: int`, `max_val: int` | `str` |
| `newtoken()` | Random URL-safe string. | `length: int` | `str` |
| `choice()` | Selects a random element from a list. | `lst: list` | `any` |
| `shuffle()` | Shuffles a list in-place and returns it. O(n). | `lst: list` | `list` |
| `compress()` | Maps a value into [min, max] while minimizing modulo bias. | `value`, `min_val: int`, `max_val: int` | `int` |

---

## Statistical Test Results

Results from the [NIST SP 800-22 Rev. 1a](https://github.com/dj-on-github/sp800_22_tests) test suite, run against **1 Mibibit (33,554,432 bits)** of `RNG()` output.

| Test | P-Value | Result |
|:---|:---|:---|
| `monobit_test` | 0.046613138703915244 | ✅ PASS |
| `frequency_within_block_test` | 0.6787903492122158 | ✅ PASS |
| `runs_test` | 0.33232036052397196 | ✅ PASS |
| `longest_run_ones_in_a_block_test` | 0.21020703185565603 | ✅ PASS |
| `binary_matrix_rank_test` | 0.2571877713800565 | ✅ PASS |
| `dft_test` | 0.8685773273998374 | ✅ PASS |
| `non_overlapping_template_matching_test` | 0.893926430778068 | ✅ PASS |
| `overlapping_template_matching_test` | 0.7796009868841686 | ✅ PASS |
| `maurers_universal_test` | 0.9802530560443485 | ✅ PASS |
| `linear_complexity_test` | 0.4685290247356243 | ✅ PASS |
| `serial_test` | 0.5630465232357214 | ✅ PASS |
| `approximate_entropy_test` | 0.5631130245829565 | ✅ PASS |
| `cumulative_sums_test` | 0.039939937090386124 | ✅ PASS |
| `random_excursion_test` | 0.5178616373360564 | ✅ PASS |
| `random_excursion_variant_test` | 0.14694060874229203 | ✅ PASS |

**15 / 15 PASS** — Work in progress.

---

## Links

[GitHub Repository](https://github.com/batuhansenol/senol-randomizer) · [PyPI Package](https://pypi.org/project/senol-randomizer/)

[Author on GitHub](https://github.com/batuhansenol) · [Author on PyPI](https://pypi.org/user/Batuhan_Senol/)

---

*— Batuhan Şenol*