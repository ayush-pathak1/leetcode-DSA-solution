class Solution(object):
    def isValid(self, s):
        """
        Time Complexity TC O n
        Space Complexity SC O n
        """
        
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0