class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        max_profit = 0
        lowest_price = prices[0]
        lowest_index = 0
        highest_price = 0
        highest_index = 100

        #have one pointer iterate through each element, one tracking lowest price
        while (j < len(prices)):

            if (prices[j] <= lowest_price):
                lowest_price = prices[j]
                lowest_index = i
                i = j

            profit = prices[j] - lowest_price

            if (profit > max_profit):
                max_profit = profit
             
            j+= 1
        

        return max_profit


            