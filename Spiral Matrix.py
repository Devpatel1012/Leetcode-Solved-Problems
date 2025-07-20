class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        result = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while top < bottom and left < right:
            # Traverse from Left to Right
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # Traverse from Top to Bottom
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not (top < bottom and left < right):
                break

            # Traverse from Right to Left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse from Bottom to Top
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result
