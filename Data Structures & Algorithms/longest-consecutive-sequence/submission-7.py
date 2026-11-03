class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = {}
        seen = set()
        for num in nums:
            if (num-1 not in seen):
                sequences[num] = {num}
            
            if (num-1 in seen and num+1 in seen):

                top_len = len(sequences[num+1])
                bottom_len = len(sequences[num-1])

                sequences[num-1].update(sequences[num+1])
                sequences[num+1] = sequences[num-1]
                sequences[num] = sequences[num-1]
                sequences[num].add(num)

                sequences[num+top_len] = sequences[num]
                sequences[num-bottom_len] = sequences[num]
        
            elif (num-1 in seen):
                sequences[num-1].add(num)
                sequences[num] = sequences[num-1]
            
            elif (num+1 in seen):
                sequences[num+1].add(num)
                sequences[num] = sequences[num+1]

            seen.add(num)
            
            
            
        
        return max((len(s) for s in sequences.values()), default=0)