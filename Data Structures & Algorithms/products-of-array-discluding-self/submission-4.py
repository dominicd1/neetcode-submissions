class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        numsLength = len(nums)
        output = [0] * numsLength
        beforeProduct = [1] * numsLength;
        afterProduct = [1] * numsLength;
        j = numsLength - 2
        afterProduct[numsLength-1] = nums[numsLength-1]
        beforeProduct[0] = nums[0]

        for i in range(1, numsLength):

            beforeProduct[i] = beforeProduct[i-1] * nums[i]
            
            afterProduct[j] = afterProduct[j+1] * nums[j]
            j -=1
            

        output[0] = afterProduct[1]

        for i in range (1, numsLength-1):
            output[i] = beforeProduct[i-1]* afterProduct[i+1]

        output[numsLength-1] = beforeProduct[numsLength-2]

        return output



