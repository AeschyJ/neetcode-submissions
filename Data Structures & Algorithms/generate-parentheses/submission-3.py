class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []
        def travel(s, l, r):
            if l == r and l == n:
                a.append(s)
                return
            if l > r:
                travel(s+")", l, r + 1)
            if l < n:
                travel(s+"(", l + 1, r)
        travel("", 0, 0)
        return a
            