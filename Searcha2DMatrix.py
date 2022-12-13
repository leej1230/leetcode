class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = -1
        for ind, row in enumerate(matrix):
            if row[0] <= target and row[-1] >= target:
                targetRow = ind
                break
        
        if targetRow == -1:
            return False
        
        left, right = 0, len(matrix[targetRow])-1
        while left <= right:
            middle = int((right + left)/2)
            if matrix[targetRow][middle] == target:
                return True
            if matrix[targetRow][middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return False
        '''
        Check if each row may contain a target number or not by looking at first and last number

        After picking the row, do a binary search in there
        If the target number exist, return True

        return False
        '''