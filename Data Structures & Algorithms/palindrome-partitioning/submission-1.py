class Solution:
    def partition(self, s: str) -> List[List[str]]:
        a = []
        temp = []
        def travel(arr = [], idx = 0):
            if idx >= len(s):
                temp.append("".join(arr))
                for i in temp:
                    if len(i) == 1:
                        pass
                    elif len(i) > 1 and i == i[::-1]:
                        pass
                    else:
                        temp.pop()
                        return
                a.append(temp.copy())
                temp.pop()
                return
            c = s[idx]
            arr.append(c)
            travel(arr, idx + 1)
            arr.pop()
            temp.append("".join(arr))
            travel([c], idx + 1)
            temp.pop()
        travel()
        return a