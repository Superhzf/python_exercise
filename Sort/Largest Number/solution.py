class Solution:
    def mergeSort(self,arr):
        if len(arr)>1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = 0
            j = 0
            k = 0

            while i < len(L) and j < len(R):
                LR = str(L[i]) + str(R[j])
                RL = str(R[j]) + str(L[i])
                if LR > RL:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1


            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i+=1
                k+=1

            while j < len(R):
                arr[k] = R[j]
                j+=1
                k+=1

        res = ''.join(map(str,arr))
        if set(res) == {'0'}:
            return '0'
        return res



    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return ''.join(map(str,nums))
        return self.mergeSort(nums)

# I solved this problem myself but it took me some time
# just want to write it down
