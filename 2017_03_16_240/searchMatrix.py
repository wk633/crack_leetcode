class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j = -1
        for row in matrix:
            if len(row) == 0:
                continue
            length = len(row)
            while (length + j) and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False
