from stack import Stack


def find_maximum_area_histogram(a):
    s = Stack()
    v = []

    s2 = Stack()
    v2 = []

    # NSL
    for i in range(len(a)):
        if s.stackSize == 0:
            v.append(-1)
        elif s.stackSize > 0:
            if s.top()[0] < a[i]:
                v.append(s.top()[1])
            elif s.top()[0] >= a[i]:
                while s.stackSize > 0 and s.top()[0] >= a[i]:
                    s.pop()
                if s.stackSize == 0:
                    v.append(-1)
                else:
                    v.append(s.top()[1])
        s.push((a[i], i))

    # print(v)

    # NSR
    for i in range(len(a) - 1, -1, -1):
        if s2.stackSize == 0:
            v2.append(len(a))
        elif s2.stackSize > 0:
            if s2.top()[0] < a[i]:
                v2.append(s2.top()[1])
            elif s2.top()[0] >= a[i]:
                while s2.stackSize > 0 and s2.top()[0] >= a[i]:
                    s2.pop()
                if s2.stackSize == 0:
                    v2.append(len(a))
                else:
                    v2.append(s2.top()[1])
        s2.push((a[i], i))

    v2 = v2[::-1]
    # print(v2)

    result = 0

    for i in range(len(a)):
        temp = v2[i] - v[i] - 1
        result = max(result, temp * a[i])

    return result


print(find_maximum_area_histogram([6, 2, 5, 4, 5, 1, 6]))
print(find_maximum_area_histogram([1, 8, 6, 2, 5, 4, 8, 3, 7]))
