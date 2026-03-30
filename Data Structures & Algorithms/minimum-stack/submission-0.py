class MinStack:

    def __init__(self):
        self.arr = []
        self.mn = float("inf")

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.arr[-1]

        while len(self.arr):
            mini = min(mini, self.arr[-1])
            tmp.append(self.arr.pop())

        while len(tmp):
            self.arr.append(tmp.pop())

        return mini
