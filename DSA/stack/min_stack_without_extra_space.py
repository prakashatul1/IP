import sys

from stack import Stack


class Stack3(Stack):

    def __init__(self):
        self.minEle = -sys.maxsize - 1
        super().__init__()

    def push(self, item):
        if self.stackSize > 0:
            if item < self.minEle:
                self.stackList.append((2 * item) - self.minEle)
                self.minEle = item
            else:
                self.stackList.append(item)
        else:
            self.stackList.append(item)
            self.minEle = item
        self.stackSize += 1

    def pop(self):
        if self.stackSize == 0:
            return -1
        elif self.stackList[-1] >= self.minEle:
            temp = self.stackList.pop()
            self.stackSize -= 1
            return temp
        elif self.stackList[-1] < self.minEle:
            temp = self.minEle
            self.minEle = 2 * self.minEle - self.stackList[-1]
            self.stackList.pop()
            self.stackSize -= 1
            return temp

    def getMin(self):
        if self.stackSize > 0:
            return self.minEle
        else:
            return -1

    def top(self):
        if self.stackSize == 0:
            return -1
        elif self.stackList[-1] >= self.minEle:
            return self.stackList[-1]
        elif self.stackList[-1] < self.minEle:
            return self.minEle


if __name__ == "__main__":
    s = Stack3()
    s.push(2)
    s.push(3)
    s.push(5)
    s.push(0)
    s.push(7)
    s.pop()
    s.pop()
    print(s.getMin())
