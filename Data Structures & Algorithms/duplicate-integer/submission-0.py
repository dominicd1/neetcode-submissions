class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #iterate through list
        s = set()
        for number in nums:
            if number not in s:
                s.add(number)
            else:
                return True
        return False
    #if number not in already_checked set,
    #then add to set and continue
    #else return false

        