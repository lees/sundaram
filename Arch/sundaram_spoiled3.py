
import itertools
import bintrees


def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(itertools.islice(iterable, n))


def func(i):
    return 2*(i+1)*(i+2), 2*(i+1)+1


def func_next(struct):
    (current_value, step) = struct
    return current_value + step, step


def smart_insert(tree, value):
    while value[0] in tree:
        value = func_next(value)
    tree.insert(value[0], value)


def exclude_generator():
    data_tree = bintrees.FastRBTree()
    start_value = func(0)
    min_border = start_value[0]
    i = 0
    smart_insert(data_tree, start_value)

    while True:
        res = data_tree.pop_min()
        if res[0] == min_border:
            i += 1
            new_value = func(i)
            min_border = new_value[0]
            smart_insert(data_tree, new_value)

        smart_insert(data_tree, func_next(res[1]))
        yield res[0]


def primes_generator():
    yield 2
    yield 3
    ex_generator = exclude_generator()
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


def ithprime(n):
    primes = primes_generator()
    for i in xrange(n - 1):
        primes.next()
    return primes.next()


if __name__ == '__main__':
    sun_ex = exclude_generator()
    for i in xrange(1, 400000):
        sun_ex.next()
    print sun_ex.next()
