class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True
        d = defaultdict(list)
        for i in range(n-1):
                d[edges[i][1]].append(edges[i][0])
                d[edges[i][0]].append(edges[i][1])
        visit = set()
        def tree(node):
            visit.add(node)
            if len(visit) > n:
                return False
            a = True
            for leaf in d[node]:
                if leaf in visit: continue
                a = a and tree(leaf)
            return a
        if tree(edges[0][0]):
            return len(visit) == n
        return False