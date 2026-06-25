class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        import heapq

        #use a dictionary to keep track of the frequency of each value, making sure each one is unique
        frequent_dict = {}

        for num in nums:
            if num in frequent_dict:
                frequent_dict[num] += 1
            else:
                frequent_dict[num] = 1
       
        frequent_nums = []
        frequent_min = 0
        frequent_count = 0
        for num in frequent_dict:
            if frequent_dict[num] > frequent_min:
                heapq.heappush(frequent_nums, (frequent_dict[num], num))
                frequent_count+=1
                if(frequent_count > k):
                    heapq.heappop(frequent_nums)
                    frequent_min = frequent_nums[0][0]
                    frequent_count-=1
        
        frequent = []
        i = 0

        for x in frequent_nums:
            frequent.append(frequent_nums[i][1])
            i+=1

        return frequent