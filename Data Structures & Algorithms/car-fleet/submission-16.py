class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [(p, s) for p, s in zip(position, speed)]
        fleet.sort(reverse=True)
        stack = []

        for p, s in fleet:
            v = (target - p) / s
            stack.append(v)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)