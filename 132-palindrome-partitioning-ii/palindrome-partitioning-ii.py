# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution(object):
    def minCut(self, s):
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True

        dp = [0] * n

        for i in range(n):
            if palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(1, i + 1):
                    if palindrome[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1]
        