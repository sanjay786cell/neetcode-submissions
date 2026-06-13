class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            current_num = nums[i]
            if current_num > 0 :
                break
            if i>0 and current_num == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                print(r)
                threesum = current_num + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([current_num, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
            