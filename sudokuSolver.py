import collections

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        ## create three hash tables and populate it with current bord
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        subSqures = collections.defaultdict(set)       
        for r in range(9):
            if r < 3:
                rId = "A"
            elif r >= 3 and r < 6:
                rId = "B"
            else:
                rId = "C"            
            for c in range(9):               
                if c < 3:
                    cId = "A"
                elif c >= 3 and c < 6:
                    cId = "B"
                else:
                    cId = "C"
                if board[r][c] ==".":
                    continue
                else:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    subSqures[rId+cId].add(board[r][c])
        for r in range(9):
            if r < 3:
                rId = "A"
            elif (r >= 3 and r < 6):
                rId = "B"
            else:
                rId = "C" 
            for c in range(9):
                
                if c < 3:
                    cId = "A"
                elif c >= 3 and c < 6:
                    cId = "B"
                else:
                    cId = "C"
                
                if board[r][c] ==".":
                    # if a location need a value, iterate over 1-9 see if fits
                    for i in range(1,10):
                        if (str(i) in cols[c] or 
                            str(i) in rows[r] or 
                            str(i) in subSqures[ rId+cId]):
                            continue
                        else:
                            board[r][c] = str(i)
                            cols[c].add(str(i))
                            rows[r].add(str(i))
                            subSqures[rId+cId].add(str(i))
                else:
                    continue
        print(board)
        
        
        
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]] 


b= Solution()  
b.solveSudoku(board)