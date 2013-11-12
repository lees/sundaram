

from timer import Timer
import isundaram
#import isundaram2
import sundaram_fast_tree
#import sundaram_tree
import sundaram_minpq
import sundaram_minpq_onc


def take(n, iterable):
    """Return first n items of the iterable as a list"""
    res = []
    for i in range(n):
        res.append(iterable.next())
    return res

def ith(n, iterable):
    for i in xrange(n):
        iterable.next()
    return iterable.next()

def timeiter(iterable):
    Timer.start()
    ith(400000, iterable)
    Timer.end()

#timeiter(isundaram_spoiled.main_generator())
#timeiter(sundaram_spoiled.exclude_repeat(sundaram_spoiled.next_data()))
#timeiter(isundaram.exclude_generator())
#timeiter(isundaram2.exclude_generator())
timeiter(sundaram_fast_tree.exclude_generator())
#timeiter(sundaram_tree.exclude_generator())

#timeiter(sundaram_minpq.exclude_generator())
timeiter(sundaram_minpq_onc.exclude_generator())

