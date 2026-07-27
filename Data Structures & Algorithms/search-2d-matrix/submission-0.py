class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        mid = rows // 2
        left = 0
        right = rows - 1

        while left < right:
            print(left, right, mid, target)
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][cols - 1]:
                left = mid + 1
            else:
                break
            mid = left + (right - left) // 2

        left = 0
        right = cols - 1
        mid2 = left + (right - left) // 2
        while left <= right:
            if target < matrix[mid][mid2]:
                right = mid2 - 1
            elif target > matrix[mid][mid2]:
                left = mid2 + 1
            else:
                return True
            mid2 = left + (right - left) // 2
        
        return False

        