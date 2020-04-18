arr = [7,13,12, 11, 5, 6]
# sort two lists based on one
list1 = np.array([3,2,4,1])
list2 = np.array(["three","two","four","one"])
idx   = np.argsort(list1)

list1 = np.array(list1)[idx]
list2 = np.array(list2)[idx]

# 1 merge sort
# time complexity: worst, average, and best: O(nlog(n)), extra space:O(n)
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = 0
        j = 0
        k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    return arr

# selection sort
# time complexity: O(n^2) all the time, extra space: O(1)
# selection: select the least element in the right side of i and put in i's
# left side, the left side of i is always sorted
def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j]< arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

# Bubble sort
# time complexity: O(n^2), extra space O(1)
def bubbleSort(arr):
    for i in range(len(arr)):
        is_sorted = True
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                is_sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if is_sorted:
            return arr
    return arr

def bubbleSortRecur(arr):
    for i,num in enumerate(arr):
        try:
            if arr[i+1] < arr[i]:
                arr[i] = arr[i+1]
                arr[i+1] = num
                bubbleSortRecur(arr)
        except:
            pass
    return arr

# Insertion sort
# time complexity: O(n^2), extra space: O(1)
# Insert： elements in the left side of i is sorted, we iterate it's right side
# and insert each element in the right side to the correct position in the left
# side
def insertSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        # find where to insert the new element
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
    return arr

def insertionSortRecursive(arr,n):
    # base case
    if n<=1:
        return

    selectionSortRecursive(arr,n-1)

    last = arr[n-1]
    j = n-2

    while (j>=0 and arr[j] > last):
        arr[j+1] = arr[j]
        j=j-1
    arr[j+1] = last
    return arr

# Quick sort
# time complexity: O(nlog(n)), extra space: O(log(n))
def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]# It is like bubble sort
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)

        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
    return arr

quickSort(arr,0,len(arr)-1)
# Heap sort
# time complexity: O(nlogn) all the time, space complexity O(1)
def heapify(arr: List[int], size: int, root: int) -> None:
    largest = root
    l = 2 * root + 1
    r = 2 * root + 2

    if l < size and arr[l] > arr[root]:
        largest = l

    if r < size and arr[r] > arr[largest]:
        largest = r

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, size, largest)

def heapSort(arr: List[int]) -> List[int]:
    size = len(arr)

    # Build a max heap from arr
    for i in range(size-1,-1,-1):
        heapify(arr,size,i)

    # do some sorting
    for i in range(size-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)

    return arr


# Sort a linked list
# this is a classic problem from LeetCode: https://leetcode.com/problems/sort-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)

        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1 is not None:
            cur.next = l1

        if l2 is not None:
            cur.next = l2

        return dummy.next
