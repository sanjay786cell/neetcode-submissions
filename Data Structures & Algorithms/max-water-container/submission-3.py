class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n -1
        res = 0
        
            
        while l < r:
            area_of_w = min(heights[l], heights[r]) * (r-l)
            res = max(res, area_of_w)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res