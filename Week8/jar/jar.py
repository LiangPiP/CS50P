class Jar:
    def __init__(self, capacity=12):
        if capacity<=0 or not isinstance(capacity,int):
            raise ValueError
        self._capacity=capacity
        self._size=0


    def __str__(self):
        return ""+"🍪"*self.size

    def deposit(self, n):
        if self.size+n>self.capacity or n<0 or not isinstance(n,int):
            raise ValueError
        else:
            self._size+=n

    def withdraw(self, n):
        if self.size-n<0 or n<0 or not isinstance(n, int):
            raise ValueError
        else:
            self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
