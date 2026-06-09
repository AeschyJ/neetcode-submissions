class PrefixTree:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        def backtrack(d: dict, idx = 0):
            if idx >= len(word):
                d['.'] = {}
                return
            if word[idx] not in d:
                d[word[idx]] = {}
            backtrack(d[word[idx]], idx + 1)
        backtrack(self.d)

    def search(self, word: str) -> bool:
        def backtrack1(d, idx = 0):
            if idx >= len(word):
                if '.' in d:
                    return True
                else:
                    return False
            if word[idx] in d:
                return backtrack1(d[word[idx]], idx + 1)
            else:
                return False
        return backtrack1(self.d)

    def startsWith(self, prefix: str) -> bool:
        def backtrack2(d, idx = 0):
            if idx >= len(prefix):
                return True
            if prefix[idx] in d:
                return backtrack2(d[prefix[idx]], idx + 1)
            else:
                return False
        return backtrack2(self.d)
        