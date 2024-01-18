from stack import Stack


def find_nearest_greater_to_left(array_list):
    calculation_stack = Stack()
    result_list = []

    # loop from beginning to ending since it is left
    for i in range(len(array_list)):

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

                # loop till end of stack to find next greater
                # till one of the condition is met
                while calculation_stack.stackSize > 0 and \
                        calculation_stack.top() <= j:
                    calculation_stack.pop()

                # repeat the conditions 1 and 2
                if calculation_stack.stackSize == 0:
                    result_list.append(-1)

                else:
                    result_list.append(calculation_stack.top())

        # add element in stack for next loop calculation
        calculation_stack.push(j)

    return result_list


print(find_nearest_greater_to_left([1, 3, 2, 4]))
