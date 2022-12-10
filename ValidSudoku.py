class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check for each 3X3 Block
        for i in range(3):
            for j in range(3):
                checkDuplicate = set()
                for k in range(3):
                    for l in range(3):
                        if board[3*i+k][3*j+l] != ".":
                            if board[3*i+k][3*j+l] not in checkDuplicate:
                                checkDuplicate.add(board[3*i+k][3*j+l])
                            else:
                                return False
        
        #Check for each row
        for i in range(9):
            checkDuplicate = set()
            for n in board[i]:
                if n != ".":
                    if n not in checkDuplicate:
                        checkDuplicate.add(n)
                    else:
                        return False
        
        #Check for each column
        for i in range(9):
            checkDuplicate = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] not in checkDuplicate:
                        checkDuplicate.add(board[j][i])
                    else:
                        return False
        
        #Check for Diagonal 1
        for i in range(9):
            checkDuplicate1 = set()
            checkDuplicate2 = set()
            if board[i][i] != ".":
                if board[i][i] not in checkDuplicate1:
                        checkDuplicate1.add(board[i][i])
                else:
                    return False
            if board[8-i][i] != ".":
                if board[8-i][i] not in checkDuplicate2:
                        checkDuplicate2.add(board[8-i][i])
                else:
                    return False

        return True
        '''
        Types of checks you have to done:
            Each block
            Each row
            Each column
            2 Diagonal
        
        Each Block
            for i in range(3)
                for j in range(3)
                    initialize hashmap
                    for k in range(3)
                        for j in range(3)
                            if the board is not "."
                                if the number already exist in hashmap return false
                                else add number to hashmap
        
        Each row
            for i in range(9):
                initialize hashmap
                for n in board[i]
                    if the board is not "."
                        if the number is in hashmap return false
                        else add number
        
        Each column
            for i in range(9):
                initialize hashmap
                for j in range(9)
                    if the board is not "."
                        if the number is in hashmap return false
                        else add number
        
        Diagonal 1
            for i in range(9)
                inirialize hashmap
                if the board is not "."
                    if the number is in hashmap return false
                    else add number
        
        Diagonal 2
            for i in range(9)
                    inirialize hashmap
                    if the board is not "."
                        if the number is in hashmap return false
                        else add number
        '''