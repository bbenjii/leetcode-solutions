def divisable(numerator, denominator):
    l = len(denominator)

    if len(numerator) % l != 0:
        return False
    for i in range(int(len(numerator) / l)):
        n = numerator[i*l:i*l+l]
        if n != denominator:
            return False

    return True



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        print(str1, str2)

        # start with the longest possible denominator
        denominator = str1 if len(str1) < len(str2) else str2

        while len(denominator) > 0:
            if divisable(str1, denominator) and divisable(str2, denominator):
                break

            denominator = denominator[:-1]

        print(denominator)
        return denominator







str1 = "ABCABC"
str2 = "ABC"

Solution().gcdOfStrings(str1, str2)

# print(divisable(str1, str2))