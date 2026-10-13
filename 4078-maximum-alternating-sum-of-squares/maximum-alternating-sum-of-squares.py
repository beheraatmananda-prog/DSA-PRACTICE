class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x: abs(x),reverse = True)
        ans = 0
        n = len(nums)
        for i in range(n):
            if i<(n+1)//2:
                ans+=nums[i]**2
            else:
                ans-=nums[i]**2
        return ans