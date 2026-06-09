class WordDictionary:

    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        curr = self.d
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#'] = True

    def search(self, word: str) -> bool:
        def backtrack(curr, idx = 0):
            for i in range(idx, len(word)):
                c = word[i]

                if c == '.':
                    for child in curr:
                        if child != '#' and backtrack(curr[child], i + 1):
                            return True
                    return False
                
                if c not in curr:
                    return False
                curr = curr[c]

            return '#' in curr
        return backtrack(self.d)