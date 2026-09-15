# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result