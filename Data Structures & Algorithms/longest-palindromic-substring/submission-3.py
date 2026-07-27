class Solution:
    def longestPalindrome(self, s: str) -> str:
        rs = list(reversed(s))
        ans = []
        for i, c in enumerate(s):
            if len(ans) >= len(s) - i:
                break
            for ri, rc in enumerate(rs):
                if c == rc:
                    ti, tri = i, ri
                    tmp = []
                    while ti < len(s) and tri < len(s) and s[ti] == rs[tri]:
                        tmp.append(s[ti])
                        ti += 1
                        tri += 1
                    # print(tmp, i, tri)
                    if tri != len(s) - i:
                        pass
                    elif len(tmp) > len(ans):
                        ans = tmp
        return "".join(ans)