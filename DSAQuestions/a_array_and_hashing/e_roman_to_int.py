def romanToInt(s: str) -> int:
    roman_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    for i in range(len(s) - 1):

        if roman_value[s[i]] < roman_value[s[i + 1]]:
            total -= roman_value[s[i]]
        else:
            total += roman_value[s[i]]

    return total + roman_value[s[-1]]


print(romanToInt("MCMXCIV"))
# 1994