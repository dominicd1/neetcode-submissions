class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort numbers in ascending order
        nums.sort()
        selected_nums = set()

        triplets = []

        k = 0
        for num in nums:
            if num in selected_nums:
                k+=1
                continue
            target = -num
            i = k+1
            j = len(nums)-1
            selected_inner = set()
            while (i < j):
                sum = nums[i]+nums[j]
                if (sum > target):
                    j-=1
                    continue
                elif (sum == target and nums[i] not in selected_inner):
                    selected_nums.add(num)
                    selected_inner.add(nums[i])
                    triplets.append([num, nums[i], nums[j]])
                i+=1
            k += 1
        
        return triplets