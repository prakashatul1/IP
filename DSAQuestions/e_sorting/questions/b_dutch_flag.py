"""
Asymptotic complexity in terms of size of `balls` `n`:
* Time: O(n).
* Auxiliary space: O(1).
* Total space: O(n).
"""

FIRST_CHAR = 'R'
SECOND_CHAR = 'G'
THIRD_CHAR = 'B'


def swap(balls, i, j):
    balls[i], balls[j] = balls[j], balls[i]


def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    if not balls or len(balls) == 1:
        return balls

    # maintain 4 regions
    # 0 -> low - R
    # low -> mid - G
    # mid -> high - unknown
    # high -> end - B
    low, mid, high = 0, 0, len(balls) - 1

    while mid <= high:
        if balls[mid] == FIRST_CHAR:
            swap(balls, mid, low)
            # increase the low and mid regions
            low += 1
            mid += 1
        elif balls[mid] == SECOND_CHAR:
            # low to mid is in the right place
            mid += 1
        else:
            # will be last character
            swap(balls, mid, high)
            # lower the high number
            high -= 1

    return balls


print(dutch_flag_sort(["G", "B", "G", "G", "R", "B", "R", "G"]))
