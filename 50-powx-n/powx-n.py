# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def myPow(self, x, n):
        power = abs(n)
        result = 1
        
        while power > 0:
            
            if power % 2 == 1:
                result = result * x
            
            x = x * x
            power = power // 2
        
        if n < 0:
            result = 1 / result
            
        return result