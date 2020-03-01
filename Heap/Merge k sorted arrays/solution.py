import sys
from typing import List
Matrix = List[List[int]]

class MinHeapNode:
    def __init__(self,el,i,j):
        self.element = el # the element to be sorted
        self.i = i # index of array from which element is taken
        self.j = j # index of next element to be picked from array

class MinHeap:
    def __init__(self,ar: List[MinHeapNode],size: int):
        self.heap_size = size
        self.heap_arr = ar
        i = (self.heap_size-1)//2
        while i>=0:
            self.min_heapify(i)
            i-=1

    def min_heapify(self,i):
        """
        A recursive method to heapify a subtree with the root at given index.
        This method assumes that the subtree are already heapified
        """
        l = 2*i+1
        r = 2*i+2
        smallest = i
        if l < self.heap_size and self.heap_arr[l].element<self.heap_arr[i].element:
            smallest = l

        if r < self.heap_size and self.heap_arr[r].element<self.heap_arr[smallest].element:
            smallest = r

        if smallest!=i:
            self.heap_arr[i],self.heap_arr[smallest] = self.heap_arr[smallest],self.heap_arr[i]
            self.min_heapify(smallest)

    def get_min(self):
        if self.heap_size <= 0:
            print ('Heap underflow')
            return None
        return self.heap_arr[0]

    def replace_min(self,root):
        self.heap_arr[0] = root
        self.min_heapify(0)

def mergeKSortedArrays(arr:Matrix,k:int):
    h_arr = []
    result_size = 0
    for i in range(len(arr)):
        node = MinHeapNode(arr[i][0],i,1)
        h_arr.append(node)
        result_size +=len(arr[i])

    min_heap = MinHeap(h_arr,k)
    result = [0] * result_size
    for i in range(result_size):
        root = min_heap.get_min()
        result[i] = root.element
        if root.j < len(arr[root.i]):
            root.element = arr[root.i][root.j]
            root.j += 1
        else:
            root.element = sys.maxsize
        min_heap.replace_min(root)

    return result
