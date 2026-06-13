class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = defaultdict()
        res = maxcount = 0
        for i in nums:
            s[i] = s.get(i, 0) + 1
            if maxcount < s[i]:
                res = i
                maxcount = s[i]
        return res