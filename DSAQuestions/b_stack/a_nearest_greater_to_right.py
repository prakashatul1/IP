from stack import Stack


def find_nearest_greater_to_right(array_list):
    calculation_stack = Stack()
    result_list = []

    # loop from ending to beginning since it is right
    for i in range(len(array_list) - 1, -1, -1):

        # for dry
        j = array_list[i]

        # 3 conditions

        # 1st - when starting with the loop
        if calculation_stack.stackSize == 0:
            result_list.append(-1)

        # after first loop
        elif calculation_stack.stackSize > 0:

            # 2nd Condition if next element is greater
            # found 1 result
            if calculation_stack.top() > j:
                result_list.append(calculation_stack.top())

            # 3rd Condition if next element is not grater
            elif calculation_stack.top() <= j:

                # loop till end of b_stack to find next greater
                # till one of the condition is met
                while calculation_stack.stackSize > 0 and \
                        calculation_stack.top() <= j:
                    calculation_stack.pop()

                # repeat the conditions 1 and 2
                if calculation_stack.stackSize == 0:
                    result_list.append(-1)

                else:
                    result_list.append(calculation_stack.top())

        # add element in b_stack for next loop calculation
        calculation_stack.push(j)

    return result_list[::-1]


array1 = [1, 7, 5, 3, 9, 4]
print(find_nearest_greater_to_right(array1))
