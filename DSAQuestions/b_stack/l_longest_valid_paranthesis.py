def longestValidParentheses(s: str) -> int:
    max_length = 0
    stack = [-1]  # Initialize stack with -1 to handle base case for valid substring starting at index 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Push the index of '(' onto the stack
        else:
            stack.pop()  # Pop the last '(' index off the stack
            if not stack:
                stack.append(i)  # No matching '(', update the base index for the next valid substring
            else:
                # Calculate the length of the current valid substring
                max_length = max(max_length, i - stack[-1])

    return max_length


print(longestValidParentheses(")()())"))
# result = 4
