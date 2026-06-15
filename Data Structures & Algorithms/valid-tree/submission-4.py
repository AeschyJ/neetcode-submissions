class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        if len(edges) != n - 1:
            return False
        d = defaultdict(list)
        for i in range(n-1):
                d[edges[i][1]].append(edges[i][0])
                d[edges[i][0]].append(edges[i][1])
        # print(d)
        visit = set()
        def tree(node, i = 1):
            if i > n:
                return False
            visit.add(node)
            if len(visit) > n:
                return False
            for leaf in d[node]:
                if leaf in visit: continue
                i = tree(leaf, i + 1)
            return i
        if n == 1:
            if not edges:
                return True
            return False
        if not edges:
            return False
        if tree(edges[0][0]):
            return len(visit) == n
        return False