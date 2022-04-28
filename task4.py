#!/usr/bin/env python3
# task 4-1

def inverse_mod(k, p):
    return pow(k, -1, p)


def add(point1, point2, p, a):
    """Returns the result of point1 + point2 with field characteristic p and curve coefficient a 
    / points at infinity representation is None """

    if point1 is None:
        # O + point2 = point2
        return point2
    if point2 is None:
        # point1 + O = point1
        return point1

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 != y2:
        # point1 + (-point1) = 0
        return None

    if x1 == x2:
        # This is the case point1 == point2.
        m = (3 * x1 * x1 + a) * inverse_mod(2 * y1, p)
    else:
        # This is the case point1 != point2.
        m = (y1 - y2) * inverse_mod((x1 - x2), p)

    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % p,
              -y3 % p)

    return result


def scalar_mult(s, point, p, a):
    """Returns s * point using the double-and-add algorithm over finite fields."""
    result = None
    addend = point

    while s:
        if s & 1:  # ‘&’ is a bitwise operator in Python
            # Add.
            result = add(result, addend, p, a)
        # Double.
        addend = add(addend, addend, p, a)
        s >>= 1  # shift right
    return result


# Field characteristic:
p = 5
# Curve coefficient:
a = 2
# Curve coefficient:
b = (-1)
# generatorPoint:
gp = (0, 3)
# skalar factor:
s = 6

print(scalar_mult(s, gp, p, a))

# test with task 3.4:
assert scalar_mult(6, (0, 3), 5, 2) == (0, 2), "logic broken"
