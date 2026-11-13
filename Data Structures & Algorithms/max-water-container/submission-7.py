class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bars = {}
        i = 0
        j = len(heights)-1
        max_area = 0
        max_height = 0


        while i < j:
            width = j - i

            #area is only as big as your shortest wall
            area = min(heights[i], heights[j]) * width

            #replace max area if found new max
            if (area > max_area):
                max_area = area
                print ([i, j, area])

            #increment pointer of the shortest wall
            #remember, area is only as big as the shortest wall, so you have already seen the best combination
            #with the shortest wall, and width will only decrease as you move in
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1

        print([i, j])
        return max_area
        
            


