class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from collections import deque, defaultdict
        
        if len(words) == 1:
            return words[0]
        adj = defaultdict(set)
        indegree = defaultdict(int)
        seen = set()

        for word in words:
            for c in word:
                seen.add(c)

        def graphing(w1, w2):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
            else:
                if len(w1) > len(w2):
                    return False
            return True
        
        for i in range(len(words)-1):
            if not graphing(words[i], words[i+1]):
                return ""
        know = deque()
        for c in seen:
            if indegree[c] == 0:
                know.append(c)
        a = []
        while know:
            c = know.popleft()
            a.append(c)
            for edge in adj[c]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    know.append(edge)
        ans = "".join(a)
        return ans if len(seen) == len(ans) else ""