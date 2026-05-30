class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.mini = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.mini)
            if val < self.mini:
                self.mini = val

    def pop(self) -> None:
        if not self.stack:
            return
        last = self.stack.pop()
        if last < 0:
            self.mini = self.mini - last

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.mini
        else:
            return self.mini

    def getMin(self) -> int:
        return self.mini
