#!/usr/bin/python3


def convert_roman(ch):
    """
    converts a roman numeral character into the respective integer
    """
    romint = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return romint.get(ch, -1)


def roman_to_int(roman_string):
    """
    converts any string of roman numerals to decimal
    """
    cur_max = -1
    cur = conv = 0
    holder = []

    if roman_string is None or not isinstance(roman_string, str):
        return 0
    for c in roman_string:
        cur = convert_roman(c)
        if cur == -1:
            return 0
        if len(holder) == 0:
            if cur == cur_max or cur_max == -1:
                cur_max = cur
                conv += cur
            elif cur < cur_max:
                holder.append(cur)
            elif cur > cur_max:  # only happens if smaller is starting number
                # for example: IIX, VXC
                cur_max = cur
                cur -= conv
                conv = cur
        else:
            if cur > holder[-1]:
                cur_max = cur
                cur -= sum(holder)
                conv += cur
                holder.clear()
            else:
                holder.append(cur)

    if len(holder) != 0:
        conv += sum(holder)
    return conv
