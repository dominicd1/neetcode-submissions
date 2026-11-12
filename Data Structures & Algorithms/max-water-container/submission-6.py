class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bars = {}
        i = 0
        j = len(heights)-1
        max_area = 0
        max_height = 0


        while i < j:
            width = j - i
            area = min(heights[i], heights[j]) * width
            if (area > max_area):
                max_area = area
                print ([i, j, area])
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1

        print([i, j])
        return max_area
        
            


