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
        def backtrack(d, idx = 0):
            if idx >= len(word):
                return '#' in d
            if word[idx] in d:
                return backtrack(d[word[idx]], idx + 1)
            elif word[idx] == '.':
                a = False
                for c in d:
                    if c == '#':
                        continue
                    else:
                        if backtrack(d[c], idx + 1):
                            a = True
                            break
                return a
            else:
                return False
        return backtrack(self.d)