class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        def travel(n):
            if n == 1:
                return ["()"]
            else:
                r = []
                for i in range(n-1):
                    x = travel(i+1)
                    y = travel(n-i-1)
                    for a in x:
                        for b in y:
                            r.append(a+b)
                for a in travel(n-1):
                    r.append("(" + a + ")")
            return r
        for i in travel(n):
            ans.add(i)
        return list(ans)