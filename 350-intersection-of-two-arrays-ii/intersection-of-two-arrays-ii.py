# Time Complexity: O(n + m)
# Space Complexity: O(min(n, m))
class Solution(object):
    def intersect(self, nums1, nums2):

        freq = {}
        res = []

        for x in nums1:
            freq[x] = freq.get(x, 0) + 1

        for x in nums2:
            if x in freq and freq[x] > 0:
                res.append(x)
                freq[x] -= 1

        return res
        