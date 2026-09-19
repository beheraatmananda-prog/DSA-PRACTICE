class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        i = 0
        j = 1
        ans = 1
        set_1= set()
        set_1.add(s[0])
        while j<n:
            while s[j] in set_1:
                set_1.discard(s[i])
                i+=1
            set_1.add(s[j])
            j+=1
            ans= max(ans,j-i)
        return ans