class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        indexes = []

        while (i < j):
            sum = numbers[i]+numbers[j]

            #if sum is greater than target, 
            #eliminate that option because at a higher i index, it will definitely be greater
            if (sum > target):
                j-=1
                continue;
        
            elif (sum == target):
                indexes.append (i+1)
                indexes.append(j+1)

            #otherwise if the sum is less than the target, then increase i index
            i+=1

            

        return indexes

        