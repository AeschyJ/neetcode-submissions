class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            count = [0] *26
            for s in i:
                count[ord(s)-ord('a')] +=1
            d[tuple(count)].append(i)
        return list(d.values())

