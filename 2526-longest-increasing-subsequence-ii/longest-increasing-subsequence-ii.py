# TC: O(n log M)
# SC: O(M)
class Solution(object):
    def lengthOfLIS(self, nums, k):
        if not nums:
            return 0
        
        max_val = max(nums)
        tree = [0] * (4 * max_val + 1)

        def update(v, tl, tr, pos, new_val):
            if tl == tr:
                tree[v] = max(tree[v], new_val)
            else:
                tm = (tl + tr) // 2
                if pos <= tm:
                    update(2 * v, tl, tm, pos, new_val)
                else:
                    update(2 * v + 1, tm + 1, tr, pos, new_val)
                tree[v] = max(tree[2 * v], tree[2 * v + 1])

        def query(v, tl, tr, l, r):
            if l > r:
                return 0
            if l == tl and r == tr:
                return tree[v]
            tm = (tl + tr) // 2
            return max(query(2 * v, tl, tm, l, min(r, tm)),
                       query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r))

        max_len = 0
        for num in nums:
            current_max = query(1, 1, max_val, max(1, num - k), num - 1)
            update(1, 1, max_val, num, current_max + 1)
            max_len = max(max_len, current_max + 1)

        return max_len