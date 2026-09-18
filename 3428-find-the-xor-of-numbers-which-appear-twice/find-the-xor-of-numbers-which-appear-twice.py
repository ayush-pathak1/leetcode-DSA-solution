# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def duplicateNumbersXOR(self, nums):
        seen = set()
        result = 0

        for num in nums:
            if num in seen:
                result ^= num
            else:
                seen.add(num)

        return result