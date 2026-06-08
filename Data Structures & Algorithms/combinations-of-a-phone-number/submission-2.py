class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a = []
        def backtrack(arr = [], idx = 0):
            if idx >= len(digits):
                if arr:
                    a.append("".join(arr))
                return
            n = int(digits[idx])
            length = 4 if n in (7, 9) else 3
            offset = ord('a') + 3 * (n - 2)
            if n > 7:
                offset += 1
            for i in range(length):
                arr.append(chr(offset + i))
                backtrack(arr, idx + 1)
                arr.pop()
        backtrack()
        return a