""" Time Complexity (TC): O(n * m)
    Space Complexity (SC): O(1)
    No extra space used (constant space) """

class Solution(object):
    def strStr(self, haystack, needle): 
        n = len(haystack)
        m = len(needle)
        
        if m == 0:
            return 0
        
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        
        return -1