class Solution:
    def partition(self, s: str) -> List[List[str]]:
        a = []
        temp = []
        def travel(arr = [], idx = 0):
            if idx >= len(s):
                sarr = "".join(arr)
                if sarr != sarr[::-1]:
                    return
                temp.append("".join(arr))
                a.append(temp.copy())
                temp.pop()
                return
            c = s[idx]
            arr.append(c)
            travel(arr, idx + 1)
            arr.pop()
            if arr:
                sarr = "".join(arr)
                if sarr != sarr[::-1]:
                    return
                temp.append("".join(arr))
                travel([c], idx + 1)
                temp.pop()
        travel()
        return a