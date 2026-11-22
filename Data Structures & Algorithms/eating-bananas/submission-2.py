class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        #at minimum, you need at least len(piles) hours. 

        #add the totals of each pile and find maximum value
        
    
        max_pile = 0
        for p in piles:
            if (p > max_pile):
                max_pile = p
        
        i = 1
        j = max_pile

        prev_hours = max_pile
        valid_k = max_pile

        #binary search to optimize for the lowest k
        while (i <= j):
            k = (j-i)//2 + i
            hours = 0
            x = 0

            #iterate through each pile and add up time to eat each pile
            for p in piles:
                #use ceiling function (pile total / eating rate)
                hours += -(-p//k)
            
            difference = hours - h

            #print([k,difference])
            
            #cant take longer than the h hours given, so must increase k to eat more
            if (difference > 0):
                i = k+1
            #otherwise, if you're within the given hours, try to decrease k to find the lowest k
            else:
                #update the k value is a valid k value, to save just in case the next k is invalid
                valid_k = k
                j = k-1
            


        return valid_k
