class Solution(object):
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def myAtoi(self, s):
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        res = 0
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
            if res * sign > 2147483647:
                return 2147483647
            if res * sign < -2147483648:
                return -2147483648
                
        return res * sign