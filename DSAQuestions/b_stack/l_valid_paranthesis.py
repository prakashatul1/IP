def isValid(s: str) -> bool:
    opening_brackets = {"(", "{", "["}
    closing_brackets = {")": "(", "}": "{", "]": "["}
    stack = []

    for each in s:  # Use the parameter 's' instead of type 'str'
        if each in opening_brackets:
            stack.append(each)
        else:
            # If stack is empty or the last opening bracket doesn't match the current closing bracket
            if not stack or closing_brackets[each] != stack[-1]:
                return False
            else:
                stack.pop()

    # If stack is empty, all brackets were balanced, otherwise, return False
    return not stack


print(isValid("()[]{}"))
