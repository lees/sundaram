
import itertools




def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(itertools.islice(iterable, n))


def func(i):
    return 2*(i+1)*(i+2), 2*(i+1)+1


def func_next(struct):
    (current_value, step) = struct
    return current_value + step, step


def next_data():
    data = [func(0)]

    while True:
        res = min(enumerate(data), key=lambda x: x[1][0])
        if res[0] == len(data) - 1:
            data.append(func(res[0] + 1))

        data[res[0]] = func_next(data[res[0]])
        yield res[1][0]


def exclude_repeat(iterable):
    last_el = iterable.next()
    yield last_el
    while True:
        next_el = iterable.next()
        if next_el != last_el:
            yield next_el
            last_el = next_el


def primes_generator():
    yield 1
    yield 2
    ex_generator = exclude_repeat(next_data())
    to_exclude = ex_generator.next()
    to_return = 1
    while True:
        to_return += 1
        if to_return < to_exclude:
            yield 2 * to_return + 1
        else:
            to_exclude = ex_generator.next()


def take(n, iterable):
    return list(itertools.islice(iterable, n))


def xprint(n, iterable):
    for x in xrange(1, n):
        print iterable.next()


def compare(n):
    t1 = take(n, primes_generator())
    t2 = take(n, sundaram.Primes())
    return t1 == t2


def ithprime(n):
    primes = primes_generator()
    for i in xrange(n - 1):
        primes.next()
    return primes.next()


if __name__ == '__main__':
    take(30000, exclude_repeat(next_data()))
