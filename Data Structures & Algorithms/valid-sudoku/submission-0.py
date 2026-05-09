class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        r = defaultdict(list)
        c = defaultdict(list)
        b = defaultdict(list)
        for in1, i in enumerate(board):
            for in2, j in enumerate(i):
                q1, r1 = divmod(in1, 3)
                q2, r2 = divmod(in2, 3)
                if j != ".":
                    r[in1].append(j)
                    c[in2].append(j)
                    b[q1*3+q2].append(j)
        print(r)
        for i in r:
            if len(r[i]) != len(set(r[i])):
                return False
        for i in c:
            if len(c[i]) != len(set(c[i])):
                return False
        for i in b:
            if len(b[i]) != len(set(b[i])):
                return False
        return True
        