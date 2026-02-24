class Solution(object):
    def generate(self, numRows):
        """
        Time Complexity (TC): O(n^2)
         We build n rows.
         Each row can have up to n elements

        Space Complexity (SC): O(n^2)
         We store the entire triangle
        """
        
        result = []
        
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            result.append(row)
        
        return result