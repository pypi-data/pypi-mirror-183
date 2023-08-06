# What is tencdec

A number array to/from bytes high performance encoder/decoder.

It gets a list of monotonic increasing integers and can encode it to a byte object very fast in a compressed form using deltas.

Then you may store that byte object in a DB or whatever, and when you need the list of integers back, you just decode it.

Example:

```
>>> numbers = [0, 1, 2, 3, 4, 28, 87, 87, 500, 501, 507, 2313]
>>> enc = tencdec.encode(numbers)
>>> enc
b'\x00\x01\x01\x01\x01\x18;\x00\x9d\x03\x01\x06\x8e\x0e'
>>> dec = tencdec.decode(enc)
>>> numbers == dec
True
```

And it's very fast! 

Using the numbers from the example above, `timeit` shows around 2 microseconds to encode or decode (in a AMD Ryzen 7 PRO 4750U CPU):

```
$ python3 -m timeit -s "import tencdec; numbers = [0, 1, 2, 3, 4, 28, 87, 87, 500, 501, 507, 2313]" "tencdec.encode(numbers)"
100000 loops, best of 5: 2.28 usec per loop
$ python3 -m timeit -s "import tencdec; e = tencdec.encode([0, 1, 2, 3, 4, 28, 87, 87, 500, 501, 507, 2313])" "tencdec.decode(e)"
100000 loops, best of 5: 2.42 usec per loop
```

The restriction are that numbers need to be integers (else encoding will crash with `TypeError`) and monotonic increasing positive (this is verified, otherwise it gets into an infinite loop, but with an `assert` so you may disable the verification running Python with `-O` if you are already sure that list of numbers is ok).

Note that there are no external dependencies for this. It's just Python 3 and its standard library.


## How it works

It encodes a delta of the numbers. Deltas must always positive (that's why source numbers must be monotonic increasing).

If the delta is less than or equal to 127, it's stored directly, otherwise it's stored in multiple bytes, using seven bits on each byte, with the most significant one in 1 if more bytes to process.

E.g. for a simple case:

```
0000 0100 -> 4 (in decimal)
```

Multiple bytes:

```
    1111 0100
    0000 0011
```
- first byte indicates that it goes on, second byte indicates that ends there

- bits are collected without using the most significant one, in reverse order:

    ```
    000 0011 111 0100 -> 0000 0001 1111 0100 -> 500 (in decimal)
    ```
