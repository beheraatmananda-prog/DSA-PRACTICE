class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def union(A, B):
            return A | B
        def product(A,B):
            return {a+b for a in A for b in B}
        def parse(i):
            result = set()
            current = {""}
            while i<len(expression) and expression[i]!='}':
                if expression[i] == '{':
                    sub_result,i = parse(i+1)
                elif expression[i] ==',':
                    result = union(result,current)
                    current = {""}
                    i+=1
                    continue
                else:
                    sub_result = {expression[i]}
                    i+=1
                current = product(current,sub_result)
            result = union(result,current)
            return result,i+1
        result,_=parse(0)
        return sorted(result)