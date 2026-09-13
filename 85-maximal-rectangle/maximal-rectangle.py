# Time Complexity: O(rows * cols)
# Space Complexity: O(cols)

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            for i in range(cols + 1):
                curr = heights[i] if i < cols else 0

                while stack and heights[stack[-1]] > curr:
                    h = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    max_area = max(max_area, h * width)

                stack.append(i)

        return max_area