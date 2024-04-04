#!/usr/bin/python3
'''refer to readme'''


def validUTF8(data):
    '''validate utf-8 encoding'''
    '''
    n_bytes = 0

    for byte in data:
        if n_bytes == 0:
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
    '''

    n_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1

    if n_bytes == 0:
        return True

    return False
