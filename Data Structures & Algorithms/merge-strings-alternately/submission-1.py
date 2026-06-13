class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        i = j = 0
        res = []
        while i < n1 and j < n2:
            res.append( word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        if i < n1:
            res.extend(word1[i:])
        if j < n2:
            res.extend(word2[j:])
        return "".join(res)