# Time Complexity: O(2^target) approx (exploring many combinations using recursion)
# Space Complexity: O(target) for recursion stack and storing current combination

class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res
        