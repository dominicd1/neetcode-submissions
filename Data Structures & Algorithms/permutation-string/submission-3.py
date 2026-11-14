class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        i = 0
        j = 0

        orig = dict()
        new = dict()

        #create a frequency map for the original string, getting the exact counts of each value
        for s in s1:
            if (s in orig):
                orig[s] += 1
            else:
                orig[s] = 1
        
        
        while (j < len(s2)):

        #create a frequency map for everything currently in the sliding window
            if(s2[j] in new):
                new[s2[j]] += 1
            else:
                new[s2[j]] = 1
            
        #shrink the left side of the window to match the size of the original string
            while(j-i+1 > len(s1)):
                new[s2[i]] -= 1
                if (new[s2[i]]) == 0:
                    del new[s2[i]]
                i += 1
        
        #check if the frequencies of each letter in the current window match the original map
            if new == orig:
                return True

            j+=1 

           
        #if no matches were found, return false

        return False

        