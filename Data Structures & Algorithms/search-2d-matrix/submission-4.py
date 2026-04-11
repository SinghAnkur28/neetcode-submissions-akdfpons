class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        t, b = 0, rows - 1
        while t <= b:
            m = (t + b) // 2
            if matrix[m][0] <= target:
                t = m + 1
            else:
                b = m - 1

        row = b
        if row < 0:
            return False

        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
