class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        for i in nums:
            dict_[i] = 1 + dict_.get(i, 0)
        
        arr = []
        for num, cnt in dict_.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
        return 
                
        