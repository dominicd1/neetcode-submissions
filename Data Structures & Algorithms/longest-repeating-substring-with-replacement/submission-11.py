class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #set up two pointers for start and end of sliding window
        i = 0
        j = 0
        max_char_count = 0
        longest = 0

        #set an empty dictionary to track the frequency of each character
        char_dict = {}

        #set highest frequency character as the first character
        if (len(s) > 0):
            max_char_seen = s[0]
            

        
        while (j < len(s)):
        
        #if character has already been seen, increment the frequency of that letter in the dictionary
            if (s[j] in char_dict):
                char_dict[s[j]] += 1
                
        #if the character frequency is greater than the current max, replace that max character
                if (char_dict[s[j]] > max_char_count):
                    max_char_seen = s[j]
                
        #otherwise, make a new dictionary entry for the new character
            else:
                char_dict[s[j]] = 1

        
        #caluclate the max count by looking up the frequency of it inside the character_dictionary
            max_char_count = char_dict[max_char_seen]


        #if the amount of other characters (that you can replace with k) is greater than k:
        #decrease the window, and update the max_char_count if 
            while(((j - i + 1) - max_char_count) > k):
                char_dict[s[i]] -= 1
                i += 1
            
        #size of the current sliding window
            current = j-i + 1


            if (current > longest):
                longest = current
        
            
            j+= 1
                
            

      
        return longest




