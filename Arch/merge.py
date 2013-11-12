import numpy
import time
import itertools

def smerge(list1,list2):

	local_list1 = list1
	local_list2 = list2
	rez = []

	while True:
		if not local_list1:
			rez += local_list2
			return rez
		if not local_list2:
			rez += local_list1
			return rez

		el1,el2 = local_list1[0],local_list2[0]
		if el1<el2:
			rez.append(el1)
			del local_list1[0]
		elif el1>el2:
			rez.append(el2)
			del local_list2[0]
		else:
			rez.append(el1)
			del local_list1[0]
			del local_list2[0]


def imerge(i1,i2):

	while True:
		try:
			el1 = i1.next()
		except:
			for el in i2: yield el
			raise StopIteration
		try:
			el2 = i2.next()
		except:
			for el in i1: yield el
			raise StopIteration

		if el1 < el2:
			yield el1
			takefrom = itertools.takewhile(lambda x: x<el2,i1)
			for el in takefrom:
				yield el
			yield el2
		elif el1 > el2:
			yield el2
			takefrom = itertools.takewhile(lambda x: x<el1,i2)
			for el in takefrom:
				yield el
			yield el1
		else:
			yield el1


		

def amerge0(l1, l2,res):
	len1, len2 = len(l1) , len(l2)
	
	i1 = 0
	i2 = 0
	for i in xrange(len1+len2):
		if (i1 < len1) and (i2 >= len2 or l1[i1] < l2[i2]):
			res[i] = l1[i1]
			i1 += 1
		else:
			res[i] = l2[i2]
			i2 += 1

	return res


def amerge1(l1, l2,res):
	len1, len2 = len(l1) , len(l2)
	#res = [0]*(len1+len2)
	i1,i2 = 0,0
	for i in xrange(len1+len2):
		if (i1 < len1) and (i2 >= len2 or l1[i1] < l2[i2]):
			res[i] = l1[i1]
			i1 += 1
		else:
			res[i] = l2[i2]
			i2 += 1

	return res



def test(f,res):
	n = 10**7
	l1=range(n)
	l2=range(0,n,3) 
	tic = time.time()
	res = f(l1,l2,res)
	tac = time.time()
	#assert l1==res
	print f.__name__,"| Elapsed time: {0:.4f} sec".format(tac-tic)


def ttest(n):
	res = []
	for k in xrange(1,n):
		for j in xrange(1,k/2+1):
			i = k-j
			res.append(i+j+2*i*j)
	return res




#test(smerge)
'''
res = numpy.zeros(2*(10**7))
test(amerge0,res)
res = [0]*(2*(10**7))
test(amerge1,res)
'''

n = 10**7
l1=iter(range(n))
l2=iter(range(0,n,3))
tic = time.time()
res = [x for x in imerge(l1,l2)]
tac = time.time()
print "| Elapsed time: {0:.4f} sec".format(tac-tic) 
#print ttest(30)


