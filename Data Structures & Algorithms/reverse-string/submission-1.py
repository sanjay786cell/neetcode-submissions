class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, n = 0, len(s)
        while i < n:
            p = s.pop()
            s.insert(i, p)
            i+=1
        