class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a = []
        phone_config = {
            "2": ("a", 3), "3": ("d", 3), "4": ("g", 3), "5": ("j", 3),
            "6": ("m", 3), "7": ("p", 4), "8": ("t", 3), "9": ("w", 4)
        }
        def backtrack(arr = [], idx = 0):
            if idx >= len(digits):
                if arr:
                    a.append("".join(arr))
                return
            for n in range(phone_config[digits[idx]][1]):
                arr.append(chr(ord(phone_config[digits[idx]][0]) + n))
                backtrack(arr, idx + 1)
                arr.pop()
        backtrack()
        return a