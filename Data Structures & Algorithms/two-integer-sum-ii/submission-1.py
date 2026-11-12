class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        indexes = []
        while (i < j):
            sum = numbers[i]+numbers[j]
            if (sum > target):
                j-=1
                continue;
            elif (sum == target):
                indexes.append (i+1)
                indexes.append(j+1)
            i+=1

            

        return indexes

        