class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n -1
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                area_of_w = min(heights[i],heights[j]) * (j-i)
                print(i, j, area_of_w)
                res = max(res, area_of_w)
        return res