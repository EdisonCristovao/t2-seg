from random import randint
import time
from decimal import Decimal


class LaggedFibonacciGenerator:
    def __init__(self, seed = None, j = 3, k = 7, bits = 32):
        self._seed = [0] * k
        if seed is None:
            upper_bound = 0
            lower_bound = 2**(bits-1)
            for i in range(0, bits):
                upper_bound = upper_bound + pow(2, i)
            for i in range(0, k):
                self._seed[i] = randint(lower_bound, upper_bound)
        else:
            self._seed = seed
        self._m = 2**bits
        self._j = j - 1
        self._k = k - 1
        self._bits = bits
        if (len(self._seed) < k):
            print("error, len _seed shoud be, at least, the value of k")

    def next(self):
        _next = (self._seed[self._j] + self._seed[self._k]) % self._m
        if (_next.bit_length() > self._bits):
            diff_bits = (_next.bit_length() - self._bits)
            _next = _next >> diff_bits
        self._seed = self._seed[1:7] + [_next]
        return _next