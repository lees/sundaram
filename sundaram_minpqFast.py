
import itertools
import minpqFast



def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(itertools.islice(iterable, n))


def func(i):
    return 2*(i+1)*(i+2), 2*(i+1)+1


def func_next(struct):
    (current_value, step) = struct
    return current_value + step, step


def exclude_generator():
    data_tree = minpqFast
    start_value = func(0)
    last_returned = None
    min_border = start_value[0]
    i = 0
    data_tree.insert(start_value[0],(start_value[0], start_value))

    while True:
        (value,iterator) = data_tree.get()
        if value == min_border:
            i += 1
            new_iterator = func(i)
            min_border = new_iterator[0]
            data_tree.insert(new_iterator[0],(new_iterator[0], new_iterator))

        next_value = func_next(iterator)
        data_tree.insert(next_value[0],(next_value[0], next_value))

        if value == last_returned:
            continue
        
        last_returned = value
        yield value

        
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


def ithprime(n):
    primes = primes_generator()
    for i in xrange(n - 1):
        primes.next()
    return primes.next()


if __name__ == '__main__':
    print ithprime(30000)
