# Time Complexity: O(m * n * 3^L)
# Space Complexity: O(L)

from collections import Counter

class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        board_count = Counter()
        for row in board:
            board_count.update(row)

        word_count = Counter(word)

        for ch in word_count:
            if word_count[ch] > board_count[ch]:
                return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, index):
            if index == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] == word[index + 1]
                ):
                    if dfs(nr, nc, index + 1):
                        board[r][c] = temp
                        return True

            board[r][c] = temp
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False