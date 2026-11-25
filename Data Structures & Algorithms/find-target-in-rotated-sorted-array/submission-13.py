class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1

        if nums[j] < nums[i]:
            #while (i <= j-3):
            # [0, 1, 2, 3, 4| 5, 6, 7, 8] 9//2 = 4
            # [3, 4, 5, 6, 7| 8, 9, 1, 2] target = 1
            # [8, 9, 1, 2, 3| 4, 5, 6, 7] target = 1
            range_found = False
            x = 0
            while not range_found:
                # if (x > 6):
                #     return mid
                mid = (j-i)//2 + i
                #you find the target
                if (target == nums[mid]):
                    return mid
                #if the rotation point is on the right side, everything on the left side is in order
                #so that means if the target between nums[i] and nums[mid], you can definitely find it there
                #otherwise, cut down the range from the left side
                elif (nums[mid] > nums[j]):
                    # print("left side")
                    if (target < nums[mid] and nums[i] <= target):
                        j = mid -1
                        range_found = True
                    else:
                        i = mid + 1
                #if the rotation point is on the left side, everything on the right side is in order
                #if the target is between the midpoint number and the end number, its in the sorted range
                elif (nums[mid] < nums[i]):
                    # print("right side")
                    if (nums[mid] < target and target <= nums[j]):
                        i = mid + 1
                        range_found = True
                    else:
                        j = mid-1
                
                else:
                    range_found = True
                    
                # print(nums[mid])
                
                # print (nums[i:j+1])
                # x+= 1


      
           
        
        #typical binary search if thee's no equivalent rotation
        while (i <= j):
            mid = (j-i)//2 + i
            if (target == nums[mid]):
                return mid
            elif (target < nums[mid]):
                j = mid - 1
            elif (target > nums[mid]):
                i = mid+ 1

        if (len(nums) == 1):
            if (target == nums[0]):
                return 0

        return -1


                
            
        