from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find and store the highest element in the candies array

        # then iterate again through the candies array,comparing each element+extraCandies  with the highestNumber. \
        # if it's equal to or equal than the highestNumber, we store True.

        highest_number = max(candies)
        output = [c+extraCandies >= highest_number for c in candies]
        print(output)




candies = [2,3,5,1,3]
extraCandies = 3

solution = Solution()

solution.kidsWithCandies(candies, extraCandies)