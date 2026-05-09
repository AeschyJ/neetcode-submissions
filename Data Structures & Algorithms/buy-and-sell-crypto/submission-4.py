class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = None
        s = None
        a = 0
        for i in prices:
            if b is None:
                b = i
                print("first",b)
            elif b > i:
                b = i
                s = None
                print("change", b,s)
            elif s is None:
                s = i
                print("yes S",s)
            elif s < i:
                s = i
                print("new S",s)
            print("here", i, b, s)
            if s:
                t = s - b
                a = t if t > a else a
                print("i",i,"b",b,"s",s,"t",t,"a",a)
        return a
