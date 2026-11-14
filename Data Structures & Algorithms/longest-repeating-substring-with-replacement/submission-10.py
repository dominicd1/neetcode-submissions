class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        max_char_count = 0
        longest = 0

        char_dict = {}

        if (len(s) > 0):
            max_char_seen = s[0]
            

        while (j < len(s)):
            if (s[j] in char_dict):
                char_dict[s[j]] += 1
                
                if (char_dict[s[j]] > max_char_count):
                    max_char_seen = s[j]
                
                    
            else:
                char_dict[s[j]] = 1
            
            max_char_count = char_dict[max_char_seen]

            while(((j - i + 1) - max_char_count) > k):
                char_dict[s[i]] -= 1
                if (s[i] == max_char_count):
                    max_char_count -= 1
                i += 1
            
            
            current = j-i + 1


            if (current > longest):
                longest = current
            
            # print (s[i:j+1])
            # print (char_dict)
            # print ("max_char: " + max_char_seen)
            # print("max_count: " +str(max_char_count))
            
            j+= 1
                
            

      
        return longest




