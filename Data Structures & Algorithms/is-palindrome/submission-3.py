class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(c for c in s.lower() if c.isalpha() or 0<=ord(c)-ord('0')<=9)
        if a == a[::-1]:
            return True
        return False
        