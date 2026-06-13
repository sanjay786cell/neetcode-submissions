class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        nums = sorted(nums)
        print(nums)
        for i in nums:
            count += 1
            if len(nums) - count + 1 == k:
                return i
        
        return 0
