# Time Complexity: O(rowIndex)
# Space Complexity: O(rowIndex)

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]

        for i in range(1, rowIndex + 1):
            row.append(row[-1] * (rowIndex - i + 1) // i)

        return row