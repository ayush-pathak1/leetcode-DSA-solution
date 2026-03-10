# Time Complexity: O(n * k)
# Space Complexity: O(n * k)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            key = tuple(count)
            groups[key].append(word)

        return list(groups.values())