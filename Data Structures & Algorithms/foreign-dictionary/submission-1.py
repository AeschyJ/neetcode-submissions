class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1. 一次性建立 Node 集合與固定的 Adjacency / Indegree 字典
        nodes = {c for w in words for c in w}
        adj = {c: set() for c in nodes}
        indegree = {c: 0 for c in nodes}

        # 2. 建圖 (Inline 處理，省去 Function Call Stack 的成本)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
            else:
                if len(w1) > len(w2):
                    return ""

        # 3. BFS 拓撲排序 (Python 絕技：直接對 List append 並遍歷)
        queue = [c for c in nodes if indegree[c] == 0]
        for c in queue:
            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        # 4. 若 queue 長度等於所有點的總數，代表無 Cycle
        return "".join(queue) if len(queue) == len(nodes) else ""