import itertools

def take(n, iterable):
    """Return first n items of the iterable as a list"""
    res = []
    for i in range(n):
        res.append(iterable.next())
    return res


def imerge(i1, i2):

    el1 = i1.next()
    el2 = i2.next()

    while True:
        if el1 < el2:
            yield el1
            el1 = i1.next()
        elif el1 > el2:
            yield el2
            el2 = i2.next()
        else:
            el1 = i1.next()


'''
def i_iterator_old(i):
    res = 2*(i+1)*(i+2)
    while True:
        yield res
        res += 2*(i+1) + 1


i_iterator = lambda i: (2*i*(i+1) + (2*i+1) * j for j in itertools.count())

'''
def i_iterator(i):
    return ((2*(i+1)*(i+2) + (2*(i+1)+1) * j) for j in itertools.count())


def func(i):
    return 2*(i+1)*(i+2), 2*(i+1)+1


def func_next(struct):
    (current_value, step) = struct
    return current_value + step, step

#i_iterator = lambda i: (2*(i+1)*(i+1) + (2*i+1) * j for j in itertools.count())

def exclude_generator():
    rez = i_iterator(1)
    i = 2
    last_returned = 0
    while True:
        ichunk = i_iterator(i)
        min_border = 2*(i+1)*(i+2)
        rez = imerge(rez, ichunk)
        while last_returned < min_border:
            last_returned = rez.next()
            yield last_returned
        i += 1


def primes_generator():
    yield 1
    yield 2
    ex_generator = exclude_generator()
    to_exclude = ex_generator.next()
    to_return = 1
    while True:
        to_return += 1
        if to_return<to_exclude:
            yield 2*to_return+1
        else:
            to_exclude = ex_generator.next()


def ithprime(n):
    primes = primes_generator()
    for i in xrange(n-1):
        primes.next()
    return primes.next()


if __name__ == '__main__':
    sun_ex = exclude_generator()
    for i in xrange(1, 40000):
        sun_ex.next()
    print sun_ex.next()

