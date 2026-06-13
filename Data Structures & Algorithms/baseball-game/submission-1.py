class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            if operations[i] == '+':
                s = int(stack[-1]) + int(stack[-2])
                stack.append(str(s))
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == 'D':
                r = stack[-1]
                stack.append(str(int(r) * 2))
            else:
                stack.append(operations[i])
        print(stack)
        return sum(int(i) for i in stack)