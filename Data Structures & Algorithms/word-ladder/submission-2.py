from typing import List
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # 📦 1. 預處理鄰居：用 Wildcard Pattern 建立 Adjacency List
        # 這樣就不用在每一層遞迴都用 List Comprehension 做全清單線性掃描
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)
        
        self.min_ans = float('inf')
        path = set()
        
        def dfs(word):
            # ✂️ 2. 全域動態剪枝：如果當前路徑長度已經追平或超越已知最優解，直接認輸回頭
            if len(path) >= self.min_ans:
                return
            
            # 達陣：成功走到終點，更新全域最短紀錄
            if word == endWord:
                self.min_ans = min(self.min_ans, len(path))
                return
            
            # 🔍 3. 透過 Pattern 實現 O(1) 快速撈出鄰居
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for next_word in neighbors[pattern]:
                    if next_word not in path:
                        path.add(next_word)
                        dfs(next_word)
                        path.remove(next_word) # 🧼 乾淨的 Backtracking 狀態回復
        
        # 核心啟動點
        path.add(beginWord)
        dfs(beginWord)
        
        return self.min_ans if self.min_ans != float('inf') else 0