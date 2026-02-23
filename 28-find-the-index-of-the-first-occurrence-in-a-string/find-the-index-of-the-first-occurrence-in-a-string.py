class Solution(object):
    def strStr(self, haystack, needle):
        """
        Time Complexity (TC): O(n * m)
         n = length of haystack
         m = length of needle
         In worst case, we compare m characters at each position in haystack

        Space Complexity (SC): O(1)
         No extra space used (constant space).
        """
        
        n = len(haystack)
        m = len(needle)
        
        # Edge case: if needle is empty
        if m == 0:
            return 0
        
        # Check every possible starting index
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        
        return -1