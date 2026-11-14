class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        char_set = set()
        longest = 0
        current = 0
        
        
        while (j < len(s)):         
            if(s[j] not in char_set):
                char_set.add(s[j])
                current += 1
            else:
                while(s[j] in char_set):
                    char_set.remove(s[i])
                    i += 1
                    current -= 1
                char_set.add(s[j])
                current+=1     
            
            if (current > longest):
                longest = current

            j+=1

        return longest