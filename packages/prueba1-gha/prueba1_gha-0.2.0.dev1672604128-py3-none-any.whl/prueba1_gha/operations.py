def sum_(args):
    args = args or []
    total = 0

    if not all(isinstance(x, int) for x in args):
        raise ValueError("Invalid arg: no int")

    for val in args:
        total += val

    return total
