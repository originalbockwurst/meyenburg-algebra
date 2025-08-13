"""
Behavior of bool operations.

This study tests that operation can be reversed
in order to recover a starting value.

An example of a non-boolean reversible operation would be:

    6 = 3 * 2     # 3 * 2 --> 6
    3 = 6 / 2     # 6 / 2 --> 3    The 3 is recovered.

This program will compare a set of boolean operations, and determine
if they can be reversed.
Any that do not match will be marked with '<<<<<'.

"""
import itertools


def dval(v):
    """
        Convert (0,0) and (1,1) to (0,1)
    """
    if v[0] == v[1]:
        v = 0, 1
    return v


def mbool_add(a, b):
    return (a[0]+b[0])%2, (a[1]+b[1])%2


def mbool_sub(a, b):
    return (a[0]-b[0])%2, (a[1]-b[1])%2


def mbool_mul(a, b):
    b = dval(b)
    terms = a[0]|b[0], a[0]|b[1], a[1]|b[0], a[1]|b[1]
    outer = (terms[0] + terms[3])%2
    inner = (terms[1] + terms[2])%2
    return outer, inner


def mbool_div(a, b):
    return mbool_mul(a, b)



if __name__ == "__main__":

    items = {0,1}

    ops = ([mbool_add, mbool_sub, mbool_div, mbool_mul],
           [mbool_sub, mbool_add, mbool_mul, mbool_div])

    symbols = {mbool_add:'+',
               mbool_sub:'-',
               mbool_div:'/',
               mbool_mul:'*'}

    pairs = list(itertools.product(items, items))

    counter = 0
    count_fail = 0
    for op, opi in zip(*ops):
        print(f"{op.__name__} <--> {opi.__name__}")
        for a, b in itertools.product(pairs, pairs):
            c = op(a, b)
            aa = opi(c, b)
            inverse_ok = True
            if a != aa:
                inverse_ok = False
                count_fail += 1
            failed = "" if inverse_ok else "   <<<<<"
            print(f"{a}{symbols[op]}{b} -> {c}")
            print(f"{c}{symbols[opi]}{b} -> {aa}{failed}\n")
            counter += 1
    print(f"{counter - count_fail}/{counter} are reversible.")

