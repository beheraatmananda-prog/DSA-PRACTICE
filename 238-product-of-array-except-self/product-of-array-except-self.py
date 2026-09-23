class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = [1] * len(nums)

        # Product of elements on the LEFT
        for i in range(len(nums)):
            ans[i] = product
            product = product * nums[i]

        # Product of elements on the RIGHT
        product = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * product
            product = product * nums[i]

        return ans