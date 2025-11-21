#GF.py
#Defines the Galois Field (GF) multiplication for GF(2^4).
import numpy as np

def gf_multiply(a, b):
    # Galois Field (2^4) multiplication of a and b
    p = 0
    for _ in range(4):
        # if b is 0001, add a to p
        if b & 1:
            p ^= a
        # check if the most significant bit of a is 1
        hi_bit_set = a & 0x8
        a <<= 1
        a &= 0xF
        # if the most significant bit was 1, xor with the irreducible polynomial
        # x^4 + x + 1 or 0x3
        if hi_bit_set:
            a ^= 0x3
        b >>= 1
    return hex(p)[2:]

if __name__ == "__main__":
    print("Galois Field (GF) Multiplication Table:")
    print(np.array([[gf_multiply(a, b) for b in range(2**4)] for a in range(2**4)]))
    