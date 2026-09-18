# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def singleNumber(self, nums):
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones
        