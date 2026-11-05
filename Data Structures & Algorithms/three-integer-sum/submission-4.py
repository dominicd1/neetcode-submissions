class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        
        j = 0
        for x in range(len(nums)):
            
            two_sum_target = -nums[j]
            i = 0
            seen = set()
            for y in range(len(nums)):

                if i == j:
                    i+=1 
                    continue
    
                difference = two_sum_target - nums[i]
                

                if difference in seen:
                    triplet = [nums[i], difference, nums[j]]
                    triplet.sort()
                    triplets.add(tuple(triplet))
                
                elif (nums[i] not in seen and i != j):
                    seen.add(nums[i])

                i+=1
            j+=1




        return list(list(t) for t in triplets)