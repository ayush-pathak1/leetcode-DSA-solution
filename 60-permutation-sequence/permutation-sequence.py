class Solution(object):
    def getPermutation(self, n, k):
        """
        Time Complexity TC O n2
        Space Complexity SC O n
        """
        
        numbers = list(range(1, n + 1))
        k -= 1
        fact = 1
        for i in range(1, n):
            fact *= i
        
        result = ""
        
        while n > 0:
            index = k // fact
            result += str(numbers[index])
            numbers.pop(index)
            
            k %= fact
            n -= 1
            
            if n > 0:
                fact //= n
        
        return result