class RLEIterator(object):

    def __init__(self, A):
        self.A = A
        self.index = 0 # which element
        self.quantity = 0 # how many current element has been exhausted

    def next(self, n):
        while self.index < len(self.A):
            if  n > self.A[self.index] - self.quantity:
                n = n - (self.A[self.index] - self.quantity)
                self.quantity = 0
                self.index += 2
            else:
                self.quantity += n
                return self.A[self.index+1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
