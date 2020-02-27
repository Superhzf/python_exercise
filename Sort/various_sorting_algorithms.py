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
# time complexity: O(n^2), extra space: O(1)
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
    n = len(arr)
    for i in range(n):
        # after each round, the last element is always the biggest one
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def bubbleSortIter(arr):
    for i,index in enumerate(arr):
        try:
            if arr[i+1] < arr[i]:
                arr[i] = arr[i+1]
                arr[i+1] = num
                bubbleSortIter(list)
        except:
            pass
    return arr

# Insertion sort
# time complexity: O(n^2), extra space: O(1)
def selectionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        # find where to insert the new element
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key

def selectionSortRecursive(arr,n):
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
# time complexity: O(nlog(n)), extra space: O()
