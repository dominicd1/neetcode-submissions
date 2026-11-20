class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #set two pointers at each end of the list
        i = 0
        j = len(nums)-1

        #while the two pointers are not equal to each other
        while (i != j):

            #find the midpoint between two pointers
            k = (j-i)//2 + i

            #return if element is equal to target
            if (nums[k] == target):
                return k

            #otherwise shrink from the right half if target is less than
            elif (nums[k] > target):
                j -= (j-k) 

            #shrink from left side if target is greater
            elif  (nums[k] < target):
                i = k+1
            
        #if the pointers equal each other, check if they both point to the target (when len(nums) == 1)
        if (nums[i] == target):
            return i
        return -1