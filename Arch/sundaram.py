import time
import itertools


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))


def merge(l1, l2):
	len1, len2 = len(l1) , len(l2)
	res = [0]*(len1+len2)
	i1,i2 = 0,0
	for i in xrange(len1+len2):
		if (i1 < len1) and (i2 >= len2 or l1[i1] < l2[i2]):
			res[i] = l1[i1]
			i1 += 1
		else:
			res[i] = l2[i2]
			i2 += 1

	return res

def exclude(frm,what):

	rez = []
	frm_local = frm
	whal_local = what

	while frm_local:
		if len(what)==0:
			rez += frm_local
			break

		if frm_local[0]<what[0]:
			rez += frm_local[:1]
			del frm_local[0]
		elif frm[0]>what[0]:
			del what[0]
		else:
			del frm_local[0]
			del what[0]

	return rez

def exclude_generator():
	rez = []
	i=1
	last_returned=0
	while True:
		chunk_big = []		
		for counter in range(100):
			chunk = [i+j+2*i*j for j in range(1,i+1)]
			chunk_big += chunk
			i += 1
		min_border = chunk[0]
		chunk_big = sorted(chunk_big)
		rez = merge(rez,chunk_big)
		while last_returned<min_border:
			el = rez.pop(0)
			if el == last_returned:
				continue
			yield el
			last_returned = el

def i_iterator(i):
	for j in range(1,i+1):
		yield i+j+2*i*j

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

class Primes(object):
	
	def __init__(self):
		super(Primes, self).__init__()
		self.primes = primes_generator()

	def __iter__(self): return self

	def next(self): return self.primes.next()


if __name__ == '__main__':
	print take(99,Primes())

