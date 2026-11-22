class Solution:
    def findMin(self, nums: List[int]) -> int:
        #treat the array the same, but just adjust the indexes.

        #find where the list was rotated, then that position is automatically the minimum.
        i = 0
        j = len(nums)-1

        #compare the endpoints

        

        while (i <= j-2):
            mid = (j-i)//2 + i
            
            if (nums[mid] > nums[j]):
                i = mid 
            elif (nums[mid] < nums[i]):
                j = mid 
            else:
                return nums[0]
            #print(nums[i:j+1])
            
        mini = 1001
        for x in range (i, j+1):
            if nums[x] < mini:
                mini = nums[x]
        
        return mini



        