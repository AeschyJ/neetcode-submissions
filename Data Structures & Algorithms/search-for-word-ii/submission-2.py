class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d = {}
        for word in words:
            curr = d
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = word

        a = []
        directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
        row, col = len(board), len(board[0])
        def travel(r, c, trie):
            char = board[r][c]

            if char not in trie:
                return

            curr = trie[char]

            if '#' in curr:
                a.append(curr['#'])
                del curr['#']
            board[r][c] = '#'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    travel(nr, nc, curr)
            board[r][c] = char

        for r in range(row):
            for c in range(col):
                travel(r, c, d)

        return a