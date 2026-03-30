class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for c in tokens:
            if c == "+":
                arr.append(arr.pop() + arr.pop())
            elif c == "-":
                a, b = arr.pop(), arr.pop()
                arr.append(b - a)
            elif c == "/":
                a, b = arr.pop(), arr.pop()
                arr.append(int(b / a))
            elif c == "*":
                arr.append(arr.pop() * arr.pop())
            else:
                arr.append(int(c))
        return arr[-1]