class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        h = {}
        g = {}
        for c in s:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1
        for c in t:
            if c in g:
                g[c] += 1
            else:
                g[c] = 1
        return h == g