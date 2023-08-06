# Copyright 2022 Facundo Batista
# Licensed under the LGPL v2.1 License
# For further info, check https://github.com/facundobatista/tencdec

"""Encode and decode numbers into compressed bytes.

Only the deltas of the numbers are encoded. Deltas are always positive (that's why
source numbers must be monotonic increasing).

If the delta is less than or equal to 127, it's stored directly, otherwise it's
stored in multiple bytes, using seven bits on each byte, with the most significant
one in 1 if more bytes to process.

E.g. for a simple case:

    0000 0100 -> 4 (in decimal)

Multiple bytes:

    1111 0100
    0000 0011

    - first byte indicates that it goes on, second byte indicates that ends there

    - bits are collected without using the most significant one, in reverse order:

        000 0011 111 0100 -> 0000 0001 1111 0100 -> 500 (in decimal)
"""

import array


def encode(numbers):
    """Compress an array of numbers into a bytes object."""
    result = array.array('B')
    add_to_result = result.append

    prev_number = 0
    for number in numbers:
        number, prev_number = number - prev_number, number
        assert number >= 0, "source numbers are not monotonic increasing"
        while True:
            byte = number & 0x7F
            number >>= 7
            if number:
                # the number is not exhausted yet, store these 7b with the flag and continue
                add_to_result(byte | 0x80)
            else:
                # we're done, store the remaining bits
                add_to_result(byte)
                break

    return result.tobytes()


def decode(bytes_array):
    """Decode a compressed array of bytes."""
    result = []
    add_to_result = result.append
    prev_number = 0
    number = 0
    shift = 0

    for byte in bytes_array:
        number |= (byte & 0x7F) << shift
        shift += 7

        if not (byte & 0x80):
            # the sequence ended
            prev_number += number
            add_to_result(prev_number)
            number = 0
            shift = 0

    return result
