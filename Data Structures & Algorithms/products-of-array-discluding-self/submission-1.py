class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        ls = [1] * len(nums)
        for i in range(len(nums)):
            ls[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            ls[i] *= postfix
            postfix *= nums[i]
        return ls
            
        
        
        