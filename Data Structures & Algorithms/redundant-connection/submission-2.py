class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        double = defaultdict(list)
        for e in edges:
            double[e[0]].append(e[1])
            double[e[1]].append(e[0])
        path = set()
        def dfs(node, prev = None):
            if node in path:
                return path
            path.add(node)
            for e in double[node]:
                if e == prev: continue
                p = dfs(e, node)
                if p: return p
            path.remove(node)          
            return None
        a = [e for e in edges if e[0] in dfs(edges[0][0]) and e[1] in dfs(edges[0][0])]
        return a[-1]