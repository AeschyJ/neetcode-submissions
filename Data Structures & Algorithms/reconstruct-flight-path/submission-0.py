class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        adj = defaultdict(list)
        
        # 1. 建立 Adjacency List 並將目的地排序
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        res = []
        
        # 2. Hierholzer's Algorithm (DFS)
        def dfs(airport: str):
            while adj[airport]:
                next_airport = adj[airport].pop()
                dfs(next_airport)
            res.append(airport)  # 死胡同節點最先被 append
            
        dfs("JFK")
        
        # 3. 反轉結果
        return res[::-1]