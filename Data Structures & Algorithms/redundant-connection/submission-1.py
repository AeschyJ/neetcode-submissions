class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        double = defaultdict(list)
        for e in edges:
            double[e[0]].append(e)
            double[e[1]].append(e[::-1])
        path = set()
        def dfs(node, prev = None):
            # print(node, prev)
            if node in path:
                # print(path)
                return path
            path.add(node)
            for e in double[node]:
                if e[1] == prev: continue
                p = dfs(e[1], node)
                if p: return p
            path.remove(node)          
            return None
        a = [e for e in edges if e[0] in dfs(edges[0][0]) and e[1] in dfs(edges[0][0])]
        # print(a)
        return a[-1]