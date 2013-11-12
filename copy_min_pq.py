"""
Implementation for the heapqueue with O(log n) write and get max time 
"""


class MinPQ(object):
    """docstring for MinPQ"""

    def __init__(self):
        super(MinPQ, self).__init__()
        self.data = [None]
        self.len = 0

    def push(self, key, value):
        self.data.append((key, value))
        self.len += 1
        self.swim(self.len)

    def pop(self):
        self.exch(1, self.len)
        to_return = self.data.pop()
        self.len -= 1
        self.sink(1)
        return to_return

    def getkey(self, k):
        return self.data[k][0]

    def less(self,i,j):
        return self.data[i][0]<self.data[j][0]

    def exch(self, i, j):
        self.data[j], self.data[i] = self.data[i], self.data[j]

    def swim(self, k):
        while k > 1 and not self.less(k/2,k):
            self.exch(k / 2, k)
            k /= 2

    def sink(self, k):
        j = 2 * k
        while j <= self.len:
            if j < self.len and not self.less(j, j+1):
                j += 1
            if not self.less(j, k): 
                break
            self.exch(k, j)
            k, j = j, 2 * j


t = MinPQ()

for i in range(10, 0, -1):
    t.push(i, i)

#for i in range(5):
    #t.pop()