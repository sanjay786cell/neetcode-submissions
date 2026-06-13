class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        cnt_stack = []
        cur = ""
        k = 0
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                str_stack.append (cur)
                cnt_stack.append(k)
                cur = ""
                k=0
            elif c == ']':
                temp = cur
                cur = str_stack.pop()
                count = cnt_stack.pop()
                cur += temp * count
            else:
                cur += c
        return cur
                
