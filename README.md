# A Simple Cython Example

A Cython Example based on [The Performance of Python, Cython and C on a Vector](https://notes-on-cython.readthedocs.io/en/latest/std_dev.html). Added `setup.py` and `performance.sh` for simplicity.

Requirement:

```bash
sudo apt-get install python-dev python3-dev
pip install Cython
```

## Usage

Build with native

```bash
python setup.py build_ext --inplace
```

Run this example. Actually, you can check details in `performance.sh`.

```bash
bash performance.sh
```

Output of `performance.sh`

```bash
################################
# Pure Python
10 loops, best of 3: 88.8 msec per loop
# Python Numpy
1000 loops, best of 3: 1.78 msec per loop
# Cython - naive
100 loops, best of 3: 3.38 msec per loop
# Optimised Cython
100 loops, best of 3: 2.38 msec per loop
# Cython calling C
100 loops, best of 3: 2.38 msec per loop
################################       
```
