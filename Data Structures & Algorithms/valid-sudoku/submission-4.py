class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        i = 0
        j = 0
        for row in board:
            row_set = set()
            for col in row:
                if (board[i][j].isdigit()):

                    number = int(board[i][j])
                    box = (i//3 * 3) + j//3

                    if (0 < number and number < 10):
                        if(number not in row_set):
                            row_set.add(number)
                        else:
                            print ("row:" + str(i) + " col:" + str(j))
                            return False
                        if(number not in cols[j]):
                            cols[j].add(number)
                        else:
                            print ("row:" + str(i) + " col:" + str(j))
                            return False
                        if(number not in boxes[box]):
                            boxes[box].add(number)
                        else:
                            print ("row:" + str(i) + " col:" + str(j))
                            return False
                        
                    else:
                        print ("row:" + str(i) + " col:" + str(j))
                        return False

                j+=1
            i += 1
            j = 0

        return True
                
        