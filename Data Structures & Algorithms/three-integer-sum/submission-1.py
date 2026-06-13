class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        nums.sort()
        n = len(nums)
        for num in nums:
            count[num] += 1
            
        
        res=[]
        for i in range(n):
            count[nums[i]] -= 1
            print(count)
            if i and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                count[nums[j]] -= 1
                if j -1 > i and nums[j] == nums[j-1]:
                    continue
                
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i+1, n):
                count[nums[j]]+=1
        return res