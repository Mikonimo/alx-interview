#!/usr/bin/python3
"""This module contains a function for utf8 validation"""


def validUTF8(data):
    # Number of bytes remaining in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Mask to get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & 0x80) == 0:  # 1-byte character (0xxxxxxx)
                continue
            elif (byte & 0xE0) == 0xC0:  # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte & 0xF0) == 0xE0:  # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte & 0xF8) == 0xF0:  # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                return False
        else:
            # Check that the byte is a valid continuation byte (10xxxxxx)
            if (byte & 0xC0) != 0x80:
                return False
            num_bytes -= 1

    # If num_bytes is not 0, then we have an incomplete character
    return num_bytes == 0
