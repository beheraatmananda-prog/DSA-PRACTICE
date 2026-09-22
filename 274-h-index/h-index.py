class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        n = len(citations)
        h = 0
        for i in range(n):
            papers = n-i
            if citations[i]>=papers:
                h = max(h,papers)
        return h