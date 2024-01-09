from stack import Stack


def find_nearest_smaller_to_left(a):
    s = Stack()
    v = []

    for i in range(len(a)):

        if s.stackSize == 0:
            v.append(-1)

        elif s.stackSize > 0:

            if s.top() < a[i]:
                v.append(s.top())

            elif s.top() >= a[i]:

                while s.stackSize > 0 and s.top() >= a[i]:
                    s.pop()

                if s.stackSize == 0:
                    v.append(-1)
                else:
                    v.append(s.top())

        s.push(a[i])

    return v


print(find_nearest_smaller_to_left([4, 5, 2, 10, 8]))
