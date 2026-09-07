# Time Complexity: O(Catalan(n))
# Space Complexity: O(n) (excluding output)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        path = []

        def backtrack(open_count, close_count):
            if len(path) == 2 * n:
                ans.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop()

            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return ans