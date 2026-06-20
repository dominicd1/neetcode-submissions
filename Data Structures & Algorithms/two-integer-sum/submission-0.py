class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = []
        numbers_dict = {}
        index = 0
        for num in nums:
            missing_num = target - num
            if missing_num in numbers_dict:
                sums.append(numbers_dict[missing_num])
                sums.append(index)
            
            else:
                numbers_dict[num] = index
                
            index+=1
        return sums