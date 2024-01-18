from stack import Stack


class Stack2(Stack):

    def __init__(self):
        self.minStackList = []
        super().__init__()

    def push(self, item):
        super().push(item)
        if len(self.minStackList) and self.minStackList[-1] > item:
            self.minStackList.append(item)
        elif len(self.minStackList) == 0:
            self.minStackList.append(item)

    def pop(self):
        temp = super().pop()
        if len(self.minStackList) and self.minStackList[-1] < temp:
            self.minStackList.pop()
        return temp

    def getMin(self):
        if len(self.minStackList):
            return self.minStackList[-1]
        else:
            return -1


if __name__ == "__main__":
    s = Stack2()
    s.push(2)
    s.push(3)
    s.push(5)
    s.push(0)
    s.push(7)
    s.pop()
    s.pop()
    print(s.getMin())
