class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        take = {}
        for i in range(numCourses):
            take[i] = [x[1] for x in prerequisites if x[0] == i]
        pas = set()
        ans = []
        def travel(i, arr: list) -> bool:
            if i in pas:
                return True
            if not take[i]:
                pas.add(i)
                ans.append(i)
                return True
            arr.append(i)
            for t in take[i]:
                if t in arr:
                    return False
                if not travel(t, arr):
                    return False
            if arr: arr.pop()
            pas.add(i)
            ans.append(i)
            return True
        a = True
        for i in range(numCourses):
            a = a and travel(i, [])
        return [] if not a else ans