class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while (i != j):
            k = (j-i)//2 + i
            if (nums[k] == target):
                return k
            elif (nums[k] > target):
                j -= (j-k) 
            elif  (nums[k] < target):
                i = k+1
            print(nums[i:j+1])
            print (k)

        if (nums[i] == target):
            return i
        return -1