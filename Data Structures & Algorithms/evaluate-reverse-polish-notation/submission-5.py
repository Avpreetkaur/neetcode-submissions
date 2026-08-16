class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num in "+-*/":
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if num == "+":
                    res = operand1 + operand2
                elif num == "-":
                    res = operand2 - operand1
                elif num == "*":
                    res = operand1 * operand2
                else:
                    res = operand2 / operand1
                print(res)
                stack.append(res)
            else:
                stack.append(num)
        return int(stack[-1])