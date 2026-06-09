class PrefixTree:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        curr = self.d
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['.'] = True

    def search(self, word: str) -> bool:
        curr = self.d
        for c in word:
            if c in curr:
                curr = curr[c]
            else:
                return False
        return '.' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.d
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True
        