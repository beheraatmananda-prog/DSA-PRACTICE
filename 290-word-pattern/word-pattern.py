class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern)!=len(words):
            return False
        map_p = {}
        map_w = {}
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if p in map_p:
                if map_p[p]!=w:
                    return False
            else:
                map_p[p] = w
            if w in map_w:
                if map_w[w]!=p:
                    return False
            else:
                map_w[w] = p
        return True