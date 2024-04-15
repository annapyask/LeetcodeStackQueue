from collections import deque
class FreqStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.appendleft(val)

    def pop(self) -> int:
        counter = 0
        indexx = 0
        set_qu = set(self.stack)
        if self.stack:
            for i in set_qu:
                if self.stack.count(i) == counter:
                    if self.stack.index(i) < indexx:
                        counter = self.stack.count(i)
                        num = i
                        indexx = self.stack.index(num)
                if self.stack.count(i) > counter:
                    counter = self.stack.count(i)
                    num = i
                    indexx = self.stack.index(num)
            self.stack.remove(num)
            return num
