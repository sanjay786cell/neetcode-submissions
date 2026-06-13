class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_sq = 0
        print(numSet)
        for n in nums:
            if n-1 not in numSet:
                length = 0
                
                while (n+length) in numSet:
                    print(n+length)
                    length +=1
                longest_sq = max(length, longest_sq)
        


        return longest_sq