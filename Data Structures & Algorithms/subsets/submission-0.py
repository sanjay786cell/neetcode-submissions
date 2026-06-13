class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub_set = []
        def dfs(i):
            if i >= len(nums):
                res.append(sub_set.copy())
                return
            
            sub_set.append(nums[i])
            dfs(i+1)

            sub_set.pop()
            dfs(i+1)
        
        dfs(0)
        return res