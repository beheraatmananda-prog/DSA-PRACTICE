class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        minimum = float('inf')
        for right in range (len(nums)):
            curr_sum += nums[right]
            while curr_sum >=target:
                minimum = min(minimum,right-left+1)
                curr_sum-=nums[left]
                left+=1
        if minimum == float('inf'):
            return 0
        return minimum