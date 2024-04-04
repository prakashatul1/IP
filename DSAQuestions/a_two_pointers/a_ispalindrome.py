def isPalindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1
    while j > i:
        # Corrected conditions: `j > i` ensures we're looking within the bounds of the string.
        while j > i and not isalnum(s[j]):
            j -= 1
        while i < j and not isalnum(s[i]):
            i += 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def isalnum(st):
    # Checks if `st` is a single character and if it's alphanumeric
    return (
            (ord("A") <= ord(st) <= ord("Z")) or
            (ord("a") <= ord(st) <= ord("z")) or
            (ord("0") <= ord(st) <= ord("9"))
    )


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
