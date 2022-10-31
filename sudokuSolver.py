

class Solution(object):
    def solveSudoku(self, board, r=0, c=0):
    
        if r==9:
            return True
        elif c == 9:
            return self.solveSudoku(board,r+1,0)
        elif str(board[r][c])!= ".":
            return self.solveSudoku(board,r,c+1)
        else:
            for k in range(1,10):
                if self.isValid(board,r,c,k):
                    print("hello")
                    board[r][c]= str(k)
                    print(board)
                    if self.solveSudoku(board, r,c+1):
                        return True
                    board[r][c] = "." 
            return False
        
       
        
                
    def isValid(self,board,r,c,k):
        not_in_row = str(k) not in board[r]
        
        not_in_col = True
        
        for i in range(9):
            if str(k) == board[i][c]:
                not_in_col = False
                break
            
        
        
        not_in_subSq = True
        sqr_start = r - (r%3)
        sqc_start =c - (c%3)
       
        
        for i in range(sqr_start,sqr_start+3):
            for j in range(sqc_start,sqc_start+3):
                if board[i][j] == str(k):
                    not_in_subSq = False
                    break      
            
        return not_in_col and not_in_row and not_in_subSq
         
        
        
        
  
        
        
        
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]] 


b= Solution()  
b.solveSudoku(board)