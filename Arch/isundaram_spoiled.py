
def take(n, iterable):
    """Return first n items of the iterable as a list"""
    res = []
    for i in range(n):
        res.append(iterable.next())
    return res

def row0():
    res = 4
    while True:
        yield res, True
        res += 3


def row(i):
    res = 2*(i+1)*(i+2)
    while True:
        yield res
        res += 2*(i+1) + 1


def merger(rows, row):
    el1 = rows.next()
    el2 = row.next()
    last = 0
    while True:
        if el1[0] <= el2:
            if el1[0] > last:
                yield el1[0], False
                last = el1[0]
            el1 = rows.next()
        else:
            if el2 > last:
                yield el2, True
                last = el2
            el2 = row.next()


def main_generator():
    rows = row0()
    rows = merger(rows, row(1))
    counter = 2
    while True:
        (num, flag) = rows.next()
        if flag:
            rows = merger(rows, row(counter))
            counter += 1
        yield num


if __name__ == '__main__':
    print take(100,main_generator())

