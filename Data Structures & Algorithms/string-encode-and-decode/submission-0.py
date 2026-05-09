class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for i in strs:
            # a += str(len(i))
            a += ("中")
            a += i
        return a
    def decode(self, s: str) -> List[str]:
        a = []
        if s.find("中") != -1:
            a = s.split("中")
        return a[1:]
            

            
