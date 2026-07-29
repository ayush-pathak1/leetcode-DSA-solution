# Time Complexity: O(n * k)
# Space Complexity: O(k)

from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        target = Counter(words)
        ans = []

        for offset in range(word_len):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    seen[word] += 1
                    count += 1

                    while seen[word] > target[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        ans.append(left)
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return ans