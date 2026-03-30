class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        mini = self.stack[-1]
        temp = []

        while self.stack:
            mini = min(self.stack[-1], mini)
            temp.append(self.stack.pop())
        
        while temp:
            self.stack.append(temp.pop())
        
        return mini
