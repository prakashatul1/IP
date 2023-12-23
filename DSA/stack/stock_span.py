from stack import Stack


# similar to nearest greater to left
# can be also seen as
# consecutive smaller or equal to before it
def find_consecutive_smaller_or_equal_before(a):

    s = Stack()
    v = []

    for i in range(len(a)):

        if s.stackSize == 0:
            v.append(-1)

        if s.stackSize > 0:

            # comapre with element value
            # append the index of value
            if s.top()[0] > a[i]:
                v.append(s.top()[1])

            elif s.top()[0] <= a[i]:

                while s.stackSize > 0 and s.top()[0] <= a[i]:
                    s.pop()

                if s.stackSize == 0:
                    v.append(-1)

                else:
                    v.append(s.top()[1])

        # this will identify that s stack has a tuple
        # of size 2
        s.push((a[i], i))

    print(v)
    # now this loop is required to find
    # difference between index and
    # nearest greatest index
    for i in range(len(v)):
        v[i] = i - v[i]

    return v


print(find_consecutive_smaller_or_equal_before(
    [100, 80, 60, 70, 60, 75, 85]
))
