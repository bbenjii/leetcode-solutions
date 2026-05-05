from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # iterate through flowerbed
        # whenever a flower can be placed, substract 1 from n
        # return n == 0

        length = len(flowerbed)
        i = 0

        def hasAdjacent(index):
            isFirst = index == 0
            isLast = index == length-1

            if isFirst and isLast:
                return flowerbed[index] == 1
            elif isFirst:
                return flowerbed[index + 1] == 1
            elif isLast:
                return flowerbed[index - 1] == 1
            else:
                return flowerbed[index + 1] == 1 or flowerbed[index - 1] == 1

        while i < length:
            # if there's currently a flower on this index, skip two indices
            if flowerbed[i] == 1:
                i += 2

            elif not hasAdjacent(i):
                n -= 1
                i += 2
            else:
                i += 1

            if n == 0:
                return True

        return n <= 0


sol = Solution()

flowerbed = [0,0,1,0,0]



n = 2

print(sol.canPlaceFlowers(flowerbed, n))
