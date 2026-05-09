class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        from operator import itemgetter
        # d1 = defaultdict(list)
        d2 = defaultdict(int)
        t = 0
        for i in nums:
            d2[i] += 1
            # d1[d2[i]].append(i)
        a = []
        sort = sorted(d2.items(), key=itemgetter(1))
        for i, j in sort[-k:]:
            a.append(i)
        return list(set(a))