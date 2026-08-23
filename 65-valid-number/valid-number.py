# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s)

        if i < n and s[i] in "+-":
            i += 1

        digit = False
        while i < n and s[i].isdigit():
            digit = True
            i += 1

        if i < n and s[i] == ".":
            i += 1
            while i < n and s[i].isdigit():
                digit = True
                i += 1

        if not digit:
            return False

        if i < n and s[i] in "eE":
            i += 1

            if i < n and s[i] in "+-":
                i += 1

            exp_digit = False
            while i < n and s[i].isdigit():
                exp_digit = True
                i += 1

            if not exp_digit:
                return False

        return i == n