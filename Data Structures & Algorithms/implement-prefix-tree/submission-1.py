class PrefixTree:

    def __init__(self):
        self.a = []

    def insert(self, word: str) -> None:
        self.a.append(word)

    def search(self, word: str) -> bool:
        for s in self.a:
            if s == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for s in self.a:
            if s.startswith(prefix):
                return True
        return False
        