class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort numbers in ascending order for efficient two pointer search
        nums.sort()

        #track first numbers in outer loop that have already been scanned
        selected_nums = set()

        #build list to store trips
        triplets = []

        k = 0
        for num in nums:

            #skip numbers that have already been selected as a triplet, because the inner two sum will find 
            #all triplets with this num index
            
            if num in selected_nums:
                k+=1
                continue
            target = -num

            #start inner loop list at one index past current num and go until the end
            i = k+1
            j = len(nums)-1

            #track inner loop repeats, avoiding the dupes in the inner loop
            selected_inner = set()

            #inner two sum loop finds all triplets with num
            while (i < j):
                sum = nums[i]+nums[j]
                if (sum > target):
                    j-=1
                    continue
                
                #make sure that the inner loop two sum hasnt already been selected
                # if num[i] has been selected, its gonna be the same num[j] too
                elif (sum == target and nums[i] not in selected_inner):
                    selected_nums.add(num)
                    selected_inner.add(nums[i])
                    triplets.append([num, nums[i], nums[j]])
                i+=1
            k += 1
        
        return triplets