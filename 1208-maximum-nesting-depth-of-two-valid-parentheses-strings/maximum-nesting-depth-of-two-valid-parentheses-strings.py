class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        answer = []
        depth = 0
        for ch in seq:
            
            if ch == '(':
                depth+=1
                if depth%2 == 1:
                    answer.append(0)
                else:
                    answer.append(1)
            else:
                if depth%2 == 1:
                    answer.append(0)
                else:
                    answer.append(1)
                depth-=1
        return answer