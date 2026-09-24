class Solution:
    def reverseWords(self, s: str) -> str:
        # with in build function
        words = s.split()
        words.reverse()
        return " ".join(words)
        # with out inbuild function
        result = ""
        word = ""
        i = len(s)-1
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            word = ""
            while i>=0 and s[i]!=" ":
                word = s[i]+word
                i-=1
            if word!="":
                if result !="":
                    result +=" "
                result +=word
        return result
        
        