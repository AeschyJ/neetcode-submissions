class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a = []
        phone = {
            "2": "abc", "3": "def",  "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        arr = []
        max_len = len(digits)
        def backtrack(idx):
            if idx >= max_len:
                if arr:
                    a.append("".join(arr))
                return
            for n in phone[digits[idx]]:
                arr.append(n)
                backtrack(idx + 1)
                arr.pop()
        backtrack(0)
        return a