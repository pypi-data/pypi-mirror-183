def make_even_ceil(*args):
    for _n in args:
        n = int(_n)
        if (n % 2) != 0:
            n += 1
        yield n


def make_even_floor(*args):
    for _n in args:
        n = int(_n)
        if (n % 2) != 0:
            n -= 1
        yield n


def make_odd_ceil(*args):
    for _n in args:
        n = int(_n)
        if (n % 2) == 0:
            n += 1
        yield n


def make_odd_floor(*args):
    for _n in args:
        n = int(_n)
        if (n % 2) == 0:
            n -= 1
        yield n


