# Time Complexity: O(n + m)
# Space Complexity: O(n)
class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        res = set()         

        for x in nums2:
            if x in s1:
                res.add(x)

        return list(res)
        