class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #given an integer array piles, decide your bananas per hour eating rate of k
        #each hour, you may choose a pile of bananas and eat k bananas from that piles
        #find the minimum integer k that you can eat all the bananas within h hours
       
        #at minimum, you need at least len(piles) hours. 

        #add the totals of each pile and find maximum value
        
        total = 0
        max_pile = 0
        for p in piles:
            if (p > max_pile):
                max_pile = p
            total += p
        
        i = 1
        j = max_pile

        print(max_pile)
        print(total)

        prev_hours = max_pile
        valid_k = max_pile

        while (i <= j):
            k = (j-i)//2 + i
            hours = 0
            x = 0
            for p in piles:
                hours += -(-p//k)
            
            difference = hours - h

            print([k,difference])
            
            #cant take longer than the h hours given, so must decrease
            if (difference > 0):
                i = k+1
            else:
                valid_k = k
                j = k-1
            


        return valid_k
