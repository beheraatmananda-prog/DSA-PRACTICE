class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        st = []
        if n%2 ==1:
            return False
        for ch in s:
            if ch =='[' or ch =='{' or ch =='(':
                st.append(ch)
            else:
                if len(st) ==0:
                    return False
                if ch ==']' and st[-1]!='[':
                    return False
                if ch ==')' and st[-1]!='(':
                    return False
                if ch =='}' and st[-1]!= '{':
                    return False
                st.pop()
        return len(st)==0
     