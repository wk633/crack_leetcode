class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        length = len(matrix[0])
        i, j = 0, len(matrix) * length-1
        while i <= j:
            mid = i + (j-i)/2
            if matrix[mid/length][mid%length] == target:
                return True
            elif matrix[mid/length][mid%length] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False
