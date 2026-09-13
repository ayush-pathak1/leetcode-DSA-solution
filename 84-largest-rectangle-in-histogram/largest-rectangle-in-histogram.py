# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            curr = heights[i] if i < len(heights) else 0

            while stack and heights[stack[-1]] > curr:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area