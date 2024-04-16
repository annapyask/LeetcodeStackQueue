from collections import deque, defaultdict

class FreqStack:

    def __init__(self):
        self.stack = deque()
        self.dictio = defaultdict(int)
        self.maximum = defaultdict(list)
        self.count = 0

    def push(self, val: int) -> None:
        self.stack.appendleft(val)
        self.dictio[val] += 1
        num = self.dictio[val]
        if num > self.count:
            self.count = num
        self.maximum[num].append(val)

    def pop(self) -> int:
        if not self.stack:
            return None
        val = self.maximum[self.count].pop()
        if not self.maximum[self.count]:
            self.count -= 1
        self.dictio[val] -= 1
        self.stack.remove(val)
        return val
