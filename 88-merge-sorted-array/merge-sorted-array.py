class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Time Complexity (TC): O(m + n)
        - We traverse both arrays once.

        Space Complexity (SC): O(1)
        - No extra space used (in-place merge).
        """
        
        i = m - 1  # Last element in nums1 (valid part)
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last position in nums1
        
        # Merge from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If nums2 still has elements left
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        