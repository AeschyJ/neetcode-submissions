class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # from collections import defaultdict
        # take = defaultdict(list)
        take = {}
        for i in range(numCourses):
            take[i] = [x[1] for x in prerequisites if x[0] == i]
        pas = set()
        def travel(i, arr: list) -> bool:
            if not take[i]:
                pas.add(i)
                return True
            elif i in pas:
                return True
            arr.append(i)
            for t in take[i]:
                if t in arr:
                    return False
                arr.append(t)
                if not travel(t, arr):
                    return False
                arr.pop()
            pas.add(i)
            return True
        a = True
        for i in range(numCourses):
            a = a and travel(i, [])
        return a