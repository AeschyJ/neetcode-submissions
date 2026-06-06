class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []
        arr = []
        def travel(s, l, r):
            if l == r and l == n:
                a.append("".join(arr))
                return
            if l > r:
                arr.append(")")
                travel(arr, l, r + 1)
                arr.pop()
            if l < n:
                arr.append("(")
                travel(arr, l + 1, r)
                arr.pop()
        travel("", 0, 0)
        return a
            