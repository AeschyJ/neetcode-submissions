class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        for i in range(len(edges)):
            d[edges[i][0]].append(edges[i][1])
            d[edges[i][1]].append(edges[i][0])
        visit = set()
        def connect(node):
            if node in visit:
                return
            visit.add(node)
            for x in d[node]:
                if x not in visit:
                    connect(x)
        com = 0
        for x in range(n):
            if x not in visit:
                connect(x)
                com += 1
        return com