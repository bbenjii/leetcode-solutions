from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""

        pointer1 = 0
        pointer2 = 0
        current_group = chars[0]
        current_length = 0
        while pointer2 < len(chars):
            char = chars[pointer2]

            if char == current_group:
                current_length += 1
            else:
                chars[pointer1] = current_group
                pointer1 += 1
                if current_length > 1:
                    length = list(str(current_length))
                    for c in length:
                        chars[pointer1] = c
                        pointer1 += 1


                current_group = char
                current_length = 1

            pointer2 += 1

        chars[pointer1] = current_group
        pointer1 += 1
        if current_length > 1:
            length = list(str(current_length))
            for c in length:
                chars[pointer1] = c
                pointer1 += 1

        return pointer1

sol = Solution()


chars = ["a","a","b","b","c","c","c"]


print(sol.compress(chars))
