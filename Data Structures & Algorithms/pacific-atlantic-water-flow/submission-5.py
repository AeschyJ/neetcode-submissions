class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0] :return []
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        rows, cols = len(heights), len(heights[0])
        
        p = set()
        a = set()
        def travel(r, c, reach):
            reach.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in reach:
                    if heights[nr][nc] >= heights[r][c]:
                        travel(nr, nc, reach)
        for r in range(rows):
            travel(r, 0, p)
            travel(r, cols -1, a)
        for c in range(cols):
            travel(0, c, p)
            travel(rows -1, c, a)
        return [list(x) for x in p & a]