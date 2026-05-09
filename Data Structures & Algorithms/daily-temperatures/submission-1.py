class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = list(enumerate(temperatures))
        t = sorted(i, key = lambda x : x[1])
        a = []
        for in1, i in enumerate(temperatures):
            if in1 == len(temperatures) - 1:
                a.append(0)
            else:
                tt = [z for z in t if z[0] > in1 and z[1] > i]
                x = min(tt, default=None)
                if x:
                    a.append(x[0]-in1)
                else: a.append(0)
        return a

