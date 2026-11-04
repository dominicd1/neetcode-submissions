class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        i_seen = {}
        j_seen = {}
        for x in range(len(numbers)):
            if (numbers[i] not in i_seen):
                i_seen[numbers[i]] = i
            if (numbers[j] not in j_seen):
                j_seen[numbers[j]] = j

            i_difference = target - numbers[i]
            j_difference = target - numbers[j]

            if (i_difference in j_seen):
                return [i + 1, j_seen[i_difference]+ 1]
    
            if (j_difference in i_seen):
                return [i_seen[j_difference]+ 1,j +1]

            i +=1 
            j-= 1
            


            

        