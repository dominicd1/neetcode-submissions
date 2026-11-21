class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #matrix is sorted in increasing order
        #find midpoint of rows
        rows = len(matrix)
        cols = len(matrix[0])
        row_window_size = rows
        row_start = 0
        row_end = rows - 1
        i = 0
        while(row_start <= row_end):
            row_midpoint = (row_start + row_end)//2
            #if target in row
            if (target >= matrix[row_midpoint][0] and target <= matrix[row_midpoint][cols-1]):
                
                for col in range(cols):
                    #print (matrix[row_midpoint][col])
                    if(matrix[row_midpoint][col] == target):
                        return True
                
                return False

            #shrink right side
            elif (target > matrix[row_midpoint][0] and target > matrix [row_midpoint][cols-1]):
                row_start = row_midpoint + 1

            
            #shrink left side
            elif (target < matrix[row_midpoint][0] and target < matrix [row_midpoint][cols-1]):
                row_end = row_midpoint - 1
                
        
            
            #print (matrix[row_start:row_end+1])
            

        return False
        