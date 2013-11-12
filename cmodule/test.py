#from example import *
import minpqFast as e


'''
example.insert(0,11)
example.insert(10,101)
example.insert(20,11)
'''



def show():
	for x in xrange(1,e.length()+1):
		print e.show(x)



for x in xrange(30,0,-1):
	e.insert(x,[x]);



#print example.show(1)


for x in xrange(1,31):
	print e.get();


#print hello(who="world!")
