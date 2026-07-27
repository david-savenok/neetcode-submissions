class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows - 1

        while left <= right:
            mid = (left + right) // 2
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][cols - 1]:
                left = mid + 1
            else:
                break

        left = 0
        right = cols - 1
        while left <= right:
            mid2 = (left + right) // 2
            if target < matrix[mid][mid2]:
                right = mid2 - 1
            elif target > matrix[mid][mid2]:
                left = mid2 + 1
            else:
                return True 
        
        return False

        