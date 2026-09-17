# Time Complexity: O(n * 2^n)
# Space Complexity: O(n^2)

class Solution(object):
    def partition(self, s):
        n = len(s)
        result = []
        path = []

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        def backtrack(start):
            if start == n:
                result.append(path[:])
                return

            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result