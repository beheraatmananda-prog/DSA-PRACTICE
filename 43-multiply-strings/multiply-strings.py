class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 =="0" or num2 == "0":
            return "0"
        result = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                n1 = ord(num1[i])-ord('0')
                n2 = ord(num2[j])-ord('0')
                product = n1*n2
                post1 = i+j
                post2 = i+j+1
                total = product+result[post2]
                result[post2]= total%10
                result[post1]+= total//10
        result = ''.join(map(str,result)).lstrip('0')
        return result