class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=0
        for row in matrix:
            if row[0]<target:
                c+=1
            elif row[0]==target:
                return True
            else:
                break
            
        if target in matrix[c-1]:
            return True
        else:
            return False


