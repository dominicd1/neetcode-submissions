class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        i = 0
        j = 0

        orig = dict()
        new = dict()

        for s in s1:
            if (s in orig):
                orig[s] += 1
            else:
                orig[s] = 1
        
        print(orig)
        
        while (j < len(s2)):
            if(s2[j] in new):
                new[s2[j]] += 1
            else:
                new[s2[j]] = 1
            
            while(j-i+1 > len(s1)):
                new[s2[i]] -= 1
                if (new[s2[i]]) == 0:
                    del new[s2[i]]
                i += 1
            
            if new == orig:
                return True

            # print(s2[i:j+1])
            # print (new)

            j+=1 

           


        return False

        